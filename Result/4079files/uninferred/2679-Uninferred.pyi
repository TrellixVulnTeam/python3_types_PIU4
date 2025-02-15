from typing import Any

URL: str

class Configuration:
    loop: Any = ...
    web_proto: Any = ...
    host: Any = ...
    port: Any = ...
    username: Any = ...
    password: Any = ...
    session: Any = ...
    def __init__(self, loop: Any, host: Any, username: Any, password: Any, *, port: int = ..., web_proto: str = ..., verify_ssl: bool = ...) -> None: ...
    @property
    def url(self): ...
