from typing import Any

class DataPacket:
    data: Any = ...
    resize: Any = ...
    def __init__(self, msg: Any) -> None: ...

class WebsocketBinding:
    websocket: Any = ...
    def __init__(self, ws: Any) -> None: ...
    def send(self, data_str: Any) -> None: ...
    def send_error(self, error_str: Any) -> None: ...
    def receive(self): ...
    def close(self) -> None: ...