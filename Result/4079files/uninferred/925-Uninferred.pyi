from typing import Any

class SegmentTree:
    N: Any = ...
    st: Any = ...
    lazy: Any = ...
    flag: Any = ...
    def __init__(self, N: Any) -> None: ...
    def left(self, idx: Any): ...
    def right(self, idx: Any): ...
    def build(self, idx: Any, l: Any, r: Any, A: Any) -> None: ...
    def update(self, idx: Any, l: Any, r: Any, a: Any, b: Any, val: Any): ...
    def query(self, idx: Any, l: Any, r: Any, a: Any, b: Any): ...
    def showData(self) -> None: ...
