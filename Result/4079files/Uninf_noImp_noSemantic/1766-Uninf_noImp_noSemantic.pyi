from collections import namedtuple
from typing import Any

TimeSignature = namedtuple('TimeSignature', ['top', 'bottom'])

TimeReport = namedtuple('TimeReport', ['delta', 'measure', 'signature', 'tick', 'bpm', 'prog', 'playing'])

def ticks_per_measure(signature: Any): ...
def seconds_per_tick(bpm: Any): ...

class Clock:
    parent: Any = ...
    _bpm: int = ...
    signature: Any = ...
    tick_count: int = ...
    measure_count: int = ...
    last_report_time: Any = ...
    last_tick_time: Any = ...
    prog: float = ...
    running: bool = ...
    absolute_time: float = ...
    last_prog: float = ...
    def __init__(self, parent: Any) -> None: ...
    def get_report(self): ...
    @property
    def bpm(self): ...
    @bpm.setter
    def bpm(self, value: Any) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def unpause(self) -> None: ...
    def tick(self) -> None: ...
    def _at_measure_start(self) -> None: ...
