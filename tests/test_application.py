from elgas import application, frames
from elgas.constants import ServiceNumber
from elgas.frames import Response


def test_read_time_response():
    data = bytes.fromhex("02FE866C17000000000200021033123005060C2D20D49B0D")
    response = frames.Response.from_bytes(data)
    print(response)
    pdu = application.ReadTimeResponse.from_bytes(response.data)
    print(pdu)
    assert False


def test_parse_parameter_data_object_1():
    response = Response(
        service=ServiceNumber.READ_SCADA_PARAMETERS,
        destination_address_1=0,
        destination_address_2=0,
        source_address_1=1,
        source_address_2=0,
        data=bytearray(
            b'\x01\x00\r\x00\x00K\x00\x1e\x00\x00\x01\x00\x06\x00\n\x00\x9bPressure p\x00 } }(Q}!} } bar\x00\x00\x00\x00\x00\x9a\x00\x9a:\x00\x00\x00\x00\xcd\xccL?\x00\x00\x8cBNy\x87d\x9e\x02Z\x00\x00\x00\n\x00\x00\x00\x00}K\x00\x1e\x01\x00\x02\x00\x08\x00\x0c\x00\x9bTemperature t\x00pp B4} } \xb0C\x00\x00\x00\x00\x00\x00\x96\x00\x16;\x00\x00H\xc2\x00\x00\xc8\xc1\x00\x00pB\xadTad\xa2\x02\\\x00\x00\x00\x0c\x00\x00\x00\x00 K\x00\x1e\x02\x00\x15\x00\n\x00\x0e\x00\x89Internal temp. A3\x00\xc1Exte\xb0C\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x00\x00\x00\xc3\x00\x00 \xc2\x00\x00\xaaB\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00oK\x00\x1e\x03\x00\x16\x00\x0c\x00\x10\x00\x89Battery voltage A4\x001} \x95V\x00\x00\x00\x00\x00\x00\x00h\xe8\x9f;\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90@\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00}K\x00\x1e\x04\x00\x17\x00\x0e\x00\x12\x00\x81Battery capacity A5\x00r} %\x00\x00\x00\x00\x00\x00\x00\xc8\x00\xc8:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00 K\x00\x1e\x05\x00\x1a\x00\x10\x00\x14\x00\x81GSM signal A6\x00} } } } \xf0%\x00\x00\x00\x00\x00\x00\x00\xc8\x00\xc8:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00 F\x00\x1f\x00\x00\xa0\x00\x90\x02\x00\x00P\x00\x81Cover B1\x00 }+} } } \xeax\x94}-\x9c\x02\x00\x00\x00\x00\x00      Closed\x00      Opened\x00K\x000\x01\x00\x1e\x00\x91\x02\x00\x00Q\x00QCall window B2\x00\x00"} } S}\x01!\x00\xb8V\x00\x00\x00\x00\x00\x00\x04     no call\x00      active\x00K\x000\x02\x00\x1f\x00\x92\x02\x00\x00R\x00IService window B3\x00\x00:\xa5}-\x01A\x00\x00\x00\x00\x00\x08Q\x01\x00\x00  no service\x00      active\x00F\x00\x1f\x03\x00\x1c\x00\x93\x02\x00\x00S\x00\xc1Modem power supp B4\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00         Off\x00          On\x00F\x00\x1f\x04\x00\x1b\x00\x94\x02\x00\x00T\x00\xc1External power B5\x005\x00ose\x9c\x02\x00\x00\x00\x00\x00    Power OK\x00 Power error\x00F\x00\x1f\x05\x001\x00\x95\x02\x00\x00U\x00\xc1Ext.power modem B6\x006\x00 n\x9c\x02\x00\x00\x00\x00\x00    Power OK\x00 Power error\x00Y\x005\x00\x00\x03\x00\x12\x00\x16\x00\x97Primary volume Vm\x00m\x00Q\x01\x00m3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\xf0?  \x9c\x02\x00\x00\x00\x00\x0e\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00'
        ),
    )

    pdu = application.ReadDeviceParametersResponse.from_bytes(response.data)
    print(pdu)


