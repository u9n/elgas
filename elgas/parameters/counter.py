import struct
from typing import ClassVar, Optional

import attr

from elgas.parameters.enumerations import ParameterObjectType
from elgas.utils import pop_many, pretty_text


@attr.s(auto_attribs=True)
class Counter:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.COUNTER
    value_length: ClassVar[int] = 4

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int
    in_data_archive: bool
    in_daily_archive: bool
    in_monthly_archive: bool
    in_factory_archive: bool
    is_metrological_quantity: bool
    accept_counting_direction: bool
    name: str
    unit: str
    digit: float
    serial_number_of_gas_meter: int

    error_bit_order_in_actual_values: int
    error_bit_order_in_binary_archive: int
    error_bit_order_in_data_archive: int
    address_in_daily_archive_record: int
    address_in_monthly_archive_record: int
    address_in_billing_archive_record: int
    serial_number_of_gas_meter_text: str

    decimals: Optional[int]

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        address_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        address_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_control = data.pop(0)
        in_data_archive = bool(bit_control & 0b00000001)
        in_daily_archive = bool(bit_control & 0b00000010)
        in_monthly_archive = bool(bit_control & 0b00000100)
        in_factory_archive = bool(bit_control & 0b00001000)
        is_metrological_quantity = bool(bit_control & 0b00010000)
        accept_counting_direction = bool(bit_control & 0b01000000)
        name = pretty_text(pop_many(data, 23))
        unit = pretty_text(pop_many(data, 8))
        digit = struct.unpack("<d", pop_many(data, 8))[0]
        serial_number_of_gas_meter = int.from_bytes(pop_many(data, 4), "little")
        error_bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        error_bit_order_in_binary_archive = int.from_bytes(pop_many(data, 2), "little")
        error_bit_order_in_data_archive = int.from_bytes(pop_many(data, 2), "little")
        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_billing_archive_record = int.from_bytes(pop_many(data, 2), "little")
        serial_number_of_gas_meter_text = pretty_text(pop_many(data, 17))

        if data:
            decimals = data.pop(0)
        else:
            decimals = None

        return cls(
            number=number,
            id=id,
            address_in_actual_values=address_in_actual_values,
            address_in_data_archive_record=address_in_data_archive_record,
            bit_control=bit_control,
            in_data_archive=in_data_archive,
            in_daily_archive=in_daily_archive,
            in_monthly_archive=in_monthly_archive,
            in_factory_archive=in_factory_archive,
            is_metrological_quantity=is_metrological_quantity,
            accept_counting_direction=accept_counting_direction,
            name=name,
            unit=unit,
            digit=digit,
            serial_number_of_gas_meter=serial_number_of_gas_meter,
            error_bit_order_in_actual_values=error_bit_order_in_actual_values,
            error_bit_order_in_binary_archive=error_bit_order_in_binary_archive,
            error_bit_order_in_data_archive=error_bit_order_in_data_archive,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            address_in_billing_archive_record=address_in_billing_archive_record,
            serial_number_of_gas_meter_text=serial_number_of_gas_meter_text,
            decimals=decimals,
        )


class DoubleCounter(Counter):
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.DOUBLE_COUNTER
    value_length: ClassVar[int] = 8  # double
