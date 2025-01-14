from bot.shared import *
from bot.providers.provider import Provider
from typing import Any, Optional

class Nox(Provider):
    NotPath: Any = ...
    _debug: bool = ...
    predefined: Any = ...
    NoxPath: Any = ...
    def __init__(self, scheduler: Any, config: Any, run_time: Any) -> None: ...
    def swipe_time(self, x1: Any, y1: Any, x2: Any, y2: Any, time_amount: Any) -> None: ...
    def swipe_right(self, time_sleep: int = ...) -> None: ...
    def swipe(self, x1: Any, y1: Any, x2: Any, y2: Any) -> None: ...
    def take_png_screenshot(self): ...
    def tap(self, x: Any, y: Any) -> None: ...
    def key_escape(self) -> None: ...
    root: Any = ...
    @staticmethod
    def __str__(): ...
    def wait_for(self, word: Any, try_scanning: bool = ...) -> None: ...
    def __is_initial_screen__(self, *args: Any, **kwargs: Any): ...
    def __start_app__(self) -> None: ...
    def pass_through_initial_screen(self, already_started: bool = ...): ...
    def wait_for_notifications(self, *args: Any, **kwargs: Any): ...
    def scan_for_download(self, corr: Any = ..., info: Optional[Any] = ...): ...
    def scan_for_close(self, corr: Any = ..., info: Optional[Any] = ..., img: Optional[Any] = ...): ...
    def method_name(self) -> None: ...
    def start_process(self) -> None: ...
    def is_process_running(self): ...
    def compare_with_cancel_button(self, corr: Any = ..., info: Optional[Any] = ..., img: Optional[Any] = ...): ...
    def compare_with_back_button(self, corr: Any = ..., info: Optional[Any] = ..., img: Optional[Any] = ...): ...
    def click_auto_duel(self) -> None: ...
    def battle(self, info: Optional[Any] = ..., check_battle: bool = ...) -> None: ...
    def check_if_battle(self, img: Any): ...
    def determine_autoduel_status(self) -> None: ...
    def check_battle_is_running(self) -> None: ...
    def kill_process(self) -> None: ...
    def scan_for_ok(self, corr: Any = ..., info: Optional[Any] = ..., img: Optional[Any] = ...): ...
    current_battle: bool = ...
    def scan(self) -> None: ...