def test_parse_parameter_data_object_0():

    response = Response(
        service=ServiceNumber.READ_SCADA_PARAMETERS,
        destination_address_1=0,
        destination_address_2=0,
        source_address_1=1,
        source_address_2=0,
        data=bytearray(
            b"\x00\x00\x0b\x00\x00\x0e\x01\x00\x83]!\xffs1.16\x00\x10\x02211137_000000001\x00\x0cF\x13\x1e\x10\x0ef\xa6\xcaB\x00\x00\x00\x00\x02\xcd\xcc\x8c?\xb3\x0cA?5\xde.B\n\xd7#?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x18\xc4B\x8a\x1fC?\xd5\t\x88>\x84\x9eM=\xac\x8b[=\xc6\xdc5<\x00o\x01<\n\xd7#<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00X\x00\x0e\x00H\x004\x00\x98\x02X\x00\x00\x00\x03\x00\x00\x08\x00\x02\x03\x03\x00\x08\x03\x00\x06h\xa6\xcaB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00*\x00\x07bar\x00\x00\x00\x00\x00 \xb0C\x00\x00\x00\x00\x00\x00\xa1m\x00\x00\x00\x00\x00\x00\x00\x90MJ/m3\x003\x00\x01\x01\x00\x00\x00\x00\x00A\x005\xe0\xff\x7f\xffw\xee\x12\x00\x00\x00\x00\x00\x00\x00\x00\x001.16\x00\x9a\xfa\x00\x00\x00\x00\xe5!\x00\x00K\x00\x1e\x00\x00\x01\x00\x06\x00\n\x00\x9bPressure p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00bar\x00\x00\x00\x00\x00\x9a\x00\x9a:\x00\x00\x00\x00\xcd\xccL?\x00\x00\x8cBNy\x87d\x9e\x02Z\x00\x00\x00\n\x00\x00\x00\x00\x00K\x00\x1e\x01\x00\x02\x00\x08\x00\x0c\x00\x9bTemperature t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0C\x00\x00\x00\x00\x00\x00\x96\x00\x16;\x00\x00H\xc2\x00\x00\xc8\xc1\x00\x00pB\xadTad\xa2\x02\\\x00\x00\x00\x0c\x00\x00\x00\x00\x00K\x00\x1e\x02\x00\x15\x00\n\x00\x0e\x00\x89Internal temp. A3\x00\x00\x00\x00\x00\x00\xb0C\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x00\x00\x00\xc3\x00\x00 \xc2\x00\x00\xaaB\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x1e\x03\x00\x16\x00\x0c\x00\x10\x00\x89Battery voltage A4\x00\x00\x00\x00\x00V\x00\x00\x00\x00\x00\x00\x00h\xe8\x9f;\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90@\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x1e\x04\x00\x17\x00\x0e\x00\x12\x00\x81Battery capacity A5\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00\xc8\x00\xc8:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x1e\x05\x00\x1a\x00\x10\x00\x14\x00\x81GSM signal A6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00\xc8\x00\xc8:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00F\x00\x1f\x00\x00\xa0\x00\x90\x02\x00\x00P\x00\x81Cover B1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00      Closed\x00      Opened\x00K\x000\x01\x00\x1e\x00\x91\x02\x00\x00Q\x00QCall window B2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01!\x00\xb8V\x00\x00\x00\x00\x00\x00\x04     no call\x00      active\x00K\x000\x02\x00\x1f\x00\x92\x02\x00\x00R\x00IService window B3\x00\x00\x00\x00\x00\x00\x01A\x00\x00\x00\x00\x00\x08Q\x01\x00\x00  no service\x00      active\x00F\x00\x1f\x03\x00\x1c\x00\x93\x02\x00\x00S\x00\xc1Modem power supp B4\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00         Off\x00          On\x00"
        ),
    )
    pdu = application.ReadDeviceParametersResponse.from_bytes(response.data)

    print(pdu)
    print(int.from_bytes(pdu.data[:2], "little"))
    print(len(pdu.data))
    print(pdu.data.hex())


def test_read_several_archive():
    response = Response(
        service=ServiceNumber.READ_ARCHIVES_BY_DATE,
        destination_address_1=0,
        destination_address_2=0,
        source_address_1=1,
        source_address_2=0,
        data=bytearray(
            b"\x03\x01\x00\x00\x00`f\x97)\x00\x00F\x10\x02\"\xa6\x0e\x9b{\xc4\xf5(\\\xa7.\xff@0\x18\xe2z$!\xed@fpi\x9em\xa94A'\x8b\x88\xc1\x92\x8a\xea@\x00\x00\x00\x00\x00\x00\x00\x00}\x96\x81@\x8a\x17~?\x80\x00\x00 \x00\x00\x00\xd0\xcd\xb5\xe0\xb7\x98)\x00\x00F\x11\x02\"\xaa\x0e\xc7|\xc4\xf5(\\\xa7.\xff@0\x18\xe2z$!\xed@fpi\x9em\xa94A'\x8b\x88\xc1\x92\x8a\xea@\x00\x00\x00\x00\x00\x00\x00\x00\x06c\x81@\xc4\x1d~?\x00\x00\x00 \x00\x00\x00\xd05\xbb`\t\x9a)\x00\x00F\x12\x02\"\xac\x0e\xca|\xc4\xf5(\\w0\xff@0\x18\xe2z$!\xed@f02~\xe2\xa94A'\x8b\x88\xc1\x92\x8a\xea@\xcd3\xcd?0\xc4\xce@\x14|\x81@\x90\x1b~?\x00\x00\x00 \x00\x00\x00\xd0\xab\xa5\xe0Z\x9b)\x00\x00F\x13\x02\"\xa8\x0ec{\xc4\xf5(\\w0\xff@0\x18\xe2z$!\xed@f02~\xe2\xa94A'\x8b\x88\xc1\x92\x8a\xea@\x00\x00\x00\x00\x00\x00\x00\x00\x84\xb7\x81@\xff\x17~?\x00\x00\x00 \x00\x00\x00\xd0\xdf;`\xac\x9c)\x00\x00F\x14\x02\"\xa5\x0efz\xc4\xf5(\\w0\xff@0\x18\xe2z$!\xed@f02~\xe2\xa94A'\x8b\x88\xc1\x92\x8a\xea@\x00\x00\x00\x00\x00\x00\x00\x00\x88\xd9\x81@\xc6\x12~?\x00\x00\x00 \x00\x00\x00\xd0\xb9\xb6"
        ),
    )

    assert response


def test_read_archive():
    response = Response(
        service=ServiceNumber.READ_ARCHIVES_BY_DATE,
        destination_address_1=0,
        destination_address_2=0,
        source_address_1=1,
        source_address_2=0,
        data=bytearray(
            b"\x03\x01\x00\x00\x00`f\x97)\x00\x00F\x10\x02\"\xa6\x0e\x9b{\xc4\xf5(\\\xa7.\xff@0\x18\xe2z$!\xed@fpi\x9em\xa94A'\x8b\x88\xc1\x92\x8a\xea@\x00\x00\x00\x00\x00\x00\x00\x00}\x96\x81@\x8a\x17~?\x80\x00\x00 \x00\x00\x00\xd0\xcd\xb5"
        ),
    )

    pdu = application.ReadArchiveByTimeResponse.from_bytes(response.data)
    print(pdu)
    assert response
    assert False
