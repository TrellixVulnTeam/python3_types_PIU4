from gi.repository import GLib as GLib, Gtk as Gtk
from tag import Tag as Tag
from tags.registered_tags import get_class_from_tagtype as get_class_from_tagtype, get_required_functions_of_tag as get_required_functions_of_tag
from threading import Thread
from typing import Any, Optional

class ExecutorTimeout(Thread):
    TIMEOUT: int = ...
    callback: Any = ...
    c: Any = ...
    daemon: bool = ...
    kill: bool = ...
    waiter: Any = ...
    start_clock: bool = ...
    def __init__(self, callback: Any) -> None: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    def destroy(self) -> None: ...
    def run(self) -> None: ...

class Executor(Thread):
    daemon: bool = ...
    parent: Any = ...
    skip: Any = ...
    status_callback: Any = ...
    abort_flag: bool = ...
    current_melement: Any = ...
    l: Any = ...
    timeout: Any = ...
    def __init__(self, parent: Any, status_callback: Any, skip: Any, abort_callback: Optional[Any] = ...) -> None: ...
    def abort(self) -> None: ...
    def has_aborted(self): ...
    prev_export: Any = ...
    prev_video: Any = ...
    def prep_gui_for_test(self) -> None: ...
    def restore_gui_after_test(self) -> None: ...
    def timeout_set(self, m_element: Any) -> None: ...
    def timeout_clear(self) -> None: ...
    def get_frames(self, vision_enable: bool = ...): ...
    def execute(self) -> None: ...
    def run(self) -> None: ...
