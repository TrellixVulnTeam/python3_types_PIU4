from typing import Any

e96: Any
e48: Any
e24: Any
e12: Any

def current_through_resistor(resistor: Any, voltage: Any) -> None: ...
def voltage_across_resistor(resistor: Any, current: Any) -> None: ...
def power_dissipated_in_resistor_by_current(resistor: Any, current: Any) -> None: ...
def power_dissipated_in_resistor_by_voltage(resistor: Any, voltage: Any) -> None: ...
def resistor_range(multiplicator: Any, sequence: Any = ...): ...
def standard_resistors(minExp: int = ..., maxExp: int = ..., sequence: Any = ...): ...
def nearest_resistor(value: Any, sequence: Any=...) -> None: ...
def parallel_resistors(*args: Any) -> None: ...
def serial_resistors(*args: Any) -> None: ...
def resistor_by_voltage_and_current(voltage: Any, current: Any) -> None: ...
