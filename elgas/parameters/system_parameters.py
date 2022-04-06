import struct
from typing import ClassVar

import attr

from elgas.parameters.enumerations import (
    CertificationVariant,
    CompressibilityFormula,
    DeviceType,
    ParameterObjectType,
    SwitchFunction,
)
from elgas.parameters.gas_composition import GasComposition
from elgas.utils import pop_many, pretty_text


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
    optical_port_speed: int
    optical_port_protocol: int
    optical_port_bit_control: int
    communication_port_0_speed: int
    communication_port_0_protocol: int
    communication_port_0_bit_control: int
    communication_port_1_speed: int
    communication_port_1_protocol: int
    communication_port_1_bit_control: int
    communication_port_2_speed: int
    communication_port_2_protocol: int
    communication_port_2_bit_control: int
    gas_day_hour: int
    fixed_barometric_pressure: float
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
    device_features_bits: int
    device_features: bytes
    version_metrological_part: str
    metrological_crc: int
    metrological_crc_32: int
    application_crc_32: int

    @classmethod
    def from_bytes(cls, in_bytes: bytes):

        # first 2 bytes is length and not included in parsing
        # third byte is object type and not included in parsing.
        data = bytearray(in_bytes)
        device_type = DeviceType(data.pop(0))
        serial_number = int.from_bytes(pop_many(data, 4), "little")
        firmware_version = pretty_text(pop_many(data, 5))
        service_version = data.pop(0)
        certification_variant = CertificationVariant(data.pop(0))
        station_id = pretty_text(pop_many(data, 17))
        data_access = data.pop(0)
        password_for_full_access_active = bool(data_access & 0b00000001)
        password_for_reading_is_on = bool(data_access & 0b00000010)
        metrological_switch = bool(data_access & 0b00000100)
        user_switch = bool(data_access & 0b00001000)
        switch_function = SwitchFunction(int((data_access & 0b00110000) >> 4))
        parameter_crc = pop_many(data, 2)
        measuring_period = data.pop(0)
        archiving_period = int.from_bytes(pop_many(data, 2), "little")
        base_pressure = struct.unpack("<f", pop_many(data, 4))[0]
        base_temperature = struct.unpack("<f", pop_many(data, 4))[0]
        compressibility_formula = CompressibilityFormula(data.pop(0))
        gas_composition = GasComposition.from_bytes(pop_many(data, (23 * 4)))
        # The record lengths are including the header with time.
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
        optical_port_speed = data.pop(0)
        optical_port_protocol = data.pop(0)
        optical_port_bit_control = data.pop(0)
        communication_port_0_speed = data.pop(0)
        communication_port_0_protocol = data.pop(0)
        communication_port_0_bit_control = data.pop(0)
        communication_port_1_speed = data.pop(0)
        communication_port_1_protocol = data.pop(0)
        communication_port_1_bit_control = data.pop(0)
        communication_port_2_speed = data.pop(0)
        communication_port_2_protocol = data.pop(0)
        communication_port_2_bit_control = data.pop(0)
        gas_hour = data.pop(0)
        fixed_barometric_pressure = struct.unpack("<f", pop_many(data, 4))[0]
        altitude = struct.unpack("<f", pop_many(data, 4))[0]
        _ = pop_many(data, 17)  # Not used
        status_archive_record_length = int.from_bytes(pop_many(data, 2), "little")
        pressure_unit_type = data.pop(0)
        pressure_unit_text = pretty_text(pop_many(data, 8))
        temperature_unit_type = data.pop(0)
        temperature_unit_text = pretty_text(pop_many(data, 8))
        altitude_unit_type = data.pop(0)
        altitude_unit_text = pretty_text(pop_many(data, 8))
        gross_calorific_value_type = data.pop(0)
        gross_calorific_value_text = pretty_text(pop_many(data, 8))
        dst_region = data.pop(0)  # seems like it should not be used.
        gmt_hour_shift = data.pop(0)
        billing_archive_record_length = int.from_bytes(pop_many(data, 2), "little")
        conditions_for_combustion_heat = data.pop(0)
        device_variant = data.pop(0)  # czech translation is device_value?
        _ = data.pop(0)  # not used
        bit_control = data.pop(0)
        corrected_volume_counters_amount = data.pop(0)
        device_features_bits = data.pop(0)
        device_features = pop_many(data, 16)
        version_metrological_part = pretty_text(pop_many(data, 5))
        metrological_crc = int.from_bytes(pop_many(data, 2), "little")
        metrological_crc_32 = int.from_bytes(pop_many(data, 4), "little")
        application_crc_32 = int.from_bytes(pop_many(data, 4), "little")

        assert not data

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
            archive_period=archiving_period,
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
            optical_port_bit_control=optical_port_bit_control,
            communication_port_0_speed=communication_port_0_speed,
            communication_port_0_protocol=communication_port_0_protocol,
            communication_port_0_bit_control=communication_port_0_bit_control,
            communication_port_1_speed=communication_port_1_speed,
            communication_port_1_protocol=communication_port_1_protocol,
            communication_port_1_bit_control=communication_port_1_bit_control,
            communication_port_2_speed=communication_port_2_speed,
            communication_port_2_protocol=communication_port_2_protocol,
            communication_port_2_bit_control=communication_port_2_bit_control,
            gas_day_hour=gas_hour,
            fixed_barometric_pressure=fixed_barometric_pressure,
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
            places_for_corrected_volume_counters=corrected_volume_counters_amount,
            device_features_bits=device_features_bits,
            device_features=device_features,
            version_metrological_part=version_metrological_part,
            metrological_crc=metrological_crc,
            metrological_crc_32=metrological_crc_32,
            application_crc_32=application_crc_32,
        )
