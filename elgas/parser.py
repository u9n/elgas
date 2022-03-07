from typing import *

import attr

from elgas import parameters
from elgas.utils import pop_many


@attr.s(auto_attribs=True)
class SimpleObjectHolder:
    """Just a class to hold data to verify in development."""

    length: int
    object_type: int
    data: bytes


@attr.s(auto_attribs=True)
class ScadaParameterParser:
    data: Optional[bytes] = attr.ib(default=None)

    def parse(self, data: Optional[bytes] = None):
        working_data = bytearray(self.data or data)

        if not working_data:
            raise ValueError("No data to parse")

        object_list = list()

        while working_data:
            length = int.from_bytes(pop_many(working_data, 2), "little")
            object_type = parameters.ParameterObjectType(working_data.pop(0))
            data = working_data[: length - 3]

            if object_type == parameters.ParameterObjectType.SYSTEM_PARAMETER:
                ## We cant parse this properly yet due to documentation error
                object_list.append(
                    SimpleObjectHolder(
                        length=length, object_type=object_type, data=data
                    )
                )

            else:

                object_list.append(
                    parameters.ParameterFactory.from_bytes(object_type, data)
                )

            working_data = working_data[length - 3 :]

        return object_list
