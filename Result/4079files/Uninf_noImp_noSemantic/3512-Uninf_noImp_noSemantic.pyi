from typing import Any

log: Any

class MultiTimer:
    _timing: Any = ...
    _overallstart: Any = ...
    _starttimes: Any = ...
    _totaldurations: Any = ...
    _count: Any = ...
    _stack: Any = ...
    def __init__(self, start: bool=...) -> None: ...
    def reset(self) -> None: ...
    def set_timing(self, timing: bool, reset: bool=...) -> None: ...
    def start(self, name: str, increment_count: bool=...) -> None: ...
    def stop(self, name: str) -> None: ...
    def report(self) -> None: ...

class MultiTimerContext:
    timer: Any = ...
    name: Any = ...
    def __init__(self, multitimer: MultiTimer, name: str) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...

timer: Any
