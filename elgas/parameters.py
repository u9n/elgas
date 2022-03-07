import struct
from decimal import Decimal
from enum import IntEnum
from typing import *

import attr

from elgas.utils import pop_many


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
    ANALOG_MEASURAND = 30
    BINARY = 31
    COUNTER = 32
    STANDARD_COUNTER = 33
    FLOW_RATE = 34
    STANDARD_FLOW_RATE = 35
    CONVERSION_COEFFICIENT = 36
    ERROR_COUNTER = 45
    ERROR_STANDARD_COUNTER = 46
    COMPRESSIBILITY = 47
    TIME_WINDOW = 48
    CORRECTION_COUNTER = 49
    DOUBLE_COUNTER = 53
    DOUBLE_ERROR_COUNTER = 54
    DIAGNOSTICS = 59
    DEVICE_ERROR = 61
    SUM_OF_ALARMS = 62
    TIMER = 65

    TARIFF_COUNTER = 68
    BASE_TARIFF_COUNTER = 69
    SET_POINT = 70
    DIFFERENCE_COUNTER = 72
    DIFFERENCE_BASE_COUNTER = 73
    COMPRESSIBILITY_Z = 74
    COMPRESSIBILITY_Z_BASE = 75
    ENERGY = 77
    ERROR_ENERGY = 78
    DOUBLE_TARIFF_COUNTER = 79
    ANALOG_STATISTICS = 80
    COUNTER_STATISTICS = 81
    STANDARD_COUNTER_STATISTICS = 82
    STATISTICS = 83
    ANALOG_TIME_STATISTICS = 84
    TIME_STATISTICS = 85

    MODEM = 141


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


@attr.s(auto_attribs=True)
class AnalogMeasurand:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.ANALOG_MEASURAND
    value_length: ClassVar[int] = 2

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str
    unit: str
    digit: float
    offset: float
    lower_limit_measuring_range: float
    upper_limit_measuring_range: float
    serial_number_transducer: int
    error_bit_order_in_actual_values: int
    error_bit_order_in_binary_archive: int
    error_bit_order_in_data_archive: int
    address_in_daily_archive_record: int
    address_in_monthly_archive_record: int
    samples_in_fast_archive: int
    decimals: Optional[int]

    @property
    def value_constant(self):
        return self.digit

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        address_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        address_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_control = data.pop(0)
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
        digit = round(struct.unpack("<f", pop_many(data, 4))[0], 7)
        offset = struct.unpack("<f", pop_many(data, 4))[0]
        lower_limit_measuring_range = round(
            struct.unpack("<f", pop_many(data, 4))[0], 7
        )
        upper_limit_measuring_range = struct.unpack("<f", pop_many(data, 4))[0]
        serial_number_transducer = int.from_bytes(pop_many(data, 4), "little")
        error_bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        error_bit_order_in_binary_archive = int.from_bytes(pop_many(data, 2), "little")
        error_bit_order_in_data_archive = int.from_bytes(pop_many(data, 2), "little")
        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")
        samples_in_fast_archive = data.pop(0)

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
            name=name,
            unit=unit,
            digit=digit,
            offset=offset,
            lower_limit_measuring_range=lower_limit_measuring_range,
            upper_limit_measuring_range=upper_limit_measuring_range,
            serial_number_transducer=serial_number_transducer,
            error_bit_order_in_actual_values=error_bit_order_in_actual_values,
            error_bit_order_in_binary_archive=error_bit_order_in_binary_archive,
            error_bit_order_in_data_archive=error_bit_order_in_data_archive,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            samples_in_fast_archive=samples_in_fast_archive,
            decimals=decimals,
        )


@attr.s(auto_attribs=True)
class StandardCounter:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.STANDARD_COUNTER
    value_length: ClassVar[int] = 8

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str
    unit: str

    number_of_primary_counter: int
    number_of_conversion: int
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
        number_of_primary_counter = data.pop(0)
        number_of_conversion = data.pop(0)
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
            number_of_primary_counter=number_of_primary_counter,
            number_of_conversion=number_of_conversion,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            address_in_billing_archive_record=address_in_billing_archive_record,
            decimals=decimals,
        )


