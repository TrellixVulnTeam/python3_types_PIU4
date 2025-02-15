# (generated with --quick)

from typing import Any, List

COSIM: Any
__all__: List[str]

class Receiver(object):
    __slots__ = ["callbacks"]
    callbacks: Any
    def AddCallback(self, cb) -> None: ...
    def Get(self, x) -> None: ...
    def __init__(self, callbacks = ...) -> None: ...

def FinishSim() -> None: ...
def Fork(c) -> None: ...
def MainLoop() -> None: ...
def RegisterCoroutines(coro) -> None: ...
def __getattr__(name) -> Any: ...
