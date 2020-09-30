import abc
import aiohttp
import typing
from abc import abstractmethod
from enum import Enum
from typing import Any

class FilterOperation(Enum):
    equal: str = ...
    exists: str = ...
    greater_than: str = ...
    greater_than_equal: str = ...
    less_than: str = ...
    less_than_equal: str = ...
    not_equal: str = ...
    like: str = ...
    not_like: str = ...
    not_in: str = ...
    with_in: str = ...

class SortOrder(Enum):
    ascending: str = ...
    decending: str = ...

class FieldSort:
    _field: Any = ...
    _sort_order: Any = ...
    def __init__(self, field: str, sort_order: SortOrder) -> None: ...
    def to_string(self): ...

class Filter(metaclass=abc.ABCMeta):
    __metaclass__: Any = ...
    @abstractmethod
    def generate_node(self, parent_node: Any) -> Any: ...

class FieldFilter(Filter):
    operation: Any = ...
    name: Any = ...
    value: Any = ...
    def __init__(self, operation: FilterOperation, name: Any, value: Any) -> None: ...
    def generate_node(self, parent_node: Any): ...

class OrFilter(Filter):
    filters: Any = ...
    def __init__(self, filters: typing.List[Filter]) -> None: ...
    def generate_node(self, parent_node: Any): ...

class AndFilter(Filter):
    filters: Any = ...
    def __init__(self, filters: typing.List[Filter]) -> None: ...
    def generate_node(self, parent_node: Any): ...

class Trafikverket:
    _api_url: str = ...
    date_time_format: str = ...
    date_time_format_for_modified: str = ...
    _client_session: Any = ...
    _api_key: Any = ...
    def __init__(self, client_session: aiohttp.ClientSession, api_key: str) -> None: ...
    def _generate_request_data(self, objecttype: str, includes: typing.List[str], filters: typing.List[Filter], limit: int=..., sorting: typing.List[FieldSort]=...) -> Any: ...
    async def async_make_request(self, objecttype: str, includes: typing.List[str], filters: typing.List[Filter], limit: int=..., sorting: typing.List[FieldSort]=...) -> Any: ...

class NodeHelper:
    _node: Any = ...
    def __init__(self, node: Any) -> None: ...
    def get_text(self, field: Any): ...
    def get_texts(self, field: Any): ...
    def get_datetime_for_modified(self, field: Any): ...
    def get_datetime(self, field: Any): ...
    def get_bool(self, field: Any): ...