@attr.s(auto_attribs=True)
class Binary:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.BINARY

    number: int
    id: int
    bit_order_in_actual_values: int
    bit_order_in_data_archive_record: int
    bit_order_in_binary_archive_record: int

    bit_control: int  # seems to be which archives the values is in?
    name: str
    error_bit_order_in_actual_values: int
    error_bit_order_in_binary_archive_record: int  # TODO: Are these switch . Seems weird to have them in reverse order further down in the structure.
    error_bit_order_in_data_archive_record: int
    action_during_change: Optional[int]
    text_log_0: Optional[str]
    text_log_1: Optional[str]

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_binary_archive_record = int.from_bytes(pop_many(data, 2), "little")

        bit_control = data.pop(0)
        name = pop_many(data, 23).decode("latin-1")
        error_bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        error_bit_order_in_binary_archive_record = int.from_bytes(
            pop_many(data, 2), "little"
        )
        error_bit_order_in_data_archive_record = int.from_bytes(
            pop_many(data, 2), "little"
        )
        print(data)
        print(len(data))
        if data:
            action_during_change = data.pop(0)
            text_log_0 = pop_many(data, 13).decode("latin-1")  # DOCUMENTATION says 17!
            text_log_1 = pop_many(data, 13).decode("latin-1")
        else:
            action_during_change = None
            text_log_0 = None
            text_log_1 = None

        assert not data

        return cls(
            number=number,
            id=id,
            bit_order_in_actual_values=bit_order_in_actual_values,
            bit_order_in_data_archive_record=bit_order_in_data_archive_record,
            bit_order_in_binary_archive_record=bit_order_in_binary_archive_record,
            bit_control=bit_control,
            name=name,
            error_bit_order_in_actual_values=error_bit_order_in_actual_values,
            error_bit_order_in_binary_archive_record=error_bit_order_in_binary_archive_record,
            error_bit_order_in_data_archive_record=error_bit_order_in_data_archive_record,
            action_during_change=action_during_change,
            text_log_0=text_log_0,
            text_log_1=text_log_1,
        )


@attr.s(auto_attribs=True)
class FlowRate:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.FLOW_RATE
    value_length: ClassVar[int] = 4

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")

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
    bit_control: int  # seems to be which archives the values is in?
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")

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
            name=name,
            unit=unit,
            number_of_primary_flow_rate=number_of_primary_flow_rate,
            number_of_conversion=number_of_conversion,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            decimals=decimals,
        )


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
    bit_control: int  # seems to be which archives the values is in?
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
        name = pop_many(data, 23).decode("latin-1")
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


@attr.s(auto_attribs=True)
class ErrorStandardCounter:
    object_type: ClassVar[
        ParameterObjectType
    ] = ParameterObjectType.ERROR_STANDARD_COUNTER
    value_length: ClassVar[int] = 8

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str
    unit: str
    number_of_standard_counter: int
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
        number_of_standard_counter = data.pop(0)

        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_billing_archive_record = int.from_bytes(pop_many(data, 2), "little")

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
            name=name,
            unit=unit,
            number_of_standard_counter=number_of_standard_counter,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            address_in_billing_archive_record=address_in_billing_archive_record,
            decimals=decimals,
        )


@attr.s(auto_attribs=True)
class Compressibility:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.COMPRESSIBILITY
    value_length: ClassVar[int] = 4

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str
    number_of_conversion_coefficient: int
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
        name = pop_many(data, 23).decode("latin-1")
        number_of_conversion_coefficient = data.pop(0)

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
            name=name,
            number_of_conversion_coefficient=number_of_conversion_coefficient,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            decimals=decimals,
        )


class CompressibilityZ(Compressibility):
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.COMPRESSIBILITY_Z
    value_length: ClassVar[int] = 4


class CompressibilityZBase(Compressibility):
    object_type: ClassVar[
        ParameterObjectType
    ] = ParameterObjectType.COMPRESSIBILITY_Z_BASE
    value_length: ClassVar[int] = 4


