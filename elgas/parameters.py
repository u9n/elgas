import struct
from enum import IntEnum
from typing import *

import attr


def pop_many(array: bytearray, amount: int) -> bytearray:
    if amount < 2:
        raise ValueError("Only use pop_many if you need to get more than 1 byte")
    out = bytearray()
    for _ in range(0, amount):
        out.append(array.pop(0))
    return out


class DeviceType(IntEnum):
    ELCOR = 128
    ELCOR_PLUS = 131


class CertificationVariant(IntEnum):
    CMI_MID = 2
    GENERIC = 4


class SwitchFunction(IntEnum):
    NONE = 0
    PROTECT_METROLOGICAL = 1
    PROTECT_ALL = 2


class CompressibilityFormula(IntEnum):
    CONST = 0
    AGANX19 = 1
    SGERG88 = 2
    AGANX19MOD = 3
    AGA8G1 = 4
    AGA8G2 = 5
    AGA892DC = 6
    GOSTNX19MOD = 7


@attr.s(auto_attribs=True)
class GasComposition:
    co2: float
    n2: float
    combustion_heat: float
    relative_density: float
    h2: float
    h2s: float
    he: float
    h2o: float
    o2: float
    ar: float
    co: float
    c1h4: float
    c2h6: float
    c3h8: float
    ic4h10: float
    nc4h10: float
    ic5h12: float
    nc5h12: float
    c6h14: float
    c7h16: float
    c8h18: float
    c9h20: float
    c10h22: float

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)

        return cls(
            co2=struct.unpack("<f", pop_many(data, 4))[0],
            n2=struct.unpack("<f", pop_many(data, 4))[0],
            combustion_heat=struct.unpack("<f", pop_many(data, 4))[0],
            relative_density=struct.unpack("<f", pop_many(data, 4))[0],
            h2=struct.unpack("<f", pop_many(data, 4))[0],
            h2s=struct.unpack("<f", pop_many(data, 4))[0],
            he=struct.unpack("<f", pop_many(data, 4))[0],
            h2o=struct.unpack("<f", pop_many(data, 4))[0],
            o2=struct.unpack("<f", pop_many(data, 4))[0],
            ar=struct.unpack("<f", pop_many(data, 4))[0],
            co=struct.unpack("<f", pop_many(data, 4))[0],
            c1h4=struct.unpack("<f", pop_many(data, 4))[0],
            c2h6=struct.unpack("<f", pop_many(data, 4))[0],
            c3h8=struct.unpack("<f", pop_many(data, 4))[0],
            ic4h10=struct.unpack("<f", pop_many(data, 4))[0],
            nc4h10=struct.unpack("<f", pop_many(data, 4))[0],
            ic5h12=struct.unpack("<f", pop_many(data, 4))[0],
            nc5h12=struct.unpack("<f", pop_many(data, 4))[0],
            c6h14=struct.unpack("<f", pop_many(data, 4))[0],
            c7h16=struct.unpack("<f", pop_many(data, 4))[0],
            c8h18=struct.unpack("<f", pop_many(data, 4))[0],
            c9h20=struct.unpack("<f", pop_many(data, 4))[0],
            c10h22=struct.unpack("<f", pop_many(data, 4))[0],
        )


class ParameterObjectType(IntEnum):

    SYSTEM_PARAMETER = 0


