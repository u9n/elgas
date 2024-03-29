import json
from pprint import pprint

from elgas.integration import (
    ConfigurationObject,
    ConfigurationObjectSchema,
    UtilitarianConfiguration,
    UtilitarianConfigurationObject,
    UtilitarianConfigurationObjectSchema,
    UtilitarianConfigurationSchema,
)
from elgas.parameters.analog_quantity import AnalogQuantity, AnalogQuantitySchema
from elgas.parameters.binary import Binary
from elgas.parameters.compressibility import (
    Compressibility,
    CompressibilityZ,
    CompressibilityZBase,
)
from elgas.parameters.conversion_coefficient import ConversionCoefficient
from elgas.parameters.counter import DoubleCounter
from elgas.parameters.diagnostics import Diagnostics
from elgas.parameters.error_counter import DoubleErrorCounter
from elgas.parameters.error_standard_counter import ErrorStandardCounter
from elgas.parameters.factory import ParameterSchemaFactory
from elgas.parameters.flow_rate import FlowRate, StandardFlowRate
from elgas.parameters.gas_composition import GasComposition
from elgas.parameters.modem import Modem
from elgas.parameters.setpoint import SetPoint
from elgas.parameters.standard_counter import StandardCounter
from elgas.parameters.system_parameters import SystemParameters
from elgas.parameters.time_window import TimeWindow


def test_analog_quantity_schema():
    data = {
        "address_in_actual_values": 16,
        "address_in_daily_archive_record": 0,
        "address_in_data_archive_record": 20,
        "address_in_monthly_archive_record": 0,
        "bit_control": 129,
        "decimals": 0,
        "digit": 0.0015259,
        "error_bit_order_in_actual_values": 668,
        "error_bit_order_in_binary_archive": 0,
        "error_bit_order_in_data_archive": 0,
        "id": 26,
        "in_daily_archive": False,
        "in_data_archive": True,
        "in_fast_archive_1": False,
        "in_fast_archvie_2": False,
        "in_monthly_archive": False,
        "is_metrological_quantity": False,
        "lower_limit_measuring_range": 0.0,
        "name": "GSM signal A6",
        "number": 5,
        "offset": 0.0,
        "samples_in_fast_archive": 0,
        "serial_number_transducer": 0,
        "unit": "%",
        "upper_limit_measuring_range": 100.0,
    }

    schema = AnalogQuantitySchema()

    obj = schema.load(data)

    assert obj.id == 26


