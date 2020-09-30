# (generated with --quick)

from typing import Any

Button: Any
ButtonList: Any
Checkbox: Any
Dial: Any
Knob: Any
LED: Any
Label: Any
Meter: Any
RadioButtons: Any
Screen: Any
Slider: Any
asyncio: Any
font10: module
font14: Any
pi: float

class AssortedScreen(Any):
    led: Any
    def __init__(self) -> None: ...
    def callback(self, button, arg, label) -> None: ...
    def cbcb(self, checkbox, label, test) -> None: ...

class BackScreen(Any):
    hide_arg: str
    open_arg: str
    def __init__(self) -> None: ...
    def on_hide(self) -> None: ...
    def on_open(self) -> None: ...

class BaseScreen(Any):
    def __init__(self) -> None: ...

class KnobScreen(Any):
    def __init__(self) -> None: ...
    def callback(self, knob, control_name) -> None: ...
    def knob_moved(self, knob, dial, pointer, label, meter = ...) -> None: ...

class SliderScreen(Any):
    lstlbl: list
    slave1: Any
    slave2: Any
    def __init__(self) -> None: ...
    def callback(self, slider, device) -> None: ...
    def master_moved(self, slider, idx_label) -> None: ...
    def slave_moved(self, slider, idx_label) -> None: ...

class ThreadScreen(Any):
    dial1: Any
    dial2: Any
    pause: bool
    def __init__(self) -> None: ...
    def mainthread(self, dial, can_pause = ...) -> coroutine: ...
    def on_hide(self) -> None: ...
    def on_open(self) -> None: ...

def __getattr__(name) -> Any: ...
def backbutton(x, y) -> None: ...
def fwdbutton(x, y, cls_screen, text = ...) -> None: ...
def quitbutton(x, y) -> None: ...
def setup() -> None: ...
def test() -> None: ...
def to_string(val) -> str: ...