from datetime import datetime

import pytest

from elgas import utils


def test_lrc():
    #  02 FE 84 6C 0F 00 00 00 00 00 00 00 19 FD 19 0D
    input = "FE846C0F00000000000000"
    lrc = utils.calculate_lrc(bytearray(bytes.fromhex(input)))
    assert lrc == 0x19

    # data: 02 FE 86 6C 17 00 00 00 00 02 00 02 10 33 12 30 05 06 0C 2D 20 D4 9B 0D
    input = "FE866C17000000000200021033123005060C2D"
    lrc = utils.calculate_lrc(bytearray(bytes.fromhex(input)))
    assert lrc == 0x20


def test_checksum():
    # 02 FE 84 6C 0F 00 00 00 00 00 00 00 19 FD 19 0D
    input = "FE846C0F00000000000000"
    checksum = utils.calculate_checksum(bytearray(bytes.fromhex(input)))

    assert checksum == 0xFD

    # 02 FE 86 6C 17 00 00 00 00 02 00 02 10 33 12 30 05 06 0C 2D 20 D4 9B 0D
    input = "FE866C17000000000200021033123005060C2D"
    checksum = utils.calculate_checksum(bytearray(bytes.fromhex(input)))

    assert checksum == 0xD4


def test_drc():
    # 02 FE 84 6C 0F 00 00 00 00 00 00 00 19 FD 19 0D
    input = "FE846C0F00000000000000"
    drc = utils.calculate_drc(bytearray(bytes.fromhex(input)))
    assert drc == 0x19

    # data: 02 FE 86 6C 17 00 00 00 00 02 00 02 10 33 12 30 05 06 0C 2D 20 D4 9B 0D
    input = "FE866C17000000000200021033123005060C2D"
    drc = utils.calculate_drc(bytearray(bytes.fromhex(input)))

    assert drc == 0x9B


def test_return_characters():
    # Escaped 02 FE 84 64 19 00 00 00 00 00 00 00 EA 03 89 A3 3F 25 AB 41 77 69 2A 48 F8 0D
    input = "02FE84641900000000000000EA0389A33F25AB4177692A48F80D"
    output = utils.return_characters(bytes.fromhex(input))
    for_redundancy_data = output[1:-4]
    lrc = utils.calculate_lrc(bytearray(for_redundancy_data))
    checksum = utils.calculate_checksum(bytearray(for_redundancy_data))
    drc = utils.calculate_drc(bytearray(for_redundancy_data))
    assert lrc == output[-4]
    assert checksum == output[-3]
    assert drc == output[-2]

    # Escaped 02 FE 86 64 35 00 00 00 00 02 00 02 10 33 12 30 05 06 1B 0F 92 56 18 39 01 00 00 00 0000 00 00 00 00 00 00 00 A6 21 7E 08 A8 0B 6E 3F C1 01 00 0C 2D 47 E7 67 BB 0D

    input = (
        "02FE866435000000000200021033123005061B0F9256183901000000000000000000"
        "000000A6217E08A80B6E3FC101000C2D47E767BB0D"
    )
    output = utils.return_characters(bytes.fromhex(input))
    for_redundancy_data = output[1:-4]
    lrc = utils.calculate_lrc(bytearray(for_redundancy_data))
    checksum = utils.calculate_checksum(bytearray(for_redundancy_data))
    drc = utils.calculate_drc(bytearray(for_redundancy_data))
    assert lrc == output[-4]
    assert checksum == output[-3]
    assert drc == output[-2]


def test_escape_characters():
    input = b"\x02\xfe\x84d\x19\x00\x00\x00\x00\x00\x00\x00\xea\x03\x89\xa3?%\xabAwi*H\xf8\r"
    output = utils.escape_characters(input)
    assert output == bytes.fromhex(
        "02FE84641900000000000000EA0389A33F25AB4177692A48F80D"
    )

    input = b"\x02\xfe\x86d5\x00\x00\x00\x00\x02\x00\x02\x103\x120\x05\x06\x8d\x92V\x189\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6!~\x08\xa8\x0bn?\xc1\x01\x00\x0c-G\xe7g\xbb\r"
    output = utils.escape_characters(input)
    assert output == bytes.fromhex(
        "02FE866435000000000200021033123005061B0F9256183901000000000000000000"
        "000000A6217E08A80B6E3FC101000C2D47E767BB0D"
    )


def test_bytes_to_datetime():
    data = bytes.fromhex("103312300506")
    timestamp, is_dst, supports_dst = utils.bytes_to_datetime(data)

    assert timestamp.isoformat() == "2006-05-30T12:33:10"
    assert not is_dst
    assert not supports_dst


def test_bytes_to_datetime2():
    data = bytes.fromhex("004953140222")
    timestamp, is_dst, supports_dst = utils.bytes_to_datetime(data)

    assert timestamp.isoformat() == "2022-02-14T13:49:00"
    assert not is_dst
    assert supports_dst


def test_datetime_to_bytes():

    timestamp = datetime(2006, 5, 30, 12, 33, 10)
    data = utils.datetime_to_bytes(timestamp)
    assert data.hex() == "103312300506"


def test_pad_password():
    password = "123456"
    padded = utils.pad_password(password)
    assert len(padded) == 10


@pytest.mark.parametrize(("input", "output"), [(b"MJ/m3\x003\x00", "MJ/m3 3")])
def test_pretty_text(input: bytes, output: str):
    assert utils.pretty_text(input) == output


def test_return_characters_2():
    data = b"\x1b\x1b\x0e"
    out = utils.return_characters(data)
    assert out == b"\x1b\x0e"