@attr.s(auto_attribs=True)
class TimeWindow:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.TIME_WINDOW

    number: int
    id: int
    bit_order_in_actual_values: int
    bit_order_in_data_archive_record: int
    bit_order_in_binary_archive_record: int

    bit_control: int  # seems to be which archives the values is in?
    name: str
    rows_in_window: int
    rows: Iterable[bytes]
    action_during_change: Optional[int]
    text_log_0: Optional[str]
    text_log_1: Optional[str]

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_binary_archive_record = int.from_bytes(pop_many(data, 2), "little")

        bit_control = data.pop(0)
        name = pop_many(data, 23).decode("latin-1")
        rows_in_window = data.pop(0)
        rows = list()
        for _ in range(0, rows_in_window):
            rows.append(pop_many(data, 10))
        if data:
            action_during_change = data.pop(0)
            text_log_0 = pop_many(data, 13).decode("latin-1")  # DOCUMENTATION says 17!
            text_log_1 = pop_many(data, 13).decode("latin-1")
        else:
            action_during_change = None
            text_log_0 = None
            text_log_1 = None

        assert not data

        return cls(
            number=number,
            id=id,
            bit_order_in_actual_values=bit_order_in_actual_values,
            bit_order_in_data_archive_record=bit_order_in_data_archive_record,
            bit_order_in_binary_archive_record=bit_order_in_binary_archive_record,
            bit_control=bit_control,
            name=name,
            rows_in_window=rows_in_window,
            rows=rows,
            action_during_change=action_during_change,
            text_log_0=text_log_0,
            text_log_1=text_log_1,
        )


@attr.s(auto_attribs=True)
class Counter:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.COUNTER
    value_length: ClassVar[int] = 4

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
        digit = struct.unpack("<d", pop_many(data, 8))[0]
        serial_number_of_gas_meter = int.from_bytes(pop_many(data, 4), "little")

        error_bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        error_bit_order_in_binary_archive = int.from_bytes(pop_many(data, 2), "little")
        error_bit_order_in_data_archive = int.from_bytes(pop_many(data, 2), "little")
        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_billing_archive_record = int.from_bytes(pop_many(data, 2), "little")
        serial_number_of_gas_meter_text = pop_many(data, 17).decode("latin-1")

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


@attr.s(auto_attribs=True)
class ErrorCounter:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.ERROR_COUNTER
    value_length: ClassVar[int] = 4

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str
    unit: str
    digit: float
    number_of_primary_counter: int

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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
        digit = struct.unpack("<d", pop_many(data, 8))[0]
        number_of_primary_counter = data.pop(0)

        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_billing_archive_record = int.from_bytes(pop_many(data, 2), "little")

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
            name=name,
            unit=unit,
            digit=digit,
            number_of_primary_counter=number_of_primary_counter,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            address_in_billing_archive_record=address_in_billing_archive_record,
            decimals=decimals,
        )


class DoubleErrorCounter(ErrorCounter):
    object_type: ClassVar[
        ParameterObjectType
    ] = ParameterObjectType.DOUBLE_ERROR_COUNTER
    value_length: ClassVar[int] = 8


class CorrectionCounter(ErrorCounter):
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.CORRECTION_COUNTER
    value_length: ClassVar[int] = 4


@attr.s(auto_attribs=True)
class Diagnostics:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.DIAGNOSTICS

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str

    address_in_daily_archive_record: int
    address_in_monthly_archive_record: int
    mask_1_of_status_archive: int
    mask_2_of_status_archive: int
    mask_1_of_alarm: int
    mask_2_of_alarm: int
    mask_1_of_calling_to_dispatching: int
    mask_2_of_calling_to_dispatching: int
    action_during_change: int

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        address_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        address_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_control = data.pop(0)
        name = pop_many(data, 23).decode("latin-1")

        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")
        mask_1_of_status_archive = int.from_bytes(pop_many(data, 4), "little")
        mask_2_of_status_archive = int.from_bytes(pop_many(data, 4), "little")
        mask_1_of_alarm = int.from_bytes(pop_many(data, 4), "little")
        mask_2_of_alarm = int.from_bytes(pop_many(data, 4), "little")
        mask_1_of_calling_to_dispatching = int.from_bytes(pop_many(data, 4), "little")
        mask_2_of_calling_to_dispatching = int.from_bytes(pop_many(data, 4), "little")
        action_during_change = data.pop(0)

        return cls(
            number=number,
            id=id,
            address_in_actual_values=address_in_actual_values,
            address_in_data_archive_record=address_in_data_archive_record,
            bit_control=bit_control,
            name=name,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            mask_1_of_status_archive=mask_1_of_status_archive,
            mask_2_of_status_archive=mask_2_of_status_archive,
            mask_1_of_alarm=mask_1_of_alarm,
            mask_2_of_alarm=mask_2_of_alarm,
            mask_1_of_calling_to_dispatching=mask_1_of_calling_to_dispatching,
            mask_2_of_calling_to_dispatching=mask_2_of_calling_to_dispatching,
            action_during_change=action_during_change,
        )


