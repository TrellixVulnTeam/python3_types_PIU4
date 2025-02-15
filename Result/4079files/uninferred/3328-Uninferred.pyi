from typing import Any

class Animation:
    icon_names: Any = ...
    timer: Any = ...
    current: int = ...
    icon: Any = ...
    rate: Any = ...
    def __init__(self, icon: Any, icons: Any, rate: int = ..., rev: bool = ...) -> None: ...
    def status(self): ...
    def get_rate(self): ...
    def set_rate(self, rate: Any) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def _animation(self): ...
