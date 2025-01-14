# (generated with --quick)

import asyncio.locks
import asyncio.tasks
from typing import Any, Coroutine, Optional

CHANNEL_PREFIX: str
PRESENCE_CHANNEL: str
_logger: logging.Logger
asyncio: module
discord: Any
enum: module
logging: module
re: module
string: module

class IRCServer:
    _port: Any
    _stop_event: asyncio.locks.Event
    def __init__(self, port = ...) -> None: ...
    def _handler(self, reader, writer) -> Coroutine[Any, Any, None]: ...
    def run(self) -> Coroutine[Any, Any, None]: ...

class IRCSession:
    ClientCommand: type
    State: type
    _channel_ids: set
    _discord_client: Any
    _discord_connect_task: Optional[asyncio.tasks.Task]
    _password: Any
    _reader: Any
    _state: Any
    _username: Any
    _writer: Any
    def __init__(self, reader, writer) -> None: ...
    def _handle_discord_message(self, message) -> Coroutine[Any, Any, None]: ...
    def _handle_login(self, command) -> Coroutine[Any, Any, bool]: ...
    def _handle_message_command(self, command) -> Coroutine[Any, Any, None]: ...
    def _join_command(self, command) -> Coroutine[Any, Any, None]: ...
    def _part_command(self, command) -> Coroutine[Any, Any, None]: ...
    def _ping_command(self, command) -> Coroutine[Any, Any, None]: ...
    def _presence_command(self, command) -> Coroutine[Any, Any, None]: ...
    def _privmsg_command(self, command) -> Coroutine[Any, Any, None]: ...
    def _reply(self, *args, tags = ..., username = ...) -> Coroutine[Any, Any, None]: ...
    @classmethod
    def escape_tag_value(cls, text) -> Any: ...
    @classmethod
    def escape_username(cls, name) -> str: ...
    def handle(self) -> Coroutine[Any, Any, None]: ...

def main() -> None: ...