@attr.s(auto_attribs=True)
class SetPoint:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.SET_POINT

    number: int
    id: int
    bit_order_in_actual_values: int
    bit_order_in_data_archive_record: int
    bit_order_in_binary_archive_record: int

    bit_control: int  # seems to be which archives the values is in?
    name: str
    value_of_limit: float
    type_of_primary_measurand: ParameterObjectType
    number_of_primary_measurand: int
    action_during_change: Optional[int]
    text_log_0: Optional[str]
    text_log_1: Optional[str]

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_binary_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_control = data.pop(0)
        name = pop_many(data, 23).decode("latin-1")
        value_of_limit = struct.unpack("<f", pop_many(data, 4))[0]
        type_of_primary_measurand = ParameterObjectType(data.pop(0))
        number_of_primary_measurand = data.pop(0)

        if data:
            action_during_change = data.pop(0)
            text_log_0 = pop_many(data, 13).decode("latin-1")  # DOCUMENTATION says 17!
            text_log_1 = pop_many(data, 13).decode("latin-1")
        else:
            action_during_change = None
            text_log_0 = None
            text_log_1 = None

        assert not data

        return cls(
            number=number,
            id=id,
            bit_order_in_actual_values=bit_order_in_actual_values,
            bit_order_in_data_archive_record=bit_order_in_data_archive_record,
            bit_order_in_binary_archive_record=bit_order_in_binary_archive_record,
            bit_control=bit_control,
            name=name,
            value_of_limit=value_of_limit,
            type_of_primary_measurand=type_of_primary_measurand,
            number_of_primary_measurand=number_of_primary_measurand,
            action_during_change=action_during_change,
            text_log_0=text_log_0,
            text_log_1=text_log_1,
        )


@attr.s(auto_attribs=True)
class Modem:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.MODEM

    number: int
    bit_control_0: int
    title: str
    modem_type: int
    initialization: str
    call_to_dispatching: str
    modem_hang_up: str
    special_initialization: str
    ip_address_for_registration_and_diagnostics: bytes
    ip_address_for_calling_to_dispatching: bytes
    registration_send_period: int
    authentication_mode: int
    port_for_registration: int
    port_for_calling_to_dispatching: int
    sms_call: str
    gprs_user_name: str
    gprs_password: str
    ip_address_for_ping: bytes
    ping_period: int
    transition_into_command_mode: str
    pin: str
    owner_sim_number: Optional[str]

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        bit_control_0 = data.pop(0)
        title = pop_many(data, 6).decode("latin-1")
        modem_type = data.pop(0)
        initialization = pop_many(data, 32).decode("latin-1")
        call_to_dispatching = pop_many(data, 32).decode("latin-1")
        modem_hang_up = pop_many(data, 8).decode("latin-1")
        special_initialization = pop_many(data, 80).decode("latin-1")
        ip_address_for_registration_and_diagnostics = pop_many(data, 4)
        ip_address_for_calling_to_dispatching = pop_many(data, 4)
        registration_send_period = data.pop(0)
        authentication_mode = data.pop(0)
        port_for_registration = int.from_bytes(pop_many(data, 2), "little")
        port_for_calling_to_dispatching = int.from_bytes(pop_many(data, 2), "little")
        sms_call = pop_many(data, 32).decode("latin-1")
        gprs_user_name = pop_many(data, 49).decode("latin-1")
        gprs_password = pop_many(data, 33).decode("latin-1")
        ip_address_for_ping = pop_many(data, 4)
        ping_period = int.from_bytes(pop_many(data, 2), "little")
        transition_into_command_mode = pop_many(data, 8).decode("latin-1")
        pin = pop_many(data, 9).decode("latin-1")
        print(len(data))
        owner_sim_number = pop_many(data, 17).decode("latin-1")

        assert not data  # Should be empty now

        return cls(
            number=number,
            bit_control_0=bit_control_0,
            title=title,
            modem_type=modem_type,
            initialization=initialization,
            call_to_dispatching=call_to_dispatching,
            modem_hang_up=modem_hang_up,
            special_initialization=special_initialization,
            ip_address_for_registration_and_diagnostics=ip_address_for_registration_and_diagnostics,
            ip_address_for_calling_to_dispatching=ip_address_for_calling_to_dispatching,
            registration_send_period=registration_send_period,
            authentication_mode=authentication_mode,
            port_for_registration=port_for_registration,
            port_for_calling_to_dispatching=port_for_calling_to_dispatching,
            sms_call=sms_call,
            gprs_user_name=gprs_user_name,
            gprs_password=gprs_password,
            ip_address_for_ping=ip_address_for_ping,
            ping_period=ping_period,
            transition_into_command_mode=transition_into_command_mode,
            pin=pin,
            owner_sim_number=owner_sim_number,
        )


