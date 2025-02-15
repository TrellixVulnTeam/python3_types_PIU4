import openhab.types
import typing
from typing import Any

__author__: str
__license__: str

class Item:
    types: typing.List[typing.Type[openhab.types.CommandType]] = ...
    openhab: Any = ...
    type_: Any = ...
    name: str = ...
    _state: Any = ...
    def __init__(self, openhab_conn: openhab.client.OpenHAB, json_data: dict) -> None: ...
    def init_from_json(self, json_data: dict) -> Any: ...
    @property
    def state(self) -> typing.Any: ...
    @state.setter
    def state(self, value: typing.Any) -> Any: ...
    def _validate_value(self, value: typing.Union[str, typing.Type[openhab.types.CommandType]]) -> Any: ...
    def _parse_rest(self, value: str) -> str: ...
    def _rest_format(self, value: str) -> str: ...
    def __set_state(self, value: str) -> Any: ...
    def __str__(self) -> str: ...
    def update(self, value: typing.Any) -> Any: ...
    def command(self, value: typing.Any) -> Any: ...

class DateTimeItem(Item):
    types: Any = ...
    def __gt__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def _parse_rest(self, value: Any): ...
    def _rest_format(self, value: Any): ...

class SwitchItem(Item):
    types: Any = ...
    def on(self) -> None: ...
    def off(self) -> None: ...

class NumberItem(Item):
    types: Any = ...
    def _parse_rest(self, value: Any): ...
    def _rest_format(self, value: Any): ...

class ContactItem(Item):
    types: Any = ...
    state: str = ...
    def open(self) -> None: ...
    def closed(self) -> None: ...

class DimmerItem(Item):
    types: Any = ...
    def _parse_rest(self, value: Any): ...
    def _rest_format(self, value: typing.Any) -> Any: ...
    def on(self) -> None: ...
    def off(self) -> None: ...
    def increase(self) -> None: ...
    def decrease(self) -> None: ...
