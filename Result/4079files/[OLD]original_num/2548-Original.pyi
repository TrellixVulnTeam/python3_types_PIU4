# (generated with --quick)

import numpy
from typing import Any, Callable, Dict, Tuple

B: Any
E: Any
W: Any
camkifu: Any
commands_size: int
golib: Any
gsize: Any
np: module
os: module
queue: module
random: module
tmp_sgf: Any

class ControllerV(Any):
    __doc__: str
    api: Dict[str, Any]
    bounds: Any
    paused: Pause
    queue: queue.Queue[nothing]
    video: Any
    def __init__(self, user_input, display, sgffile = ..., video = ..., bounds = ...) -> None: ...
    def __setattr__(self, name, value) -> Any: ...
    def _add_bfinder(self, bf_class, callback) -> None: ...
    def _add_sfinder(self, sf_class, callback) -> None: ...
    def _cmd(self, event) -> None: ...
    def _cvappend(self, move) -> None: ...
    def _delete(self, x: int, y: int, learn: bool = ...) -> Any: ...
    def _drag(self, event) -> None: ...
    def _init_sgf(self, sgffile) -> Tuple[Any, bool]: ...
    def _mouse_release(self, event) -> None: ...
    def _off(self) -> None: ...
    def _on(self) -> None: ...
    def _onclose(self) -> None: ...
    def _openlive(*args, **kwargs) -> None: ...
    def _opensgf(self) -> Any: ...
    def _openvideo(*args, **kwargs) -> None: ...
    def _pause(self, boolean) -> None: ...
    def _run(self) -> None: ...
    def _save(self) -> None: ...
    def _select_bfinder(self, label) -> None: ...
    def _select_sfinder(self, label) -> None: ...
    def auto_save(self) -> None: ...
    def corrected(self, err_move, exp_move) -> None: ...
    def del_autosave(self) -> None: ...
    def get_stones(self) -> numpy.ndarray: ...
    def next(self) -> None: ...
    def pipe(self, instruction, *args) -> None: ...
    def quit(self) -> None: ...
    def random(self) -> None: ...
    def snapshot(self, save_goban) -> None: ...
    def vidpos(self, new_pos) -> None: ...

class Pause:
    __doc__: str
    paused: Any
    def __bool__(self) -> Any: ...
    def __init__(self, paused = ...) -> None: ...
    def false(self) -> bool: ...
    def true(self) -> bool: ...

def promptdiscard(meth) -> Callable: ...
