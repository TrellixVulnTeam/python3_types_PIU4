import pykka
from http.server import BaseHTTPRequestHandler
from typing import Any

L: Any

class ExperimentActor(pykka.ThreadingActor):
    _config: Any = ...
    _view: Any = ...
    def __init__(self, config: dict, **kwargs: Any) -> None: ...
    _server_thread: Any = ...
    def on_start(self) -> None: ...
    def on_stop(self) -> None: ...
    def on_failure(self, exception_type: Any, exception_value: Any, traceback: Any) -> None: ...
    def on_receive(self, msg: dict) -> None: ...

class WebView(BaseHTTPRequestHandler):
    def __init__(self, request: Any, client_address: Any, server: Any) -> None: ...
    def _set_response(self, status_code: int = ...) -> None: ...
    def do_GET(self) -> None: ...
    def do_POST(self) -> None: ...

class NativeView:
    def __init__(self) -> None: ...