@attr.s(auto_attribs=True)
class Energy:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.ENERGY

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str
    unit: str

    number_of_standard_counter: int
    number_of_calorific_value: int
    number_of_conversion: int
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
        number_of_standard_counter = data.pop(0)
        number_of_calorific_value = data.pop(0)
        number_of_conversion = data.pop(0)
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
            number_of_standard_counter=number_of_standard_counter,
            number_of_calorific_value=number_of_calorific_value,
            number_of_conversion=number_of_conversion,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            address_in_billing_archive_record=address_in_billing_archive_record,
            decimals=decimals,
        )


class ErrorEnergy:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.ERROR_ENERGY


@attr.s(auto_attribs=True)
class TariffCounter:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.TARIFF_COUNTER
    data_length: ClassVar[int] = 4

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
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


@attr.s(auto_attribs=True)
class DifferenceCounter:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.DIFFERENCE_COUNTER
    value_length: ClassVar[int] = 8

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str
    unit: str
    digit: float
    number_of_primary_counter: int
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
        digit = struct.unpack("<d", pop_many(data, 8))[0]
        number_of_primary_counter = data.pop(0)
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
            digit=digit,
            number_of_primary_counter=number_of_primary_counter,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            address_in_billing_archive_record=address_in_billing_archive_record,
            decimals=decimals,
        )


class DifferenceBaseCounter:
    object_type: ClassVar[
        ParameterObjectType
    ] = ParameterObjectType.DIFFERENCE_BASE_COUNTER
    value_length: ClassVar[int] = 8


@attr.s(auto_attribs=True)
class Timer:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.TIMER
    value_length: ClassVar[int] = 4

    number: int
    id: int
    address_in_actual_values: int
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str

    address_in_daily_archive_record: int
    address_in_monthly_archive_record: int

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        address_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        address_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_control = data.pop(0)
        name = pop_many(data, 23).decode("latin-1")

        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")

        assert not data

        return cls(
            number=number,
            id=id,
            address_in_actual_values=address_in_actual_values,
            address_in_data_archive_record=address_in_data_archive_record,
            bit_control=bit_control,
            name=name,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
        )


@attr.s(auto_attribs=True)
class DeviceError:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.DEVICE_ERROR

    number: int
    id: int
    bit_order_in_actual_values: int
    bit_order_in_data_archive_record: int
    bit_order_in_binary_archive_record: int

    bit_control: int  # seems to be which archives the values is in?
    name: str
    error_bit_order_in_actual_values: int
    error_bit_order_in_binary_archive_record: int  # TODO: Are these switch . Seems weird to have them in reverse order further down in the structure.
    error_bit_order_in_data_archive_record: int
    action_during_change: Optional[int]
    text_log_0: Optional[str]
    text_log_1: Optional[str]

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_binary_archive_record = int.from_bytes(pop_many(data, 2), "little")

        bit_control = data.pop(0)
        name = pop_many(data, 23).decode("latin-1")
        if data:
            action_during_change = data.pop(0)
            text_log_0 = pop_many(data, 13).decode("latin-1")  # DOCUMENTATION says 17!
            text_log_1 = pop_many(data, 13).decode("latin-1")
        else:
            action_during_change = None
            text_log_0 = None
            text_log_1 = None

        assert not data

        return cls(
            number=number,
            id=id,
            bit_order_in_actual_values=bit_order_in_actual_values,
            bit_order_in_data_archive_record=bit_order_in_data_archive_record,
            bit_order_in_binary_archive_record=bit_order_in_binary_archive_record,
            bit_control=bit_control,
            name=name,
            action_during_change=action_during_change,
            text_log_0=text_log_0,
            text_log_1=text_log_1,
        )


