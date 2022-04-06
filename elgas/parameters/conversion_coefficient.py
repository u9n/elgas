import struct
from typing import ClassVar, Optional

import attr

from elgas.parameters.enumerations import ParameterObjectType
from elgas.utils import pop_many, pretty_text


@attr.s(auto_attribs=True)
class ConversionCoefficient:
    object_type: ClassVar[
        ParameterObjectType
    ] = ParameterObjectType.CONVERSION_COEFFICIENT
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

    number_of_analog_pressure: int
    number_of_analog_temperature: int
    compressibility_calculation_method: int
    default_value_pressure: float
    default_value_temperature: float
    alternate_value_of_compressibility: float
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
        number_of_analog_pressure = data.pop(0)
        number_of_analog_temperature = data.pop(0)
        compressibility_calculation_method = data.pop(0)
        default_value_pressure = struct.unpack("<f", pop_many(data, 4))[0]
        default_value_temperature = struct.unpack("<f", pop_many(data, 4))[0]
        alternate_value_of_compressibility = struct.unpack("<f", pop_many(data, 4))[0]
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
            number_of_analog_pressure=number_of_analog_pressure,
            number_of_analog_temperature=number_of_analog_temperature,
            compressibility_calculation_method=compressibility_calculation_method,
            default_value_pressure=default_value_pressure,
            default_value_temperature=default_value_temperature,
            alternate_value_of_compressibility=alternate_value_of_compressibility,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            decimals=decimals,
        )
