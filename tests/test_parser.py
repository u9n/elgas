import struct
from pprint import pprint

import attr
from attrs import asdict

from elgas import parser


def test_parser():
    data = b'\x0e\x01\x00\x83]!\xffs1.16\x00\x10\x02211137_000000001\x00\x0c\xe5\x99\x1e\x10\x0ef\xa6\xcaB\x00\x00\x00\x00\x02\xcd\xcc\x8c?\xb3\x0cA?5\xde.B\n\xd7#?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x18\xc4B\x8a\x1fC?\xd5\t\x88>\x84\x9eM=\xac\x8b[=\xc6\xdc5<\x00o\x01<\n\xd7#<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00X\x00\x0e\x00H\x004\x00\x98\x02X\x00\x00\x00\x03\x00\x00\x08\x00\x12\x03\x03\x00\x08\x03\x00\x06h\xa6\xcaB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00*\x00\x07bar\x00\x00\x00\x00\x00 \xb0C\x00\x00\x00\x00\x00\x00\xa1m\x00\x00\x00\x00\x00\x00\x00\x90MJ/m3\x003\x00\x01\x01\x00\x00\x00\x00\x00A\x005\xe0\xff\x7f\xffw\xee\x12\x00\x00\x00\x00\x00\x00\x00\x00\x001.16\x00\x9a\xfa\x00\x00\x00\x00\xe5!\x00\x00K\x00\x1e\x00\x00\x01\x00\x06\x00\n\x00\x9bPressure p\x00G\x00\x00\x00\x00\x00\x00+++\x00\x00bar\x00\x00\x00\x00\x00\x9a\x00\x9a:\x00\x00\x00\x00\xcd\xccL?\x00\x00\x8cBNy\x87d\x9e\x02Z\x00\x00\x00\n\x00\x00\x00\x00\x02K\x00\x1e\x01\x00\x02\x00\x08\x00\x0c\x00\x9bTemperature t\x00. Vbs\x00}?}\xb0C\x00\x00\x00\x00\x00\x00\x96\x00\x16;\x00\x00H\xc2\x00\x00\xc8\xc1\x00\x00pB\xadTad\xa2\x02\\\x00\x00\x00\x0c\x00\x00\x00\x00AK\x00\x1e\x02\x00\x15\x00\n\x00\x0e\x00\x89Internal temp. A3\x002\x00#\x00\x00\xb0C\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x00\x00\x00\xc3\x00\x00 \xc2\x00\x00\xaaB\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x1e\x03\x00\x16\x00\x0c\x00\x10\x00\x89Battery voltage A4\x00ax SV\x00\x00\x00\x00\x00\x00\x00h\xe8\x9f;\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90@\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x1e\x04\x00\x17\x00\x0e\x00\x12\x00\x81Battery capacity A5\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00\xc8\x00\xc8:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00aK\x00\x1e\x05\x00\x1a\x00\x10\x00\x14\x00\x81GSM signal A6\x00&\x00B\x00F\x00\x91Co%\x00\x00\x00\x00\x00\x00\x00\xc8\x00\xc8:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00BF\x00\x1f\x00\x00\xa0\x00\x90\x02\x00\x00P\x00\x81Cover B1\x00\x00\x00\x00\x00\x04B\x00;\x00\x00\'\x00J\x00\x9c\x02\x00\x00\x00\x00\x00      Closed\x00      Opened\x00K\x000\x01\x00\x1e\x00\x91\x02\x00\x00Q\x00QCall window B2\x00 B2\x002\x00\x95\x02\x01!\x00\xb8V\x00\x00\x00\x00\x00\x00\x04     no call\x00      active\x00K\x000\x02\x00\x1f\x00\x92\x02\x00\x00R\x00IService window B3\x00 B3\x003\x01A\x00\x00\x00\x00\x00\x08Q\x01\x00\x00  no service\x00      active\x00F\x00\x1f\x03\x00\x1c\x00\x93\x02\x00\x00S\x00\xc1Modem power supp B4\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00         Off\x00          On\x00F\x00\x1f\x04\x00\x1b\x00\x94\x02\x00\x00T\x00\xc1External power B5\x00 \x9c}"}\x9c\x02\x00\x00\x00\x00\x00    Power OK\x00 Power error\x00F\x00\x1f\x05\x001\x00\x95\x02\x00\x00U\x00\xc1Ext.power modem B6\x00o%} \x9c\x02\x00\x00\x00\x00\x00    Power OK\x00 Power error\x00Y\x005\x00\x00\x03\x00\x12\x00\x16\x00\x97Primary volume Vm\x00 } } m3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?} } \x9c\x02\x00\x00\x00\x00\x0e\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00?\x006\x00\x00\t\x00\x1a\x00\x1e\x00\x97Spare prim. vol. Vs\x00   m3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x16\x00\x12\x00\x00\x00\x00\x0b\x00\x00\x004\x00!\x00\x00\x07\x00"\x00&\x00\x97Base volume Vb\x00} \x95}"}!!m3\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x1a\x00\x00\x00\x023\x00.\x00\x00\x08\x00*\x00.\x00\x97Spare base vol. Vbs\x000}"m3\x00\x00\x00\x00\x00\x00\x00&\x00"\x00\x00\x00\x026\x00"\x00\x00\x04\x002\x006\x00\x8bFlow Q\x00  B3} 3}!A} } } m3/h\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00.\x00\x00\x00\x012\x00#\x00\x00\n\x006\x00:\x00\x83Base flow Qb\x00}?}#} }<} m3/h\x00\x00\x00\x00\x00\x002\x00\x00\x00\x01F\x00F\x00\x004\x00\x96\x02\x00\x00V\x00\xc1Setpoint Q max S1\x00} }  \x00<\x1cF"\x00\x00    Inactive\x00      Active\x007\x00$\x00\x00\x05\x00:\x00>\x00\x9bConvers.factor C\x00 A5\x00\x00\x00\x00\x01\x0f\x00\x00HC\x00\x00pA\x00\x00\x80?6\x00\x00\x00\x04)\x00/\x00\x00\x06\x00>\x00B\x00\x93Comp. ratio Z/Zb K\x00\x00\x81GS\x00:\x00\x00\x00\x04)\x00J\x00\x00&\x00B\x00F\x00\x91Compressibility Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04)\x00K\x00\x00%\x00F\x00J\x00\x91Base compress. Zb\x00ver B\x00\x00\x00\x00\x00\x04B\x00;\x00\x00\'\x00J\x00N\x00\xc7Status St1\x00Closed\x00     >\x00*\x00\xffo\xea\xec\xff\x0b\xff\xdf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00M\x01\x8d\x00\x12\x00\x00\x00\x00\x00\x00\x00\x05ATS0=1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ATD*99***1#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ATH\x00\x00\x00\x00\x00AT+CGDCONT=1,"IP","elvaco.tele2.m2m"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00y\x15Tg4\x81G\x99Bf\x11E\x00y\x15Tg4\x81G\x99Bf\x11E\x00y\x15Tg4\x81G\x00\x00\x00\x00\x00\x00+++\x00\x00\x00\x00\x00y\x15Tg4\x81G\x99B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    object_list = parser.ScadaParameterParser().parse(data)
    pprint(object_list)
    pretty_list = [asdict(x) for x in object_list]
    pprint(pretty_list)
    assert len(object_list) == 26
    # assert False