@attr.s(auto_attribs=True)
class SystemParameters:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.SYSTEM_PARAMETER

    device_type: DeviceType
    serial_number: int
    firmware_version: str  # TODO: Length 5
    service_version: int  # Used in how to parse the object.
    certification_variant: CertificationVariant
    station_id: str  # TODO: Lenght 17
    password_for_full_access_active: bool
    password_for_reading_is_on: bool
    metrological_switch: bool
    user_switch: bool
    switch_function: SwitchFunction
    parameter_crc: bytes  # to check if parameters have been changed from a previous read.
    measuring_period: int  # seconds
    archive_period: int  # seconds
    base_pressure: float
    base_temperature: float
    compressibility_formula: CompressibilityFormula
    gas_composition: GasComposition
    data_archive_record_length: int
    binary_archive_record_length: int
    daily_archive_record_length: int
    monthly_archive_record_length: int
    instantaneous_values_error_bit_order: int
    binary_archive_record_error_bit_order: int
    data_archive_record_error_bit_order: int
    optical_port_speed: bytes
    optical_port_protocol: int
    communication_port_0_speed: int
    communication_port_0_protocol: int
    communication_port_1_speed: int
    communication_port_1_protocol: int
    communication_port_2_speed: int
    communication_port_2_protocol: int
    communication_port_000_speed: int  # TODO: is this correct? Seems like double.
    gas_day_hour: int
    barometric_pressure_constant: float
    altitude: float
    status_archive_record_length: int
    pressure_unit_type: int  # TODO: how to interpret?
    pressure_unit_text: str
    temperature_unit_type: int  # TODO: how to interpret?
    temperature_unit_text: str
    altitude_unit_type: int
    altitude_unit_text: str
    gross_calorific_value_type: int
    gross_calorific_value_text: str
    dst_region: int
    gmt_hour_shift: int
    billing_archive_record_length: int
    conditions_for_combustion_heat: int
    device_variant: int
    bit_control: int
    places_for_corrected_volume_counters: int
    device_features: int
    version_metrological_part: str
    metrological_crc: int

    @classmethod
    def from_bytes(cls, in_bytes: bytes):

        # first 2 bytes is length and not included in parsing
        # third byte is object type and not included in parsing.
        data = bytearray(in_bytes)
        device_type = DeviceType(data.pop(0))
        serial_number = pop_many(data, 4)
        firmware_version = pop_many(data, 5).decode()
        service_version = data.pop(0)
        print(f"service version = {service_version}")
        certification_variant = CertificationVariant(data.pop(0))
        station_id = pop_many(data, 17).decode()
        access_of_data = data.pop(0)
        password_for_full_access_active = bool(access_of_data & 0b00000001)
        password_for_reading_is_on = bool(access_of_data & 0b00000010)
        metrological_switch = bool(access_of_data & 0b00000100)
        user_switch = bool(access_of_data & 0b00001000)
        switch_function = SwitchFunction(int((access_of_data & 0b00110000) >> 4))
        parameter_crc = pop_many(data, 2)
        measuring_period = data.pop(0)
        archive_period = int.from_bytes(pop_many(data, 2), "little")
        base_pressure = struct.unpack("<f", pop_many(data, 4))[0]
        base_temperature = struct.unpack("<f", pop_many(data, 4))[0]
        compressibility_formula = CompressibilityFormula(data.pop(0))
        gas_composition = GasComposition.from_bytes(pop_many(data, (23 * 4)))
        data_archive_record_length = int.from_bytes(pop_many(data, 2), "little")
        binary_archive_record_length = int.from_bytes(pop_many(data, 2), "little")
        daily_archive_record_length = int.from_bytes(pop_many(data, 2), "little")
        monthly_archive_record_length = int.from_bytes(pop_many(data, 2), "little")
        instantaneous_values_error_bit_order = int.from_bytes(
            pop_many(data, 2), "little"
        )
        binary_archive_record_error_bit_order = int.from_bytes(
            pop_many(data, 2), "little"
        )
        data_archive_record_error_bit_order = int.from_bytes(
            pop_many(data, 2), "little"
        )
        optical_port_speed = pop_many(data, 32)
        optical_port_protocol = int.from_bytes(pop_many(data, 4), "little")
        communication_port_0_speed = data.pop(0)
        communication_port_0_protocol = data.pop(0)
        communication_port_1_speed = data.pop(0)
        communication_port_1_protocol = data.pop(0)
        communication_port_2_speed = data.pop(0)
        communication_port_2_protocol = data.pop(0)
        communication_port_000_speed = int.from_bytes(
            pop_many(data, 2), "little"
        )  # TODO: is this correct? Seems like double.
        gas_day_hour = data.pop(0)
        barometric_pressure_constant = struct.unpack("<f", pop_many(data, 4))[0]
        altitude = struct.unpack("<f", pop_many(data, 4))[0]
        status_archive_record_length = int.from_bytes(pop_many(data, 2), "little")
        pressure_unit_type = data.pop(0)
        pressure_unit_text = pop_many(data, 8).decode("latin-1")
        temperature_unit_type = data.pop(0)
        temperature_unit_text = pop_many(data, 8).decode("latin-1")
        print(temperature_unit_text)
        altitude_unit_type = data.pop(0)
        altitude_unit_text = pop_many(data, 8).decode("latin-1")
        gross_calorific_value_type = data.pop(0)
        gross_calorific_value_text = pop_many(data, 8).decode("latin-1")
        dst_region = data.pop(0)
        gmt_hour_shift = data.pop(0)
        billing_archive_record_length = int.from_bytes(pop_many(data, 2), "little")
        conditions_for_combustion_heat = data.pop(0)
        device_variant = data.pop(0)
        data.pop(0)  # Removed unused byte
        bit_control = data.pop(0)
        places_for_corrected_volume_counters = data.pop(0)
        device_features = int.from_bytes(pop_many(data, 16), "little")
        version_metrological_part = pop_many(data, 5).decode()
        metrological_crc = int.from_bytes(pop_many(data, 2), "little")

        return cls(
            device_type=device_type,
            serial_number=serial_number,
            firmware_version=firmware_version,
            service_version=service_version,
            certification_variant=certification_variant,
            station_id=station_id,
            password_for_full_access_active=password_for_full_access_active,
            password_for_reading_is_on=password_for_reading_is_on,
            metrological_switch=metrological_switch,
            user_switch=user_switch,
            switch_function=switch_function,
            parameter_crc=parameter_crc,
            measuring_period=measuring_period,
            archive_period=archive_period,
            base_pressure=base_pressure,
            base_temperature=base_temperature,
            compressibility_formula=compressibility_formula,
            gas_composition=gas_composition,
            data_archive_record_length=data_archive_record_length,
            binary_archive_record_length=binary_archive_record_length,
            daily_archive_record_length=daily_archive_record_length,
            monthly_archive_record_length=monthly_archive_record_length,
            instantaneous_values_error_bit_order=instantaneous_values_error_bit_order,
            binary_archive_record_error_bit_order=binary_archive_record_error_bit_order,
            data_archive_record_error_bit_order=data_archive_record_error_bit_order,
            optical_port_speed=optical_port_speed,
            optical_port_protocol=optical_port_protocol,
            communication_port_0_speed=communication_port_0_speed,
            communication_port_0_protocol=communication_port_0_protocol,
            communication_port_1_speed=communication_port_1_speed,
            communication_port_1_protocol=communication_port_1_protocol,
            communication_port_2_speed=communication_port_2_speed,
            communication_port_2_protocol=communication_port_2_protocol,
            communication_port_000_speed=communication_port_000_speed,
            gas_day_hour=gas_day_hour,
            barometric_pressure_constant=barometric_pressure_constant,
            altitude=altitude,
            status_archive_record_length=status_archive_record_length,
            pressure_unit_type=pressure_unit_type,
            pressure_unit_text=pressure_unit_text,
            temperature_unit_type=temperature_unit_type,
            temperature_unit_text=temperature_unit_text,
            altitude_unit_type=altitude_unit_type,
            altitude_unit_text=altitude_unit_text,
            gross_calorific_value_type=gross_calorific_value_type,
            gross_calorific_value_text=gross_calorific_value_text,
            dst_region=dst_region,
            gmt_hour_shift=gmt_hour_shift,
            billing_archive_record_length=billing_archive_record_length,
            conditions_for_combustion_heat=conditions_for_combustion_heat,
            device_variant=device_variant,
            bit_control=bit_control,
            places_for_corrected_volume_counters=places_for_corrected_volume_counters,
            device_features=device_features,
            version_metrological_part=version_metrological_part,
            metrological_crc=metrological_crc,
        )
