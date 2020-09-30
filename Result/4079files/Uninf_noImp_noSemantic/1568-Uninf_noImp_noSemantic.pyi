import arcade
from typing import Any

app: App

class App:
    window: Any = ...
    game: Any = ...
    def __init__(self) -> None: ...
    def main(self) -> None: ...
    def get_screen_pos_args(self, pos: Any): ...

class MainWindow(arcade.Window):
    KeyRepeatDelayTime: float = ...
    KeyRepeatTime: float = ...
    KeyRepeatIgnoreKeys: Any = ...
    entity_pixel_size: int = ...
    key_downs: Any = ...
    def __init__(self) -> None: ...
    def on_draw(self) -> None: ...
    def update(self, delta_time: Any) -> None: ...
    def on_key_press(self, key: Any, modifiers: Any) -> None: ...
    def on_key_release(self, key: Any, modifiers: Any) -> None: ...
    def on_text(self, text: Any) -> None: ...
    def on_text_motion(self, motion: Any) -> None: ...
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) -> Any: ...
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> Any: ...

def main() -> None: ...