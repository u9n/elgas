import datetime
from typing import Any

import attr
import structlog

from elgas import application, connection, constants, state, transport

LOG = structlog.get_logger("client")


@attr.s(auto_attribs=True)
class ElgasClient:
    """Elgas client"""

    transport: transport.ElgasTransport
    password: str
    elgas_connection: connection.ElgasConnection = attr.ib(
        default=attr.Factory(
            lambda self: connection.ElgasConnection(
                password=self.password,
                password_id=801,
                destination_address_1=0,
                destination_address_2=0,
                source_address_1=0,
                source_address_2=0,
            ),
            takes_self=True,
        )
    )

    def connect(self):
        self.transport.connect()

    def disconnect(self):
        self.transport.disconnect()

    def send(self, *events):
        for event in events:
            data = self.elgas_connection.send(event)
            self.transport.send(data)
            response_data = self.transport.recv()
            self.elgas_connection.receive_data(response_data)

    def next_event(self) -> Any:
        while True:
            event = self.elgas_connection.next_event()
            if event is state.NEED_DATA:
                self.elgas_connection.receive_data(self.transport.recv())
                continue
            return event

    def read_values(self):
        request = application.ReadActualValuesRequest(password=self.password)
        self.send(request)
        response = self.next_event()
        LOG.info(response)

    def read_time(self):
        request = application.ReadTimeRequest()
        self.send(request)
        response: application.ReadTimeResponse = self.next_event()
        LOG.info(response)
        LOG.info("Got device time", time=response.time.isoformat())

    def read_parameters(self):
        request = application.ReadDeviceParametersRequest(
            password=self.password, object_count=1, buffer_length=1024
        )
        self.send(request)
        response = self.next_event()
        # TODO: How do we initial to recieve all the other data?
        LOG.info(response)

    def read_archive_by_time(self):
        request = application.ReadArchiveByTimeRequest(
            password=self.password,
            archive=constants.Archive.DATA,
            amount=1,
            last_date=datetime.datetime.now() - datetime.timedelta(days=1),
        )
        self.send(request)
        response = self.next_event()
        # TODO: How do we initial to recieve all the other data?
        LOG.info(response)
        LOG.info("Record data", data=response.data.hex())
