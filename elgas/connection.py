from __future__ import annotations

from typing import *

import attr
import structlog

from elgas import application, constants, frames, state, utils
from elgas.security import EncryptionKeyId

LOG = structlog.get_logger("connection")


@attr.s(auto_attribs=True)
class ResponsePduFactory:
    """
    Creates PDU classes from Elgas Responses via the service number.
    """

    service_map: ClassVar[Mapping] = {
        constants.ServiceNumber.READ_VALUES: application.ReadActualValuesResponse,
        constants.ServiceNumber.READ_DEVICE_TIME: application.ReadTimeResponse,
        constants.ServiceNumber.READ_SCADA_PARAMETERS: application.ReadDeviceParametersResponse,
        constants.ServiceNumber.READ_ARCHIVES_BY_DATE: application.ReadArchiveByTimeResponse,
    }

    @staticmethod
    def from_response(response: frames.Response):
        klass = ResponsePduFactory.service_map[response.service]
        return klass.from_bytes(response.data)


@attr.s(auto_attribs=True)
class ElgasConnection:
    """
    address1 is used for addressing measuring place  0-65535
    address2 is used for addressing concrete measuring place 0-255
    TODO: exactly what does that mean?..
    Address 0 in any will make all devices respond. In the response the correct
    address will be sent.


    """

    source_address_1: int = attr.ib(
        validator=[attr.validators.ge(0), attr.validators.le(65535)]
    )
    source_address_2: int = attr.ib(
        validator=[attr.validators.ge(0), attr.validators.le(255)]
    )
    destination_address_1: int = attr.ib(
        validator=[attr.validators.ge(0), attr.validators.le(65535)]
    )
    destination_address_2: int = attr.ib(
        validator=[attr.validators.ge(0), attr.validators.le(255)]
    )

    password: str = attr.ib(validator=[attr.validators.max_len(6)])
    password_id: int = attr.ib(
        validator=[attr.validators.ge(801), attr.validators.le(849)]
    )

    encryption_key: bytes | None = attr.ib(default=None)
    encryption_key_id: EncryptionKeyId | None = attr.ib(default=None)
    # TODO: Validate that there is an encryption key id if there is an encryption key.

    buffer: bytearray = attr.ib(init=False, factory=bytearray)
    elgas_state: state.ElgasState = attr.ib(factory=state.ElgasState)

    def send(self, event) -> bytes:

        LOG.debug("Sending request PDU", pdu=event)

        if self.encryption_key:
            raise NotImplementedError("encryption not implemented")

        else:
            application_data = event.to_bytes()
            request = frames.Request(
                service=event.service,
                destination_address_1=self.destination_address_1,
                destination_address_2=self.destination_address_2,
                source_address_1=self.source_address_1,
                source_address_2=self.source_address_2,
                data=application_data,
            )

        LOG.debug("Sending ELGAS request", request=request)
        frame_data = request.to_bytes()
        escaped_data = utils.escape_characters(frame_data)
        return escaped_data

    def receive_data(self, data: bytes):
        """
        Add data into the receive buffer.
        After this you could call next_event
        """
        if data:
            self.buffer += data
            LOG.debug(
                f"Added data to connection buffer", data=data, total_buffer=self.buffer
            )

    def next_event(self) -> bytes:

        if not self.buffer:
            return state.NEED_DATA

        # do we have an end char?
        try:
            end_char_index = self.buffer.index(b"\x0d") + 1
        except ValueError:
            # No end char in buffer and we need more data.
            return state.NEED_DATA

        data = self.buffer[:end_char_index]

        # TODO: Check if encrypted!
        response = frames.Response.from_bytes(utils.return_characters(data))
        LOG.debug("Received ELGAS response", response=response)
        pdu = ResponsePduFactory.from_response(response)

        self.buffer = bytearray()  # clear buffer

        return pdu