def test_all():
    data = [
        SystemParameters(
            device_type=131,
            serial_number=1946100061,
            firmware_version="1.16",
            service_version=16,
            certification_variant=2,
            station_id="211137_000000001",
            password_for_full_access_active=False,
            password_for_reading_is_on=False,
            metrological_switch=True,
            user_switch=True,
            switch_function=0,
            parameter_crc=46378,
            measuring_period=30,
            archive_period=3600,
            base_pressure=101.32499694824219,
            base_temperature=0.0,
            compressibility_formula=2,
            gas_composition=GasComposition(
                co2=1.100000023841858,
                n2=0.7541000247001648,
                combustion_heat=43.71699905395508,
                relative_density=0.6399999856948853,
                h2=0.0,
                h2s=0.0,
                he=0.0,
                h2o=0.0,
                o2=0.0,
                ar=0.0,
                co=0.0,
                c1h4=98.0468978881836,
                c2h6=0.7621999979019165,
                c3h8=0.26570001244544983,
                ic4h10=0.050200000405311584,
                nc4h10=0.053599998354911804,
                ic5h12=0.011099999770522118,
                nc5h12=0.007899999618530273,
                c6h14=0.009999999776482582,
                c7h16=0.0,
                c8h18=0.0,
                c9h20=0.0,
                c10h22=0.0,
            ),
            data_archive_record_length=88,
            binary_archive_record_length=14,
            daily_archive_record_length=72,
            monthly_archive_record_length=52,
            instantaneous_values_error_bit_order=664,
            binary_archive_record_error_bit_order=88,
            data_archive_record_error_bit_order=0,
            optical_port_speed=8,
            optical_port_protocol=0,
            optical_port_bit_control=16,
            communication_port_0_speed=8,
            communication_port_0_protocol=0,
            communication_port_0_bit_control=18,
            communication_port_1_speed=3,
            communication_port_1_protocol=3,
            communication_port_1_bit_control=0,
            communication_port_2_speed=8,
            communication_port_2_protocol=3,
            communication_port_2_bit_control=0,
            gas_day_hour=6,
            fixed_barometric_pressure=101.32501220703125,
            altitude=0.0,
            status_archive_record_length=42,
            pressure_unit_type=7,
            pressure_unit_text="bar",
            temperature_unit_type=32,
            temperature_unit_text="°C",
            altitude_unit_type=161,
            altitude_unit_text="m",
            gross_calorific_value_type=144,
            gross_calorific_value_text="MJ/m3 3",
            dst_region=1,
            gmt_hour_shift=1,
            billing_archive_record_length=0,
            conditions_for_combustion_heat=0,
            device_variant=0,
            bit_control=65,
            places_for_corrected_volume_counters=0,
            device_features_bits=53,
            device_features="e0ff7fff77ee12000000000000000000",
            version_metrological_part="1.16",
            metrological_crc=64154,
            metrological_crc_32=0,
            application_crc_32=8677,
        ),
        AnalogQuantity(
            number=0,
            id=1,
            address_in_actual_values=6,
            address_in_data_archive_record=10,
            bit_control=155,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=False,
            is_metrological_quantity=True,
            in_fast_archive_1=False,
            in_fast_archvie_2=False,
            name="Pressure p",
            unit="bar",
            digit=0.0011749,
            offset=0.0,
            lower_limit_measuring_range=0.8,
            upper_limit_measuring_range=70.0,
            serial_number_transducer=1686600014,
            error_bit_order_in_actual_values=670,
            error_bit_order_in_binary_archive=90,
            error_bit_order_in_data_archive=0,
            address_in_daily_archive_record=10,
            address_in_monthly_archive_record=0,
            samples_in_fast_archive=0,
            decimals=0,
        ),
        AnalogQuantity(
            number=1,
            id=2,
            address_in_actual_values=8,
            address_in_data_archive_record=12,
            bit_control=155,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=False,
            is_metrological_quantity=True,
            in_fast_archive_1=False,
            in_fast_archvie_2=False,
            name="Temperature t",
            unit="°C",
            digit=0.0022889,
            offset=-50.0,
            lower_limit_measuring_range=-25.0,
            upper_limit_measuring_range=60.0,
            serial_number_transducer=1684100269,
            error_bit_order_in_actual_values=674,
            error_bit_order_in_binary_archive=92,
            error_bit_order_in_data_archive=0,
            address_in_daily_archive_record=12,
            address_in_monthly_archive_record=0,
            samples_in_fast_archive=0,
            decimals=0,
        ),
        AnalogQuantity(
            number=2,
            id=21,
            address_in_actual_values=10,
            address_in_data_archive_record=14,
            bit_control=137,
            in_data_archive=True,
            in_daily_archive=False,
            in_monthly_archive=False,
            is_metrological_quantity=False,
            in_fast_archive_1=False,
            in_fast_archvie_2=False,
            name="Internal temp. A3",
            unit="°C",
            digit=0.125,
            offset=-128.0,
            lower_limit_measuring_range=-40.0,
            upper_limit_measuring_range=85.0,
            serial_number_transducer=0,
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive=0,
            error_bit_order_in_data_archive=0,
            address_in_daily_archive_record=0,
            address_in_monthly_archive_record=0,
            samples_in_fast_archive=0,
            decimals=0,
        ),
        AnalogQuantity(
            number=3,
            id=22,
            address_in_actual_values=12,
            address_in_data_archive_record=16,
            bit_control=137,
            in_data_archive=True,
            in_daily_archive=False,
            in_monthly_archive=False,
            is_metrological_quantity=False,
            in_fast_archive_1=False,
            in_fast_archvie_2=False,
            name="Battery voltage A4",
            unit="V",
            digit=0.00488,
            offset=0.0,
            lower_limit_measuring_range=0.0,
            upper_limit_measuring_range=4.5,
            serial_number_transducer=0,
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive=0,
            error_bit_order_in_data_archive=0,
            address_in_daily_archive_record=0,
            address_in_monthly_archive_record=0,
            samples_in_fast_archive=0,
            decimals=0,
        ),
        AnalogQuantity(
            number=4,
            id=23,
            address_in_actual_values=14,
            address_in_data_archive_record=18,
            bit_control=129,
            in_data_archive=True,
            in_daily_archive=False,
            in_monthly_archive=False,
            is_metrological_quantity=False,
            in_fast_archive_1=False,
            in_fast_archvie_2=False,
            name="Battery capacity A5",
            unit="%",
            digit=0.0015259,
            offset=0.0,
            lower_limit_measuring_range=0.0,
            upper_limit_measuring_range=100.0,
            serial_number_transducer=0,
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive=0,
            error_bit_order_in_data_archive=0,
            address_in_daily_archive_record=0,
            address_in_monthly_archive_record=0,
            samples_in_fast_archive=0,
            decimals=0,
        ),
        AnalogQuantity(
            number=5,
            id=26,
            address_in_actual_values=16,
            address_in_data_archive_record=20,
            bit_control=129,
            in_data_archive=True,
            in_daily_archive=False,
            in_monthly_archive=False,
            is_metrological_quantity=False,
            in_fast_archive_1=False,
            in_fast_archvie_2=False,
            name="GSM signal A6",
            unit="%",
            digit=0.0015259,
            offset=0.0,
            lower_limit_measuring_range=0.0,
            upper_limit_measuring_range=100.0,
            serial_number_transducer=0,
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive=0,
            error_bit_order_in_data_archive=0,
            address_in_daily_archive_record=0,
            address_in_monthly_archive_record=0,
            samples_in_fast_archive=0,
            decimals=0,
        ),
        Binary(
            number=0,
            id=160,
            bit_order_in_actual_values=656,
            bit_order_in_data_archive_record=0,
            bit_order_in_binary_archive_record=80,
            bit_control=129,
            in_binary_archive=True,
            in_data_archive=False,
            active_indicator=False,
            name="Cover B1",
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive_record=0,
            error_bit_order_in_data_archive_record=0,
            action_during_change=0,
            text_log_0="Closed",
            text_log_1="Opened",
        ),
        TimeWindow(
            number=1,
            id=30,
            bit_order_in_actual_values=657,
            bit_order_in_data_archive_record=0,
            bit_order_in_binary_archive_record=81,
            bit_control=81,
            in_binary_archive=True,
            in_data_archive=False,
            name="Call window B2",
            rows_in_window=1,
            rows=["2100b856000000000000"],
            action_during_change=4,
            text_log_0="no call",
            text_log_1="active",
        ),
        TimeWindow(
            number=2,
            id=31,
            bit_order_in_actual_values=658,
            bit_order_in_data_archive_record=0,
            bit_order_in_binary_archive_record=82,
            bit_control=73,
            in_binary_archive=True,
            in_data_archive=False,
            name="Service window B3",
            rows_in_window=1,
            rows=["41000000000008510100"],
            action_during_change=0,
            text_log_0="no service",
            text_log_1="active",
        ),
        Binary(
            number=3,
            id=28,
            bit_order_in_actual_values=659,
            bit_order_in_data_archive_record=0,
            bit_order_in_binary_archive_record=83,
            bit_control=193,
            in_binary_archive=True,
            in_data_archive=False,
            active_indicator=True,
            name="Modem power supp B4",
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive_record=0,
            error_bit_order_in_data_archive_record=0,
            action_during_change=0,
            text_log_0="Off",
            text_log_1="On",
        ),
        Binary(
            number=4,
            id=27,
            bit_order_in_actual_values=660,
            bit_order_in_data_archive_record=0,
            bit_order_in_binary_archive_record=84,
            bit_control=193,
            in_binary_archive=True,
            in_data_archive=False,
            active_indicator=True,
            name="External power B5",
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive_record=0,
            error_bit_order_in_data_archive_record=0,
            action_during_change=0,
            text_log_0="Power OK",
            text_log_1="Power error",
        ),
        Binary(
            number=5,
            id=49,
            bit_order_in_actual_values=661,
            bit_order_in_data_archive_record=0,
            bit_order_in_binary_archive_record=85,
            bit_control=193,
            in_binary_archive=True,
            in_data_archive=False,
            active_indicator=True,
            name="Ext.power modem B6",
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive_record=0,
            error_bit_order_in_data_archive_record=0,
            action_during_change=0,
            text_log_0="Power OK",
            text_log_1="Power error",
        ),
        DoubleCounter(
            number=0,
            id=3,
            address_in_actual_values=18,
            address_in_data_archive_record=22,
            bit_control=151,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=True,
            in_factory_archive=False,
            is_metrological_quantity=True,
            accept_counting_direction=False,
            name="Primary volume Vm",
            unit="m3",
            digit=1.0,
            serial_number_of_gas_meter=1442135460,
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive=0,
            error_bit_order_in_data_archive=0,
            address_in_daily_archive_record=14,
            address_in_monthly_archive_record=10,
            address_in_billing_archive_record=0,
            serial_number_of_gas_meter_text="",
            decimals=0,
        ),
        DoubleErrorCounter(
            number=0,
            id=9,
            address_in_actual_values=26,
            address_in_data_archive_record=30,
            bit_control=151,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=True,
            in_factory_archive=False,
            is_metrological_quantity=True,
            name="Spare prim. vol. Vs",
            unit="m3",
            digit=1.0,
            number_of_primary_counter=0,
            address_in_daily_archive_record=22,
            address_in_monthly_archive_record=18,
            address_in_billing_archive_record=0,
            decimals=0,
        ),
        StandardCounter(
            number=0,
            id=7,
            address_in_actual_values=34,
            address_in_data_archive_record=38,
            bit_control=151,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=True,
            in_factory_archive=False,
            is_metrological_quantity=True,
            name="Base volume Vb",
            unit="m3",
            number_of_primary_counter=0,
            number_of_conversion=0,
            address_in_daily_archive_record=30,
            address_in_monthly_archive_record=26,
            address_in_billing_archive_record=0,
            decimals=2,
        ),
        ErrorStandardCounter(
            number=0,
            id=8,
            address_in_actual_values=42,
            address_in_data_archive_record=46,
            bit_control=151,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=True,
            in_factory_archive=False,
            is_metrological_quantity=True,
            name="Spare base vol. Vbs",
            unit="m3",
            number_of_standard_counter=0,
            address_in_daily_archive_record=38,
            address_in_monthly_archive_record=34,
            address_in_billing_archive_record=0,
            decimals=2,
        ),
        FlowRate(
            number=0,
            id=4,
            address_in_actual_values=50,
            address_in_data_archive_record=54,
            bit_control=139,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=False,
            is_metrological_quantity=False,
            name="Flow Q",
            unit="m3/h",
            error_bit_order_in_actual_values=668,
            error_bit_order_in_binary_archive=0,
            error_bit_order_in_data_archive=0,
            address_in_daily_archive_record=46,
            address_in_monthly_archive_record=0,
            decimals=1,
        ),
        StandardFlowRate(
            number=0,
            id=10,
            address_in_actual_values=54,
            address_in_data_archive_record=58,
            bit_control=131,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=False,
            is_metrological_quantity=False,
            name="Base flow Qb",
            unit="m3/h",
            number_of_primary_flow_rate=0,
            number_of_conversion=0,
            address_in_daily_archive_record=50,
            address_in_monthly_archive_record=0,
            decimals=1,
        ),
        SetPoint(
            number=0,
            id=52,
            bit_order_in_actual_values=662,
            bit_order_in_data_archive_record=0,
            bit_order_in_binary_archive_record=86,
            bit_control=193,
            in_binary_archive=True,
            in_data_archive=False,
            active_indicator=True,
            name="Setpoint Q max S1",
            value_of_limit=9999.0,
            type_of_primary_quantity=34,
            number_of_primary_quantity=0,
            action_during_change=0,
            text_log_0="Inactive",
            text_log_1="Active",
        ),
        ConversionCoefficient(
            number=0,
            id=5,
            address_in_actual_values=58,
            address_in_data_archive_record=62,
            bit_control=155,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=False,
            is_metrological_quantity=True,
            name="Convers.factor C",
            number_of_analog_pressure=0,
            number_of_analog_temperature=1,
            compressibility_calculation_method=15,
            default_value_pressure=200.0,
            default_value_temperature=15.0,
            alternate_value_of_compressibility=1.0,
            address_in_daily_archive_record=54,
            address_in_monthly_archive_record=0,
            decimals=4,
        ),
        Compressibility(
            number=0,
            id=6,
            address_in_actual_values=62,
            address_in_data_archive_record=66,
            bit_control=147,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=False,
            is_metrological_quantity=True,
            name="Comp. ratio Z/Zb K",
            number_of_conversion_coefficient=0,
            address_in_daily_archive_record=58,
            address_in_monthly_archive_record=0,
            decimals=4,
        ),
        CompressibilityZ(
            number=0,
            id=38,
            address_in_actual_values=66,
            address_in_data_archive_record=70,
            bit_control=145,
            in_data_archive=True,
            in_daily_archive=False,
            in_monthly_archive=False,
            is_metrological_quantity=True,
            name="Compressibility Z",
            number_of_conversion_coefficient=0,
            address_in_daily_archive_record=0,
            address_in_monthly_archive_record=0,
            decimals=4,
        ),
        CompressibilityZBase(
            number=0,
            id=37,
            address_in_actual_values=70,
            address_in_data_archive_record=74,
            bit_control=145,
            in_data_archive=True,
            in_daily_archive=False,
            in_monthly_archive=False,
            is_metrological_quantity=True,
            name="Base compress. Zb",
            number_of_conversion_coefficient=0,
            address_in_daily_archive_record=0,
            address_in_monthly_archive_record=0,
            decimals=4,
        ),
        Diagnostics(
            number=0,
            id=39,
            address_in_actual_values=74,
            address_in_data_archive_record=78,
            bit_control=199,
            in_data_archive=True,
            in_daily_archive=True,
            in_monthly_archive=True,
            in_factory_archive=False,
            name="Status St1",
            address_in_daily_archive_record=62,
            address_in_monthly_archive_record=42,
            mask_1_of_status_archive=3974787071,
            mask_2_of_status_archive=3758033919,
            mask_1_of_alarm=0,
            mask_2_of_alarm=0,
            mask_1_of_calling_to_dispatching=0,
            mask_2_of_calling_to_dispatching=0,
            action_during_change=0,
        ),
        Modem(
            number=0,
            bit_control_0=18,
            title="",
            modem_type=5,
            initialization="ATS0=1",
            call_to_dispatching="ATD*99***1#",
            modem_hang_up="ATH",
            special_initialization='AT+CGDCONT=1,"IP","elvaco.tele2.m2m"',
            ip_address_for_registration_and_diagnostics="127.0.0.1",
            ip_address_for_calling_to_dispatching="127.0.0.1",
            registration_send_period=0,
            authentication_mode=0,
            port_for_registration=0,
            port_for_calling_to_dispatching=0,
            sms_call="",
            gprs_user_name="",
            gprs_password="791554673481479942661145007915546734814799426611450079155467348147",
            ip_address_for_ping="127.0.0.1",
            ping_period=0,
            transition_into_command_mode="+++",
            pin="791554673481479942",
            owner_sim_number="",
        ),
    ]

    all_objects = []
    for param in data:
        param_type = param.object_type
        schema = ParameterSchemaFactory.by_parameter_id(param_type)
        out = schema().dump(param)
        all_objects.append(
            UtilitarianConfigurationObjectSchema().dump(
                UtilitarianConfigurationObject(
                    parameter_type=int(param.object_type), data=out
                )
            )
        )

    config = UtilitarianConfiguration(objects=all_objects)
    serialized = UtilitarianConfigurationSchema().dumps(config)
    print(serialized)

    json.loads(serialized)
