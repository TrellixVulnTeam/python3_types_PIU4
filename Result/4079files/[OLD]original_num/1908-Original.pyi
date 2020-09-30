# (generated with --quick)

import tkinter
from typing import Any, Optional

tk: module

class CheckButtonWrapper(tkinter.Checkbutton):
    __doc__: str
    intval: tkinter.IntVar
    updated: bool
    def __init__(self, master, text) -> None: ...
    def _on_command(self) -> None: ...
    def get_value(self) -> Any: ...
    def set_value(self, value) -> None: ...
    def sync_value(self, value) -> Any: ...

class PanelIndicator(tkinter.Frame):
    canvas: tkinter.Canvas
    light: Any
    updated: bool
    value: Optional[int]
    def __init__(self, master, width = ..., height = ..., clickable = ...) -> None: ...
    def _on_mouse(self, event) -> None: ...
    def set_back(self) -> None: ...
    def set_disabled(self) -> None: ...
    def set_off(self) -> None: ...
    def set_on(self) -> None: ...
    def set_value(self, value) -> None: ...
    def sync_value(self, value) -> Any: ...

class Tooltip(object):
    id: None
    text: Any
    tipwindow: Optional[tkinter.Toplevel]
    widget: Any
    x: int
    y: int
    def __init__(self, widget) -> None: ...
    @staticmethod
    def create(widget, text) -> None: ...
    def hidetip(self) -> None: ...
    def showtip(self, text) -> None: ...

class ValueWidget(tkinter.Frame):
    box: Any
    canvas: tkinter.Canvas
    disabled: Any
    h: Any
    maxval: Any
    minval: Any
    round_to_step: Any
    step: Any
    text: Any
    updated: bool
    value: Any
    w: Any
    def __init__(self, master, width = ..., height = ..., clickable = ..., default = ..., minval = ..., maxval = ..., step = ..., round_to_step = ...) -> None: ...
    def _on_key(self, event) -> None: ...
    def _on_mouse(self, event) -> None: ...
    def get_value(self) -> Any: ...
    def set_disabled(self, disabled = ...) -> None: ...
    def set_range(self, minval, maxval, step) -> None: ...
    def set_value(self, value) -> None: ...
    def sync_value(self, value) -> Any: ...