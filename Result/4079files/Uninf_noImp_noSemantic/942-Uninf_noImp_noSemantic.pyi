import asyncio
from typing import Any, Optional

__all__: Any
ALL: str
EVENTS: Any

class Runner:
    registry: Any = ...
    def __init__(self, *bots: Any) -> None: ...
    def add_bot(self, bot: Any) -> None: ...
    def gather(self): ...

class Bot:
    slack: Any = ...
    uuid: Any = ...
    handlers: Any = ...
    daemons: Any = ...
    environment: Any = ...
    params: Any = ...
    def __init__(self, token: Any, daemons: Optional[Any] = ..., **kwargs: Any) -> None: ...
    running: bool = ...
    _message_id: int = ...
    def __call__(self): ...
    def __repr__(self): ...
    @property
    def id(self): ...
    @property
    def name(self): ...
    ws: Any = ...
    @asyncio.coroutine
    def ws_handler(self, url: Any, handler: Any) -> None: ...
    @asyncio.coroutine
    def ws_keepalive(self) -> None: ...
    def listen(self, coro: Any) -> None: ...
    @asyncio.coroutine
    def post(self, channel_name_or_id: Any, text: Any) -> None: ...
    @asyncio.coroutine
    def ping(self) -> None: ...
    def get_channel(self, name_or_id: Any): ...
    def get_group(self, name_or_id: Any): ...
    def get_user(self, name_or_id: Any): ...
    def _env_item(self, key: Any, name_or_id: Any, prefix: Optional[Any] = ...): ...

def run(*bots: Any) -> None: ...