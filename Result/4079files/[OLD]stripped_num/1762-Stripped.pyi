# (generated with --quick)

import argparse
from typing import Any, Callable, NoReturn, Type, TypeVar, Union

ArgumentParser: Type[argparse.ArgumentParser]
DEFAULT_DB: Any
Edge: Any
QApplication: Any
QGridLayout: Any
QMainWindow: Any
QPainter: Any
QPen: Any
QRect: Any
QWidget: Any
Qt: Any
Renderer: Any
Ui_GoalBody: Any
load: Any
loadUi: Any
pyqtSignal: Any
save: Any
split_long: Any
sys: module

AnyStr = TypeVar('AnyStr', str, bytes)

class CentralWidget(Any):
    EDGE_PENS: dict
    dependencies: Any
    def __init__(self) -> None: ...
    def paintEvent(self, event) -> None: ...
    def setDependencies(self, new_dependencies) -> None: ...

class GoalWidget(Any, Any):
    _click_in_progress: bool
    clicked: Any
    is_real: bool
    widget_id: Any
    def __init__(self) -> None: ...
    def bottom_point(self) -> Any: ...
    def mousePressEvent(self, event) -> None: ...
    def mouseReleaseEvent(self, event) -> None: ...
    def setup_data(self, number, attributes) -> None: ...
    def top_point(self) -> Any: ...

class SiebenApp(Any):
    db: Any
    force_refresh: bool
    goals: Any
    quit_app: Any
    refresh: Any
    scrollAreaWidgetContents: CentralWidget
    def __init__(self, db, *args, **kwargs) -> None: ...
    def _current_goal_label(self) -> Any: ...
    def _update_title(self) -> None: ...
    def cancel_edit(self) -> None: ...
    def close_goal(self, goal_id) -> Callable[[], Any]: ...
    def finish_edit(self, fn) -> Callable[[], Any]: ...
    def keyPressEvent(self, event) -> None: ...
    def save_and_render(self) -> None: ...
    def select_number(self, num) -> Callable[[], Any]: ...
    def setup(self) -> None: ...
    def show_keys_help(self) -> None: ...
    def show_user_message(self, message) -> None: ...
    def start_edit(self, label, fn, pre_fn = ...) -> Callable[[], Any]: ...
    def toggle_view(self) -> None: ...
    def toggle_zoom(self) -> None: ...
    def with_refresh(self, fn, *args, **kwargs) -> Callable[[], Any]: ...

def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def main(root_script) -> NoReturn: ...
def realpath(filename: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...