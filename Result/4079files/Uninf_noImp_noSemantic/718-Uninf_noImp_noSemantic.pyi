from overloading import *
from test_overloading import *
from typing import Any

class B:
    @classmethod
    def f(cls, *args: Any): ...
    def f(cls: Any, foo: Any, bar: int) -> Any: ...
    def f(cls, foo: Any, bar: Any): ...

class C:
    @classmethod
    def f(cls, *args: Any): ...
    @classmethod
    def f(cls: Any, foo: Any, bar: int) -> Any: ...
    @classmethod
    def f(cls, foo: Any, bar: Any): ...

class D:
    @classmethod
    def f(cls, *args: Any): ...
    @classmethod
    def f(cls: Any, foo: Any, bar: int) -> Any: ...
    @classmethod
    def f(cls, foo: Any, bar: Any): ...