@attr.s(auto_attribs=True)
class SumOfAlarms:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.SUM_OF_ALARMS

    number: int
    id: int
    bit_order_in_actual_values: int
    bit_order_in_data_archive_record: int
    bit_order_in_binary_archive_record: int

    bit_control: int  # seems to be which archives the values is in?
    name: str
    error_bit_order_in_actual_values: int
    error_bit_order_in_binary_archive_record: int  # TODO: Are these switch . Seems weird to have them in reverse order further down in the structure.
    error_bit_order_in_data_archive_record: int
    action_during_change: Optional[int]
    text_log_0: Optional[str]
    text_log_1: Optional[str]

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_order_in_binary_archive_record = int.from_bytes(pop_many(data, 2), "little")

        bit_control = data.pop(0)
        name = pop_many(data, 23).decode("latin-1")
        if data:
            action_during_change = data.pop(0)
            text_log_0 = pop_many(data, 13).decode("latin-1")  # DOCUMENTATION says 17!
            text_log_1 = pop_many(data, 13).decode("latin-1")
        else:
            action_during_change = None
            text_log_0 = None
            text_log_1 = None

        assert not data

        return cls(
            number=number,
            id=id,
            bit_order_in_actual_values=bit_order_in_actual_values,
            bit_order_in_data_archive_record=bit_order_in_data_archive_record,
            bit_order_in_binary_archive_record=bit_order_in_binary_archive_record,
            bit_control=bit_control,
            name=name,
            action_during_change=action_during_change,
            text_log_0=text_log_0,
            text_log_1=text_log_1,
        )


@attr.s(auto_attribs=True)
class AnalogStatistics:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.ANALOG_STATISTICS

    number: int
    id: int
    address_in_actual_values: int  # Always 0
    address_in_data_archive_record: int
    bit_control: int  # seems to be which archives the values is in?
    name: str
    unit: str
    digit: float
    offset: float
    number_of_primary_measurand: int
    statistics_type: int  # 0 = min, 1 = max.
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
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
        digit = round(struct.unpack("<f", pop_many(data, 4))[0], 7)
        offset = struct.unpack("<f", pop_many(data, 4))[0]
        number_of_primary_measurand = data.pop(0)
        statistics_type = data.pop(0)
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
            name=name,
            unit=unit,
            digit=digit,
            offset=offset,
            number_of_primary_measurand=number_of_primary_measurand,
            statistics_type=statistics_type,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
            decimals=decimals,
        )


class Statistics(AnalogStatistics):
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.STATISTICS


class AnalogTimeStatistics(AnalogStatistics):
    object_type: ClassVar[
        ParameterObjectType
    ] = ParameterObjectType.ANALOG_TIME_STATISTICS


class TimeStatistics(AnalogStatistics):
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.TIME_STATISTICS


@attr.s(auto_attribs=True)
class CounterStatistics:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.COUNTER_STATISTICS

    number: int
    id: int
    address_in_actual_values: int  # Always 0
    address_in_data_archive_record: int  # Always 0
    bit_control: int  # seems to be which archives the values is in?
    name: str
    unit: str
    digit: float
    type_of_primary_measurand: int
    number_of_primary_measurand: int
    statistics_type: int  # 0 = min, 1 = max.
    address_in_daily_archive_record: int
    address_in_monthly_archive_record: int

    @classmethod
    def from_bytes(cls, in_data: bytes):
        data = bytearray(in_data)
        number = int.from_bytes(pop_many(data, 2), "little")
        id = int.from_bytes(pop_many(data, 2), "little")
        address_in_actual_values = int.from_bytes(pop_many(data, 2), "little")
        address_in_data_archive_record = int.from_bytes(pop_many(data, 2), "little")
        bit_control = data.pop(0)
        name = pop_many(data, 23).decode("latin-1")
        unit = pop_many(data, 8).decode("latin-1")
        digit = struct.unpack("<d", pop_many(data, 8))[0]
        type_of_primary_measurand = data.pop(0)
        number_of_primary_measurand = data.pop(0)
        statistics_type = data.pop(0)
        address_in_daily_archive_record = int.from_bytes(pop_many(data, 2), "little")
        address_in_monthly_archive_record = int.from_bytes(pop_many(data, 2), "little")

        assert not data

        return cls(
            number=number,
            id=id,
            address_in_actual_values=address_in_actual_values,
            address_in_data_archive_record=address_in_data_archive_record,
            bit_control=bit_control,
            name=name,
            unit=unit,
            digit=digit,
            type_of_primary_measurand=type_of_primary_measurand,
            number_of_primary_measurand=number_of_primary_measurand,
            statistics_type=statistics_type,
            address_in_daily_archive_record=address_in_daily_archive_record,
            address_in_monthly_archive_record=address_in_monthly_archive_record,
        )


