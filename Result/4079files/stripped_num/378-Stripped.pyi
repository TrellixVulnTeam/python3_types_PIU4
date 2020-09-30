# (generated with --quick)

import http.server
from typing import Any, NoReturn, Optional, Type

Action: Any
BaseHTTPRequestHandler: Type[http.server.BaseHTTPRequestHandler]
L: logging.Logger
Server: Any
json: module
logging: module
pykka: Any
threading: module

class ExperimentActor(Any):
    _config: Any
    _server_thread: Optional[threading.Thread]
    _view: Any
    def __init__(self, config, **kwargs) -> None: ...
    def on_failure(self, exception_type, exception_value, traceback) -> None: ...
    def on_receive(self, msg) -> None: ...
    def on_start(self) -> None: ...
    def on_stop(self) -> None: ...

class NativeView(object):
    def __init__(self) -> NoReturn: ...

class WebView(http.server.BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server) -> None: ...
    def _set_response(self, status_code = ...) -> None: ...
    def do_GET(self) -> None: ...
    def do_POST(self) -> None: ...