from typing import ClassVar, Iterable, Optional

import attr

from elgas.parameters.enumerations import ParameterObjectType
from elgas.utils import pop_many, pretty_text


@attr.s(auto_attribs=True)
class TimeWindow:
    object_type: ClassVar[ParameterObjectType] = ParameterObjectType.TIME_WINDOW

    number: int
    id: int
    bit_order_in_actual_values: int
    bit_order_in_data_archive_record: int
    bit_order_in_binary_archive_record: int

    bit_control: int
    in_binary_archive: bool
    in_data_archive: bool
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
        in_binary_archive = bool(bit_control & 0b00000001)
        in_data_archive = bool(bit_control & 0b00000010)
        name = pretty_text(pop_many(data, 23))
        rows_in_window = data.pop(0)
        rows = list()
        for _ in range(0, rows_in_window):
            rows.append(pop_many(data, 10))
        if data:
            action_during_change = data.pop(0)
            text_log_0 = pretty_text(pop_many(data, 13))
            text_log_1 = pretty_text(pop_many(data, 13))
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
            in_binary_archive=in_binary_archive,
            in_data_archive=in_data_archive,
            name=name,
            rows_in_window=rows_in_window,
            rows=rows,
            action_during_change=action_during_change,
            text_log_0=text_log_0,
            text_log_1=text_log_1,
        )
