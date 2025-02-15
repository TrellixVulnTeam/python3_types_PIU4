# (generated with --quick)

from typing import Any

basics: Any
importlib: module

class AbstractAggregator(Any, metaclass=AggregatorRegistry):
    def provides(self) -> str: ...
    def requires(self) -> str: ...
    def run(self) -> None: ...

class AggregatorRegistry(type):
    aggregators: dict
    def __new__(cls, name, bases, dct) -> Any: ...
    @classmethod
    def get(cls, name) -> Any: ...
    @classmethod
    def load(cls, *aggregator_modules) -> None: ...
