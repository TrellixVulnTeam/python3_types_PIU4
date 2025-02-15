# (generated with --quick)

import threading
from typing import Any, Iterable, List, Optional, Type

Timer: Type[threading.Timer]
asyncio: module
cozmo: Any
degrees: Any
distance_mm: Any
speed: int
speed_mmps: Any
time: module
words_to_numbers: List[str]

class VoiceCommands:
    lang_data: None
    log: Any
    robot: Any
    def __init__(self, robot, log = ...) -> None: ...
    def backward(self, robot = ..., cmd_args = ...) -> None: ...
    def blocks(self, robot = ..., cmd_args = ...) -> None: ...
    def charger(self, robot = ..., cmd_args = ...) -> None: ...
    def check_charger(self, robot, distance = ..., speed = ...) -> None: ...
    def dance(self, robot = ..., cmd_args = ...) -> None: ...
    def follow(self, robot = ..., cmd_args = ...) -> str: ...
    def forward(self, robot = ..., cmd_args = ..., invert = ...) -> str: ...
    def head(self, robot = ..., cmd_args = ...) -> str: ...
    def left(self, robot = ..., cmd_args = ..., invert = ...) -> str: ...
    def lift(self, robot = ..., cmd_args = ...) -> str: ...
    def look(self, robot = ..., cmd_args = ...) -> None: ...
    def picture(self, robot = ..., cmd_args = ...) -> str: ...
    def right(self, robot = ..., cmd_args = ..., invert = ...) -> None: ...
    def say(self, robot = ..., cmd_args = ...) -> Any: ...

def colored(text: str, color: Optional[str] = ..., on_color: Optional[str] = ..., attrs: Optional[Iterable[str]] = ...) -> str: ...
def cprint(text: str, color: Optional[str] = ..., on_color: Optional[str] = ..., attrs: Optional[Iterable[str]] = ..., **kwargs) -> None: ...
def extract_float(cmd_args, index = ...) -> Optional[float]: ...
def extract_next_float(cmd_args, index = ...) -> Optional[float]: ...
def turn_off_cube_lights(cubes) -> None: ...
