from twisted.internet.protocol import Protocol
from typing import Any, Optional

AUTHORITY: str
PATH: str

class H2Protocol(Protocol):
    conn: Any = ...
    known_proto: Any = ...
    request_made: bool = ...
    request_complete: bool = ...
    file_path: Any = ...
    flow_control_deferred: Any = ...
    fileobj: Any = ...
    file_size: Any = ...
    def __init__(self, file_path: Any) -> None: ...
    def connectionMade(self) -> None: ...
    def dataReceived(self, data: Any) -> None: ...
    def settingsAcked(self, event: Any) -> None: ...
    def handleResponse(self, response_headers: Any) -> None: ...
    def handleData(self, data: Any) -> None: ...
    def endStream(self) -> None: ...
    def windowUpdated(self, event: Any) -> None: ...
    def connectionLost(self, reason: Optional[Any] = ...) -> None: ...
    def sendRequest(self) -> None: ...
    def sendFileData(self) -> None: ...

filename: Any
filename = __file__
options: Any
