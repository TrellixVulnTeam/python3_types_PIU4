import tkinter as tk
from typing import Any

__title__: str
__author__: str
__version__: str

class ProjectWindow(tk.Toplevel):
    parent: Any = ...
    minecraft_location: Any = ...
    minecraft_versions: Any = ...
    minecraft_resource_packs: Any = ...
    minecraft_mods: Any = ...
    included_mods: str = ...
    pack_location: Any = ...
    widget_frame_body: Any = ...
    variable_string_title: Any = ...
    widget_entry_title: Any = ...
    variable_string_name: Any = ...
    widget_entry_name: Any = ...
    widget_directory_location: Any = ...
    widget_combobox_version: Any = ...
    widget_text_description: Any = ...
    widget_label_error: Any = ...
    widget_frame_buttons: Any = ...
    widget_button_cancel: Any = ...
    widget_button_create: Any = ...
    widget_button_detect_mods: Any = ...
    def __init__(self, parent: Any, *args: Any, **kwargs: Any): ...
    def find_minecraft_versions(self): ...
    def extract_minecraft_jar(self) -> None: ...
    def remove_previous_pack(self) -> None: ...

def main() -> None: ...
