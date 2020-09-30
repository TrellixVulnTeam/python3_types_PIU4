from typing import Any, Tuple

class Display:
    _lcd: Any = ...
    _log: Any = ...
    _cur_index: int = ...
    _cur_side_index: int = ...
    def __init__(self, initializers: Tuple[str, str]=...) -> None: ...
    def clear(self) -> None: ...
    def get_on_screen(self) -> Tuple[str, str]: ...
    def _put(self, line1: str, line2: str) -> None: ...
    def show(self) -> None: ...
    def write(self, message: str) -> None: ...
    def scroll(self, displacement: int) -> None: ...
    def side_scroll(self, displacement: int) -> None: ...
    def set_default(self) -> None: ...
    def check_pressed(self) -> str: ...

class Input:
    def __enter__(self) -> Input: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    _window: Any = ...
    def start(self) -> None: ...
    def read(self) -> chr: ...
    def stop(self) -> None: ...