@attr.s(auto_attribs=True)
class ParseItem:

    name: str
    address: int
    length: int
    unit: str
    constant: float
    offset: float


def test_make_value_parsers():
    data = b'\x0e\x01\x00\x83]!\xffs1.16\x00\x10\x02211137_000000001\x00\x0c\xe5\x99\x1e\x10\x0ef\xa6\xcaB\x00\x00\x00\x00\x02\xcd\xcc\x8c?\xb3\x0cA?5\xde.B\n\xd7#?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x18\xc4B\x8a\x1fC?\xd5\t\x88>\x84\x9eM=\xac\x8b[=\xc6\xdc5<\x00o\x01<\n\xd7#<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00X\x00\x0e\x00H\x004\x00\x98\x02X\x00\x00\x00\x03\x00\x00\x08\x00\x12\x03\x03\x00\x08\x03\x00\x06h\xa6\xcaB\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00*\x00\x07bar\x00\x00\x00\x00\x00 \xb0C\x00\x00\x00\x00\x00\x00\xa1m\x00\x00\x00\x00\x00\x00\x00\x90MJ/m3\x003\x00\x01\x01\x00\x00\x00\x00\x00A\x005\xe0\xff\x7f\xffw\xee\x12\x00\x00\x00\x00\x00\x00\x00\x00\x001.16\x00\x9a\xfa\x00\x00\x00\x00\xe5!\x00\x00K\x00\x1e\x00\x00\x01\x00\x06\x00\n\x00\x9bPressure p\x00G\x00\x00\x00\x00\x00\x00+++\x00\x00bar\x00\x00\x00\x00\x00\x9a\x00\x9a:\x00\x00\x00\x00\xcd\xccL?\x00\x00\x8cBNy\x87d\x9e\x02Z\x00\x00\x00\n\x00\x00\x00\x00\x02K\x00\x1e\x01\x00\x02\x00\x08\x00\x0c\x00\x9bTemperature t\x00. Vbs\x00}?}\xb0C\x00\x00\x00\x00\x00\x00\x96\x00\x16;\x00\x00H\xc2\x00\x00\xc8\xc1\x00\x00pB\xadTad\xa2\x02\\\x00\x00\x00\x0c\x00\x00\x00\x00AK\x00\x1e\x02\x00\x15\x00\n\x00\x0e\x00\x89Internal temp. A3\x002\x00#\x00\x00\xb0C\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x00\x00\x00\xc3\x00\x00 \xc2\x00\x00\xaaB\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x1e\x03\x00\x16\x00\x0c\x00\x10\x00\x89Battery voltage A4\x00ax SV\x00\x00\x00\x00\x00\x00\x00h\xe8\x9f;\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90@\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00K\x00\x1e\x04\x00\x17\x00\x0e\x00\x12\x00\x81Battery capacity A5\x00\x00\x00\x00%\x00\x00\x00\x00\x00\x00\x00\xc8\x00\xc8:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00aK\x00\x1e\x05\x00\x1a\x00\x10\x00\x14\x00\x81GSM signal A6\x00&\x00B\x00F\x00\x91Co%\x00\x00\x00\x00\x00\x00\x00\xc8\x00\xc8:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8B\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00BF\x00\x1f\x00\x00\xa0\x00\x90\x02\x00\x00P\x00\x81Cover B1\x00\x00\x00\x00\x00\x04B\x00;\x00\x00\'\x00J\x00\x9c\x02\x00\x00\x00\x00\x00      Closed\x00      Opened\x00K\x000\x01\x00\x1e\x00\x91\x02\x00\x00Q\x00QCall window B2\x00 B2\x002\x00\x95\x02\x01!\x00\xb8V\x00\x00\x00\x00\x00\x00\x04     no call\x00      active\x00K\x000\x02\x00\x1f\x00\x92\x02\x00\x00R\x00IService window B3\x00 B3\x003\x01A\x00\x00\x00\x00\x00\x08Q\x01\x00\x00  no service\x00      active\x00F\x00\x1f\x03\x00\x1c\x00\x93\x02\x00\x00S\x00\xc1Modem power supp B4\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00\x00         Off\x00          On\x00F\x00\x1f\x04\x00\x1b\x00\x94\x02\x00\x00T\x00\xc1External power B5\x00 \x9c}"}\x9c\x02\x00\x00\x00\x00\x00    Power OK\x00 Power error\x00F\x00\x1f\x05\x001\x00\x95\x02\x00\x00U\x00\xc1Ext.power modem B6\x00o%} \x9c\x02\x00\x00\x00\x00\x00    Power OK\x00 Power error\x00Y\x005\x00\x00\x03\x00\x12\x00\x16\x00\x97Primary volume Vm\x00 } } m3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?} } \x9c\x02\x00\x00\x00\x00\x0e\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00\x00\x00?\x006\x00\x00\t\x00\x1a\x00\x1e\x00\x97Spare prim. vol. Vs\x00   m3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x16\x00\x12\x00\x00\x00\x00\x0b\x00\x00\x004\x00!\x00\x00\x07\x00"\x00&\x00\x97Base volume Vb\x00} \x95}"}!!m3\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x1a\x00\x00\x00\x023\x00.\x00\x00\x08\x00*\x00.\x00\x97Spare base vol. Vbs\x000}"m3\x00\x00\x00\x00\x00\x00\x00&\x00"\x00\x00\x00\x026\x00"\x00\x00\x04\x002\x006\x00\x8bFlow Q\x00  B3} 3}!A} } } m3/h\x00\x00\x00\x00\x9c\x02\x00\x00\x00\x00.\x00\x00\x00\x012\x00#\x00\x00\n\x006\x00:\x00\x83Base flow Qb\x00}?}#} }<} m3/h\x00\x00\x00\x00\x00\x002\x00\x00\x00\x01F\x00F\x00\x004\x00\x96\x02\x00\x00V\x00\xc1Setpoint Q max S1\x00} }  \x00<\x1cF"\x00\x00    Inactive\x00      Active\x007\x00$\x00\x00\x05\x00:\x00>\x00\x9bConvers.factor C\x00 A5\x00\x00\x00\x00\x01\x0f\x00\x00HC\x00\x00pA\x00\x00\x80?6\x00\x00\x00\x04)\x00/\x00\x00\x06\x00>\x00B\x00\x93Comp. ratio Z/Zb K\x00\x00\x81GS\x00:\x00\x00\x00\x04)\x00J\x00\x00&\x00B\x00F\x00\x91Compressibility Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04)\x00K\x00\x00%\x00F\x00J\x00\x91Base compress. Zb\x00ver B\x00\x00\x00\x00\x00\x04B\x00;\x00\x00\'\x00J\x00N\x00\xc7Status St1\x00Closed\x00     >\x00*\x00\xffo\xea\xec\xff\x0b\xff\xdf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00M\x01\x8d\x00\x12\x00\x00\x00\x00\x00\x00\x00\x05ATS0=1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ATD*99***1#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ATH\x00\x00\x00\x00\x00AT+CGDCONT=1,"IP","elvaco.tele2.m2m"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00y\x15Tg4\x81G\x99Bf\x11E\x00y\x15Tg4\x81G\x99Bf\x11E\x00y\x15Tg4\x81G\x00\x00\x00\x00\x00\x00+++\x00\x00\x00\x00\x00y\x15Tg4\x81G\x99B\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    object_list = parser.ScadaParameterParser().parse(data)
    object_list.pop(0)
    data_archive = dict()
    for item in object_list:
        try:
            address = getattr(item, "address_in_data_archive_record")
            name = getattr(item, "name")
            length = getattr(item, "value_length", None)
            constant = getattr(item, "value_constant", 1)
            offset = getattr(item, "offset", 0)
            unit = getattr(item, "unit", None)

            data_archive[address] = ParseItem(
                address=address,
                name=name,
                length=length,
                constant=constant,
                offset=offset,
                unit=unit,
            )
        except AttributeError:
            # Not in data archive
            continue

    pprint(data_archive)

    archive = b"`f\x97)\x00\x00F\x10\x02\"\xa6\x0e\x9b{\xc4\xf5(\\\xa7.\xff@0\x18\xe2z$!\xed@fpi\x9em\xa94A'\x8b\x88\xc1\x92\x8a\xea@\x00\x00\x00\x00\x00\x00\x00\x00}\x96\x81@\x8a\x17~?\x80\x00\x00 \x00\x00\x00\xd0\xcd\xb5"

    info = data_archive[38]

    data = archive[info.address : info.address + info.length]
    # number = int.from_bytes(data, 'little') * info.constant + info.offset
    number = struct.unpack("<d", data)[0]
    print(info)
    print(number)

    assert False
