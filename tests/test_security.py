from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from elgas import application, frames, security, utils


def test_security_cbc():
    encryption_key = b"\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33"
    assert len(encryption_key) == 16
    iv = b"\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33\x33"
    assert len(iv) == 16
    data = bytearray(
        [
            0x6B,
            0x04,
            0xA5,
            0xB1,
            0xB3,
            0x70,
            0xA1,
            0xB0,
            0xEF,
            0x81,
            0x00,
            0x00,
            0x00,
            0x00,
            0xE0,
            0x03,
        ]
    )
    original_length = len(data).to_bytes(2, "little")
    assert original_length == b"\x10\x00"
    padded_data_with_header = bytearray(
        [
            0x10,
            0x00,
            0x03,
            0x6B,
            0x04,
            0xA5,
            0xB1,
            0xB3,
            0x70,
            0xA1,
            0xB0,
            0xEF,
            0x81,
            0x00,
            0x00,
            0x00,
            0x00,
            0xE0,
            0x03,
            0x1D,
            0xA5,
            0x49,
            0x89,
            0x40,
            0xBD,
            0xA3,
            0x09,
            0x64,
            0xD6,
            0x66,
            0x1F,
            0x64,
            0x68,
            0x46,
            0xA3,
        ]
    )
    padded_data = bytearray(
        [
            0x6B,
            0x04,
            0xA5,
            0xB1,
            0xB3,
            0x70,
            0xA1,
            0xB0,
            0xEF,
            0x81,
            0x00,
            0x00,
            0x00,
            0x00,
            0xE0,
            0x03,
            0x1D,
            0xA5,
            0x49,
            0x89,
            0x40,
            0xBD,
            0xA3,
            0x09,
            0x64,
            0xD6,
            0x66,
            0x1F,
            0x64,
            0x68,
            0x46,
            0xA3,
        ]
    )
    assert len(padded_data) % 16 == 0
    modbus_crc_corrcet = b"\x46\xa3"
    crc = utils.calculate_crc(padded_data_with_header[:-2]).to_bytes(2, "big")
    print(padded_data_with_header.hex())
    assert crc == modbus_crc_corrcet

    encryptor = Cipher(
        algorithms.AES(encryption_key), modes.CBC(initialization_vector=iv)
    ).encryptor()
    cipher_text = encryptor.update(padded_data) + encryptor.finalize()
    print(cipher_text.hex())
    cipher_result = bytearray(
        [
            0x8D,
            0x32,
            0x1E,
            0x0E,
            0x42,
            0x6D,
            0xF9,
            0xBF,
            0x8E,
            0x72,
            0x2B,
            0x5B,
            0xB9,
            0xAF,
            0xA6,
            0x2E,
            0x95,
            0x04,
            0xA9,
            0x2A,
            0x88,
            0x6B,
            0x1D,
            0x71,
            0xBB,
            0xFF,
            0x2F,
            0x57,
            0xF8,
            0x5B,
            0x8A,
            0x5B,
        ]
    )
    print(cipher_result.hex())
    assert len(cipher_text) == len(cipher_result)
    # assert cipher_text == cipher_result

    decryptor = Cipher(
        algorithms.AES(encryption_key), modes.CBC(initialization_vector=iv)
    ).decryptor()
    decrypted = decryptor.update(cipher_result) + decryptor.finalize()

    print("PADDED:")
    print(padded_data.hex())
    print(decrypted.hex())
    assert decrypted == padded_data
