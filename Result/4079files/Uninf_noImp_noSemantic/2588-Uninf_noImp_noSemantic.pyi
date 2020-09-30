import unittest
from reobject.models import Model
from typing import Any

class Prototype(Model):
    value: str = ...
    def clone(self, **attrs: Any): ...

class TestPrototype(unittest.TestCase):
    prototype: Any = ...
    def setUp(self) -> None: ...
    def test_dispatcher(self) -> None: ...