from elgas.parameters.analog_quantity import AnalogQuantitySchema


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
