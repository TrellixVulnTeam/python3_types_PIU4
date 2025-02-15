import requests
from requests.auth import AuthBase
from typing import Any, Dict, List, MutableMapping, Optional, Sequence, Tuple, Union
from typing.io import BinaryIO as BinaryIO, IO as IO

class AptlyAPIException(Exception):
    status_code: Any = ...
    def __init__(self, *args: Any, status_code: int=...) -> None: ...

class BaseAPIClient:
    base_url: Any = ...
    ssl_verify: Any = ...
    ssl_cert: Any = ...
    http_auth: Any = ...
    exc_class: Any = ...
    timeout: Any = ...
    def __init__(self, base_url: str, ssl_verify: Union[str, bool, None]=..., ssl_cert: Optional[Tuple[str, str]]=..., http_auth: Optional[AuthBase]=..., timeout: int=...) -> None: ...
    def _error_from_response(self, resp: requests.Response) -> str: ...
    def _make_url(self, path: str) -> str: ...
    def do_get(self, urlpath: str, params: Optional[Dict[str, str]]=...) -> requests.Response: ...
    def do_post(self, urlpath: str, data: Union[bytes, MutableMapping[str, str], IO[Any], None]=..., params: Optional[Dict[str, str]]=..., files: Union[Dict[str, IO], Dict[str, Tuple[str, Union[IO, BinaryIO], Optional[str], Optional[Dict[str, str]]]], Dict[str, Tuple[str, str]], Sequence[Tuple[str, Union[IO, BinaryIO]]], Sequence[Tuple[str, Union[IO, BinaryIO], Optional[str], Optional[Dict[str, str]]]], None]=..., json: Optional[MutableMapping[Any, Any]]=...) -> requests.Response: ...
    def do_put(self, urlpath: str, data: Union[bytes, MutableMapping[str, str], IO[Any]]=..., files: Union[Dict[str, IO], Dict[str, Tuple[str, IO, Optional[str], Optional[Dict[str, str]]]], Dict[str, Tuple[str, str]], Sequence[Tuple[str, IO]], Sequence[Tuple[str, IO, Optional[str], Optional[Dict[str, str]]]], None]=..., json: Optional[MutableMapping[Any, Any]]=...) -> requests.Response: ...
    def do_delete(self, urlpath: str, params: Optional[Dict[str, str]]=..., data: Union[str, Dict[str, str], Sequence[Tuple[str, str]], None]=..., json: Union[List[Dict[str, Any]], Dict[str, Any], None]=...) -> requests.Response: ...
