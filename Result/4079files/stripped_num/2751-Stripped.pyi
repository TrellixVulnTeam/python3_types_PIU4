# (generated with --quick)

import abc
from typing import Any, Callable, Type, TypeVar

ABC: Type[abc.ABC]
json: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class BaseConfigObject(abc.ABC):
    __doc__: str
    @classmethod
    @abstractmethod
    def from_dict(cls, data) -> Any: ...
    @abstractmethod
    def to_cli(self) -> Any: ...
    @abstractmethod
    def to_dict(self) -> Any: ...
    def to_json(self) -> str: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
