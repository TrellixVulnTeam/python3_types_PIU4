from http.client import HTTPConnection as HTTPConnection
from typing import Any, Optional, Tuple

class HTTPError(Exception):
    response: Any = ...
    def __init__(self, msg: Any, response: Any) -> None: ...

def get_server_response(data: Optional[str], host: str, path: str) -> bytes: ...
def enroll(data: str, host: str=..., path: str=...) -> bytes: ...
def request_new_serial(region: str=..., model: str=...) -> Tuple[str, str]: ...
def get_time_offset(region: str=..., path: str=...) -> int: ...
def restore(serial: str, restore_code: str) -> str: ...
def initiate_paper_restore(serial: str, host: str=..., path: str=...) -> bytes: ...
def validate_paper_restore(data: str, host: str=..., path: str=...) -> bytes: ...
