import struct
from typing import ClassVar, Optional

import attr

from elgas.parameters.enumerations import ParameterObjectType
from elgas.utils import pop_many, pretty_text


@attr.s(auto_attribs=True)
class TariffCounter:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.TARIFF_COUNTER
    data_length: ClassVar[int] = 4

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
    name: str
    unit: str
    digit: float
    number_of_primary_counter: int
    tariff: int
    address_in_daily_archive_record: int
    address_in_monthly_archive_record: int
    address_in_billing_archive_record: int
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
        name = pretty_text(pop_many(data, 23))
        unit = pretty_text(pop_many(data, 8))
        digit = struct.unpack("<d", pop_many(data, 8))[0]
        number_of_primary_counter = data.pop(0)
        tariff = data.pop(0)
        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_billing_archive_record = int.from_bytes(pop_many(data, 2), "little")

        if data:
            decimals = data.pop(0)
        else:
            decimals = None

        assert not data

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
            name=name,
            unit=unit,
            digit=digit,
            number_of_primary_counter=number_of_primary_counter,
            tariff=tariff,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            address_in_billing_archive_record=address_in_billing_archive_record,
            decimals=decimals,
        )


class DoubleTariffCounter(TariffCounter):
    object_type: ClassVar[
        ParameterObjectType
    ] = ParameterObjectType.DOUBLE_TARIFF_COUNTER
    data_length: ClassVar[int] = 8


@attr.s(auto_attribs=True)
class BaseTariffCounter:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.BASE_TARIFF_COUNTER
    data_length: ClassVar[int] = 8

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str
    unit: str
    number_of_base_counter: int
    tariff: int
    address_in_daily_archive_record: int
    address_in_monthly_archive_record: int
    address_in_billing_archive_record: int
    decimals: Optional[int]

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        address_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        address_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_control = data.pop(0)
        name = pretty_text(pop_many(data, 23))
        unit = pretty_text(pop_many(data, 8))
        number_of_base_counter = data.pop(0)
        tariff = data.pop(0)
        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_billing_archive_record = int.from_bytes(pop_many(data, 2), "little")

        if data:
            decimals = data.pop(0)
        else:
            decimals = None

        assert not data

        return cls(
            number=number,
            id=id,
            address_in_actual_values=address_in_actual_values,
            address_in_data_archive_record=address_in_data_archive_record,
            bit_control=bit_control,
            name=name,
            unit=unit,
            number_of_base_counter=number_of_base_counter,
            tariff=tariff,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            address_in_billing_archive_record=address_in_billing_archive_record,
            decimals=decimals,
        )
