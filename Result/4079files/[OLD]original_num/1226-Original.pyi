# (generated with --quick)

import tkinter
from typing import Any, List, Optional, Tuple, Type

Canvas: Type[tkinter.Canvas]
Cell: Any
Com: Any
Corner: Any
Dim: Any
Floor: Any
Orientation: Any
Wall: Any

class Level:
    cells: Any
    cells_across: Any
    cells_up: Any
    corners: Any
    ew_walls: Any
    floors: Any
    level: Any
    ns_walls: Any
    tk_level: Optional[tkinter.Canvas]
    def __init__(self, cells_across, cells_up, cell_size, level) -> None: ...
    def _ew_wall(self, across, up) -> Any: ...
    def _ns_wall(self, across, up) -> Any: ...
    def cell(self, across, up) -> Any: ...
    def erode(self) -> None: ...
    def set_floor(self, maze) -> None: ...
    def string(self) -> str: ...
    def tk_paint(self) -> None: ...

class Maze:
    __doc__: str
    bods: list
    cells_across: Any
    cells_up: Any
    depth: Any
    levels: List[Level]
    mined: bool
    start: Tuple[int, int, int]
    things: list
    tk_maze: Any
    def __init__(self, cells_across, cells_up, depth, cell_size) -> None: ...
    def add_bod(self, bod, show) -> None: ...
    def add_thing(self, cell, thing) -> None: ...
    def animation(self) -> None: ...
    def at(self, index) -> Any: ...
    def cell(self, cells_across, cells_up, level = ...) -> Any: ...
    def do_mined(self) -> None: ...
    def string(self) -> str: ...
    def tk_init(self, root) -> None: ...
    def tk_paint(self) -> None: ...
