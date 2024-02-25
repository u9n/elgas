from elgas.utils import return_characters
from elgas import application, constants, frames

data = (
    b"\x02"  # STX
    b"\xfe"  # ID
    b"\x84\x87"  # Call to dispatching, Type 0x84 grpup 0x87
    b"\x9c\x00"  # Length: 156 , total data is 159 correct?
    b"\x00\x00"  # Destination address
    b"\x00"  # Destination port
    b"\x01\x00"  # Source address
    b"\x00"  # Source port
    b"\x1b\x0f\x00"  # This is length of structure but correct is 141 and only 2. But 141 is forbidden ans is replaced with
    ## Correct unescaped: \x8d\x00 = 141
    b"\x02"  # structure version
    b"@\xa4\x94\xdd\x96\xce\x1b\x1b\xb7\x19Ad\xd5jo\x80\xa4"  # Guid. What is it for? Reveresed byte order?  Not same as docs.
    b"0000000000000001\x00"  # station ID
    b"#\x82\x08p\x10cCx\x00\x00"  # ID of SIM-card, Imsi, not iccid: '23820870106343780000'
    b"\x03Y\x07s g\x06Q"  # ID of modem, ''0359077320670651''
    b"\x00"  # Protocol 0 = ELGAS2
    b"\x01\x00"  # address1, ushort = 16 bit? little endian?
    b"\x00"  # address2 uchar = 8 bit?
    b"\x1f"  # gprs signal strength = 31
    b"\x06\x00\x00\x00"  # number of gprs connections, ulong = 6, little endian
    b"\x9e+b-"  # Time of last gprs connection
    b"\x00\x00\x00\x00"  # number of gprs errors
    b"\x00\x00\x00\x00"  # time of last gprs error
    b"\x01\x00\x00\x00"  # number of resets
    b"\x91\xca\xaf,"  # time of last reset
    b"\x98\x00\x00\x00"  # number of tcp data (packets or bytes?)
    b"\x00\x00\x00\x00"  # number of all data, what is this?
    ## version 2 data
    b",@\x8c\x8c"  # serial number of device? how to parse?
    b"\nGJK"  # ip address ?  10.71.74.75
    b"\x1d*b-"  # time of last module error
    b"\x01"  # last modem error
    b"z\xfe"  # modem battery capacity  How to parse?
    b"\xcd\x01"  # modem battery voltage, how to parse?
    # What is the rest?
    b"01.000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"  # Firmware
    b"}"  # LRC
    b"C"  # Checksum
    b"+"  # DRC
    b"\r"  # ETX
)


corrected_data = (
    b"\x02"
    b"\xfe"
    b"\x84"
    b"\x87"
    b"\x9c\x00"
    b"\x00\x00"
    b"\x00"
    b"\x01\x00"
    b"\x00"
    b"\x8d\x00"
    b"\x02"
    b"@\xa4\x94\xdd\x96\xce\x1b\xb7\x19Ad\xd5jo\x80\xa4"
    b"0000000000000001\x00"
    b"#\x82\x08p\x10cCx\x00\x00"
    b"\x03Y\x07s g\x06Q"
    b"\x00"
    b"\x01\x00"
    b"\x00"
    b"\x1f"
    b"\x06\x00\x00\x00"
    b"\x9e+b-"
    b"\x00\x00\x00\x00"
    b"\x00\x00\x00\x00"
    b"\x01\x00\x00\x00"
    b"\x91\xca\xaf,"
    b"\x98\x00\x00\x00"
    b"\x00\x00\x00\x00"
    b",@\x8c\x8c"  # 2358001708 just a number, little endian
    b"\nGJK"
    b"\x1d*b-"
    b"\x01"
    b"z\xfe"
    b"\xcd\x01"
    b"01.000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    b"}"
    b"C"
    b"+"
    b"\r"
)


def test_length_of_data():
    length = 0x9C

    assert len(return_characters(data)) - 1 == length


def test_parse_call_request():
    call_request = frames.Request.from_bytes(corrected_data)
    assert call_request.service == constants.ServiceNumber.CALL

    call = application.CallRequest.from_bytes(call_request.data)
    assert call.station_id == "0000000000000001"
    assert call.sim_card_id == "23820870106343780000"
    assert call.modem_id == "359077320670651"
    assert call.protocol == constants.Protocol.ELGAS2
    assert call.address_1 == 1
    assert call.address_2 == 0
    assert call.signal_strength == 31
    assert call.connections == 6
    assert call.last_connection_time.isoformat() == "2024-02-16T14:20:14"
    assert call.connection_errors == 0
    assert call.last_connection_error_time.isoformat() == "2000-01-01T00:00:00"
    assert call.resets == 1
    assert call.last_reset_time.isoformat() == "2023-10-04T07:02:41"
    assert call.tcp_data == 152
    assert call.all_data == 0
    assert call.serial_number == "2358001708"
    assert call.ip_address == "10.71.74.75"
    assert call.last_modem_error_time.isoformat() == "2024-02-16T14:13:49"
    assert call.last_modem_error == 1
    assert call.modem_battery_capacity == 65146
    assert call.modem_battery_voltage == 461
    assert call.firmware_version == "01.000"


def test_parse_call_apdu():
    application_data = corrected_data[12:-4]
    call = application.CallRequest.from_bytes(application_data)

    assert call.station_id == "0000000000000001"
    assert call.sim_card_id == "23820870106343780000"
    assert call.modem_id == "359077320670651"
    assert call.protocol == constants.Protocol.ELGAS2
    assert call.address_1 == 1
    assert call.address_2 == 0
    assert call.signal_strength == 31
    assert call.connections == 6
    assert call.last_connection_time.isoformat() == "2024-02-16T14:20:14"
    assert call.connection_errors == 0
    assert call.last_connection_error_time.isoformat() == "2000-01-01T00:00:00"
    assert call.resets == 1
    assert call.last_reset_time.isoformat() == "2023-10-04T07:02:41"
    assert call.tcp_data == 152
    assert call.all_data == 0
    assert call.serial_number == "2358001708"
    assert call.ip_address == "10.71.74.75"
    assert call.last_modem_error_time.isoformat() == "2024-02-16T14:13:49"
    assert call.last_modem_error == 1
    assert call.modem_battery_capacity == 65146
    assert call.modem_battery_voltage == 461
    assert call.firmware_version == "01.000"
