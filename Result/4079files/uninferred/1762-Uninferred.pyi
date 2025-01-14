from PyQt5.QtWidgets import QMainWindow, QWidget
from siebenapp.ui.goalwidget import Ui_GoalBody
from typing import Any, Optional

class GoalWidget(QWidget, Ui_GoalBody):
    clicked: Any = ...
    _click_in_progress: bool = ...
    is_real: bool = ...
    widget_id: Any = ...
    def __init__(self) -> None: ...
    def setup_data(self, number: Any, attributes: Any) -> None: ...
    def mousePressEvent(self, event: Any) -> None: ...
    def mouseReleaseEvent(self, event: Any) -> None: ...
    def top_point(self): ...
    def bottom_point(self): ...

class CentralWidget(QWidget):
    EDGE_PENS: Any = ...
    dependencies: Any = ...
    def __init__(self) -> None: ...
    def setDependencies(self, new_dependencies: Any) -> None: ...
    def paintEvent(self, event: Any) -> None: ...

class SiebenApp(QMainWindow):
    refresh: Any = ...
    quit_app: Any = ...
    db: Any = ...
    goals: Any = ...
    force_refresh: bool = ...
    def __init__(self, db: Any, *args: Any, **kwargs: Any) -> None: ...
    scrollAreaWidgetContents: Any = ...
    def setup(self) -> None: ...
    def _update_title(self) -> None: ...
    def close_goal(self, goal_id: Any): ...
    def save_and_render(self) -> None: ...
    def keyPressEvent(self, event: Any) -> None: ...
    def start_edit(self, label: Any, fn: Any, pre_fn: Optional[Any] = ...): ...
    def finish_edit(self, fn: Any): ...
    def cancel_edit(self) -> None: ...
    def _current_goal_label(self): ...
    def with_refresh(self, fn: Any, *args: Any, **kwargs: Any): ...
    def select_number(self, num: Any): ...
    def toggle_view(self) -> None: ...
    def toggle_zoom(self) -> None: ...
    def show_keys_help(self) -> None: ...
    def show_user_message(self, message: Any) -> None: ...

def main(root_script: Any) -> None: ...
