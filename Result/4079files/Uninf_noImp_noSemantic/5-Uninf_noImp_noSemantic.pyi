import unittest
from typing import Any

class CompositeProgress:
    spans: Any = ...
    target: Any = ...
    def __init__(self, spans: Any, target: Any): ...
    def update(self) -> None: ...
    def set(self, current: Any, total: Any) -> None: ...

class CompositeProgressTest(unittest.TestCase):
    def test_composite_progress(self) -> None: ...

class ProgressSpan:
    max: Any = ...
    min: Any = ...
    name: Any = ...
    current: Any = ...
    on_change: Any = ...
    def __init__(self, max: int = ..., min: int = ..., name: str = ...) -> None: ...
    def update(self, current: Any) -> None: ...
    def __iadd__(self, other: Any): ...

class ProgressSpanTest(unittest.TestCase):
    updated: Any = ...
    def update(self, progress: Any) -> None: ...
    def check_updated(self, span: Any) -> None: ...
    def test_progress_update(self): ...
