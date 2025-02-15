import requests
from moneybird.authentication import Authentication
from typing import Any

VERSION: str
logger: Any

class MoneyBird:
    version: str = ...
    base_url: str = ...
    authentication: Any = ...
    session: Any = ...
    def __init__(self, authentication: Authentication) -> None: ...
    def get(self, resource_path: str, administration_id: int=...) -> Any: ...
    def post(self, resource_path: str, data: dict, administration_id: int=...) -> Any: ...
    def patch(self, resource_path: str, data: dict, administration_id: int=...) -> Any: ...
    def delete(self, resource_path: str, administration_id: int=...) -> Any: ...
    def renew_session(self) -> None: ...
    @classmethod
    def _get_url(cls: Any, administration_id: int, resource_path: str) -> Any: ...
    @staticmethod
    def _process_response(response: requests.Response, expected: list=...) -> dict: ...
    class APIError(Exception):
        _response: Any = ...
        def __init__(self, response: requests.Response, description: str=...) -> None: ...
        @property
        def status_code(self): ...
        @property
        def response(self): ...
        @property
        def request(self): ...
    class Unauthorized(APIError): ...
    class NotFound(APIError): ...
    class InvalidData(APIError): ...
    class Throttled(APIError): ...
    class ServerError(APIError): ...
