import tkinter as tk
from tkinter import ttk
from typing import Any

__title__: str
__author__: str
__version__: str

class ModDetector(tk.Toplevel):
    parent: Any = ...
    minecraft_location: Any = ...
    minecraft_mods: Any = ...
    widget_frame_main: Any = ...
    widget_tree_left: Any = ...
    widget_frame_buttons: Any = ...
    widget_button_right_all: Any = ...
    widget_button_right: Any = ...
    widget_button_left: Any = ...
    widget_button_left_all: Any = ...
    widget_tree_right: Any = ...
    widget_frame_buttons_bottom: Any = ...
    widget_button_cancel: Any = ...
    widget_button_confirm: Any = ...
    def __init__(self, parent: Any, *args: Any, **kwargs: Any) -> None: ...
    def mod_search(self) -> None: ...
    def load_mcmodinfo(self, file: Any): ...
    def move_mod_right(self) -> None: ...
    def move_mod_left(self) -> None: ...
    def move_all_mods_right(self) -> None: ...
    def move_all_mods_left(self) -> None: ...
    def confirm_mods(self) -> None: ...
    def exit_mod(self) -> None: ...

class Tree(ttk.Frame):
    parent: Any = ...
    widget_tree: Any = ...
    scrollbar_horizontal: Any = ...
    scrollbar_vertical: Any = ...
    def __init__(self, parent: Any, **kwargs: Any) -> None: ...

def main() -> None: ...
