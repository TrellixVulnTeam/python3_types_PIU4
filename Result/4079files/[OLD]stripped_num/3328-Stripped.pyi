# (generated with --quick)

from typing import Any

GLib: Any

class Animation:
    current: int
    icon: Any
    icon_names: list
    rate: Any
    timer: Any
    def __init__(self, icon, icons, rate = ..., rev = ...) -> None: ...
    def _animation(self) -> int: ...
    def get_rate(self) -> Any: ...
    def set_rate(self, rate) -> None: ...
    def start(self) -> None: ...
    def status(self) -> bool: ...
    def stop(self) -> None: ...