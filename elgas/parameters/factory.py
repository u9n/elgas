from typing import ClassVar, Dict, Type

import attr

from elgas.parameters.analog_quantity import AnalogQuantity
from elgas.parameters.binary import Binary
from elgas.parameters.compressibility import (
    Compressibility,
    CompressibilityZ,
    CompressibilityZBase,
)
from elgas.parameters.conversion_coefficient import ConversionCoefficient
from elgas.parameters.counter import Counter, DoubleCounter
from elgas.parameters.device_error import DeviceError
from elgas.parameters.diagnostics import Diagnostics
from elgas.parameters.difference_counter import DifferenceBaseCounter, DifferenceCounter
from elgas.parameters.energy import Energy, ErrorEnergy
from elgas.parameters.enumerations import ParameterObjectType
from elgas.parameters.error_counter import DoubleErrorCounter, ErrorCounter
from elgas.parameters.error_standard_counter import ErrorStandardCounter
from elgas.parameters.flow_rate import FlowRate, StandardFlowRate
from elgas.parameters.modem import Modem
from elgas.parameters.setpoint import SetPoint
from elgas.parameters.standard_counter import StandardCounter
from elgas.parameters.statistics import (
    AnalogStatistics,
    AnalogTimeStatistics,
    CounterStatistics,
    StandardCounterStatistics,
    Statistics,
    TimeStatistics,
)
from elgas.parameters.sum_of_alarms import SumOfAlarms
from elgas.parameters.system_parameters import SystemParameters
from elgas.parameters.tariff_counter import (
    BaseTariffCounter,
    DoubleTariffCounter,
    TariffCounter,
)
from elgas.parameters.time_window import TimeWindow
from elgas.parameters.timer import Timer


@attr.s(auto_attribs=True)
class ParameterFactory:

    object_map: ClassVar[Dict[ParameterObjectType, Type]] = {
        ParameterObjectType.SYSTEM_PARAMETER: SystemParameters,
        ParameterObjectType.ANALOG_MEASURAND: AnalogQuantity,
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

    @staticmethod
    def from_json(object_type: ParameterObjectType, json_data: str):
        klass = ParameterFactory.object_map[object_type]
        return klass.from_json(json_data)
