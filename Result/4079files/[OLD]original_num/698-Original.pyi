# (generated with --quick)

import json.encoder
import ssl
from typing import Any, Callable, List, Optional, Tuple, Type, Union
import urllib.error
import urllib.request

HTTPError: Type[urllib.error.HTTPError]
Request: Type[urllib.request.Request]
argv: List[str]

def dumps(obj, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> str: ...
def main() -> None: ...
def send_issue_comment_hook(action: str, number: int, author: str, body: str) -> None: ...
def send_pull_request_hook(action: str, number: int, sha: str) -> None: ...
def send_webhook(event_name: str, payload: dict) -> None: ...
def urlopen(url: Union[str, urllib.request.Request], data: Optional[bytes] = ..., timeout: Optional[float] = ..., *, cafile: Optional[str] = ..., capath: Optional[str] = ..., cadefault: bool = ..., context: Optional[ssl.SSLContext] = ...) -> Any: ...
