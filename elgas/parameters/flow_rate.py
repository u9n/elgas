from typing import ClassVar, Optional

import attr

from elgas.parameters.enumerations import ParameterObjectType
from elgas.utils import pop_many, pretty_text


@attr.s(auto_attribs=True)
class FlowRate:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.FLOW_RATE
    value_length: ClassVar[int] = 4

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int
    in_data_archive: int
    in_daily_archive: int
    in_monthly_archive: int
    is_metrological_quantity: int
    name: str
    unit: str

    error_bit_order_in_actual_values: int
    error_bit_order_in_binary_archive: int
    error_bit_order_in_data_archive: int
    address_in_daily_archive_record: int
    address_in_monthly_archive_record: int
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
        is_metrological_quantity = bool(bit_control & 0b00010000)
        name = pretty_text(pop_many(data, 23))
        unit = pretty_text(pop_many(data, 8))

        error_bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        error_bit_order_in_binary_archive = int.from_bytes(pop_many(data, 2), "little")
        error_bit_order_in_data_archive = int.from_bytes(pop_many(data, 2), "little")
        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")

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
            is_metrological_quantity=is_metrological_quantity,
            name=name,
            unit=unit,
            error_bit_order_in_actual_values=error_bit_order_in_actual_values,
            error_bit_order_in_binary_archive=error_bit_order_in_binary_archive,
            error_bit_order_in_data_archive=error_bit_order_in_data_archive,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            decimals=decimals,
        )


@attr.s(auto_attribs=True)
class StandardFlowRate:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.STANDARD_FLOW_RATE
    value_length: ClassVar[int] = 4

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int
    in_data_archive: int
    in_daily_archive: int
    in_monthly_archive: int
    is_metrological_quantity: int
    name: str
    unit: str
    number_of_primary_flow_rate: int
    number_of_conversion: int
    address_in_daily_archive_record: int
    address_in_monthly_archive_record: int
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
        is_metrological_quantity = bool(bit_control & 0b00010000)
        name = pretty_text(pop_many(data, 23))
        unit = pretty_text(pop_many(data, 8))

        number_of_primary_flow_rate = data.pop(0)
        number_of_conversion = data.pop(0)
        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")

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
            is_metrological_quantity=is_metrological_quantity,
            name=name,
            unit=unit,
            number_of_primary_flow_rate=number_of_primary_flow_rate,
            number_of_conversion=number_of_conversion,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            decimals=decimals,
        )
