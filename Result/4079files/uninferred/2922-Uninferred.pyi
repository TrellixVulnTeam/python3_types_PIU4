from collections import namedtuple
from typing import Any, Optional

JSONRPC: str

JsonRpcMsg = namedtuple('JsonRpcMsg', ['type', 'data'])

class JsonRpcMsgTyp:
    REQUEST: int = ...
    NOTIFICATION: int = ...
    RESPONSE: int = ...
    RESULT: int = ...
    ERROR: int = ...

def decode_msg(raw_msg: Any): ...
def encode_request(method: Any, id: Optional[Any] = ..., params: Optional[Any] = ...): ...
def encode_notification(method: Any, params: Optional[Any] = ...): ...
def encode_result(id: Any, result: Any): ...
def encode_error(error: Any, id: Optional[Any] = ...): ...
def decode_error(msg: JsonRpcMsg) -> Any: ...
