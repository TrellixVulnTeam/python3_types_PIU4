from demosys.context.base import BaseWindow
from typing import Any

class Window(BaseWindow):
    keys: Any = ...
    window_closing: bool = ...
    tmp_size_x: Any = ...
    tmp_size_y: Any = ...
    window: Any = ...
    context: Any = ...
    ctx: Any = ...
    fbo: Any = ...
    def __init__(self) -> None: ...
    def use(self) -> None: ...
    def swap_buffers(self) -> None: ...
    width: Any = ...
    height: Any = ...
    def resize(self, width: Any, height: Any) -> None: ...
    def process_events(self) -> None: ...
    def should_close(self): ...
    def close(self) -> None: ...
    def terminate(self) -> None: ...
    def get_library_version(self): ...
