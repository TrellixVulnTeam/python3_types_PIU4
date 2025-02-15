import openhab.items
import requests
import typing
from typing import Any

__author__: str
__license__: str

class OpenHAB:
    base_url: Any = ...
    session: Any = ...
    timeout: Any = ...
    def __init__(self, base_url: str, username: typing.Optional[str]=..., password: typing.Optional[str]=..., http_auth: typing.Optional[requests.auth.AuthBase]=..., timeout: typing.Optional[float]=...) -> None: ...
    @staticmethod
    def _check_req_return(req: requests.Response) -> None: ...
    def req_get(self, uri_path: str) -> typing.Any: ...
    def req_post(self, uri_path: str, data: typing.Optional[dict]=...) -> None: ...
    def req_put(self, uri_path: str, data: typing.Optional[dict]=...) -> None: ...
    def fetch_all_items(self) -> dict: ...
    def get_item(self, name: str) -> openhab.items.Item: ...
    def json_to_item(self, json_data: dict) -> openhab.items.Item: ...
    def get_item_raw(self, name: str) -> typing.Any: ...

class openHAB(OpenHAB):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