class StandardCounterStatistics(CounterStatistics):
    object_type: ClassVar[
        ParameterObjectType
    ] = ParameterObjectType.STANDARD_COUNTER_STATISTICS


@attr.s(auto_attribs=True)
class ParameterFactory:

    object_map: ClassVar[Dict[ParameterObjectType, Type]] = {
        ParameterObjectType.SYSTEM_PARAMETER: SystemParameters,
        ParameterObjectType.ANALOG_MEASURAND: AnalogMeasurand,
        ParameterObjectType.BINARY: Binary,
        ParameterObjectType.COUNTER: Counter,
        ParameterObjectType.STANDARD_COUNTER: StandardCounter,
        ParameterObjectType.FLOW_RATE: FlowRate,
        ParameterObjectType.STANDARD_FLOW_RATE: StandardFlowRate,
        ParameterObjectType.CONVERSION_COEFFICIENT: ConversionCoefficient,
        ParameterObjectType.ERROR_COUNTER: ErrorCounter,
        ParameterObjectType.ERROR_STANDARD_COUNTER: ErrorStandardCounter,
        ParameterObjectType.COMPRESSIBILITY: Compressibility,
        ParameterObjectType.TIME_WINDOW: TimeWindow,
        ParameterObjectType.DOUBLE_COUNTER: DoubleCounter,
        ParameterObjectType.DOUBLE_ERROR_COUNTER: DoubleErrorCounter,
        ParameterObjectType.DIAGNOSTICS: Diagnostics,
        ParameterObjectType.SET_POINT: SetPoint,
        ParameterObjectType.COMPRESSIBILITY_Z: CompressibilityZ,
        ParameterObjectType.COMPRESSIBILITY_Z_BASE: CompressibilityZBase,
        ParameterObjectType.ENERGY: Energy,
        ParameterObjectType.ERROR_ENERGY: ErrorEnergy,
        ParameterObjectType.TARIFF_COUNTER: TariffCounter,
        ParameterObjectType.DOUBLE_TARIFF_COUNTER: DoubleTariffCounter,
        ParameterObjectType.BASE_TARIFF_COUNTER: BaseTariffCounter,
        ParameterObjectType.DIFFERENCE_COUNTER: DifferenceCounter,
        ParameterObjectType.DIFFERENCE_BASE_COUNTER: DifferenceBaseCounter,
        ParameterObjectType.TIMER: Timer,
        ParameterObjectType.DEVICE_ERROR: DeviceError,
        ParameterObjectType.SUM_OF_ALARMS: SumOfAlarms,
        ParameterObjectType.ANALOG_STATISTICS: AnalogStatistics,
        ParameterObjectType.STATISTICS: Statistics,
        ParameterObjectType.ANALOG_TIME_STATISTICS: AnalogTimeStatistics,
        ParameterObjectType.TIME_STATISTICS: TimeStatistics,
        ParameterObjectType.COUNTER_STATISTICS: CounterStatistics,
        ParameterObjectType.STANDARD_COUNTER_STATISTICS: StandardCounterStatistics,
        ParameterObjectType.MODEM: Modem,
    }

    @staticmethod
    def from_bytes(object_type: ParameterObjectType, in_data: bytes):
        klass = ParameterFactory.object_map[object_type]
        return klass.from_bytes(in_data)
