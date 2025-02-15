import asyncio
import discord
import enum
from typing import Any, Optional

_logger: Any
CHANNEL_PREFIX: str
PRESENCE_CHANNEL: str

class IRCServer:
    _port: Any = ...
    _stop_event: Any = ...
    def __init__(self, port: int=...) -> None: ...
    @asyncio.coroutine
    def run(self) -> None: ...
    @asyncio.coroutine
    def _handler(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> Any: ...

class IRCSession:
    class State(enum.Enum):
        wait_for_login: str = ...
        logged_in: str = ...
    class ClientCommand:
        line: Any = ...
        args: Any = ...
        command: Any = ...
        text: Any = ...
        def __init__(self, line: str) -> None: ...
    _reader: Any = ...
    _writer: Any = ...
    _state: Any = ...
    _discord_client: Any = ...
    _channel_ids: Any = ...
    _username: Any = ...
    _password: Any = ...
    _discord_connect_task: Any = ...
    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None: ...
    @asyncio.coroutine
    def handle(self) -> None: ...
    @classmethod
    def escape_tag_value(cls: Any, text: str) -> str: ...
    @asyncio.coroutine
    def _reply(self, *args: Any, tags: Optional[Any] = ..., username: Optional[Any] = ...) -> None: ...
    @asyncio.coroutine
    def _handle_login(self, command: ClientCommand) -> bool: ...
    @asyncio.coroutine
    def _handle_message_command(self, command: ClientCommand) -> Any: ...
    @asyncio.coroutine
    def _ping_command(self, command: ClientCommand) -> Any: ...
    @asyncio.coroutine
    def _join_command(self, command: ClientCommand) -> Any: ...
    @asyncio.coroutine
    def _part_command(self, command: ClientCommand) -> Any: ...
    @asyncio.coroutine
    def _privmsg_command(self, command: ClientCommand) -> Any: ...
    @asyncio.coroutine
    def _presence_command(self, command: ClientCommand) -> Any: ...
    @asyncio.coroutine
    def _handle_discord_message(self, message: discord.Message) -> Any: ...
    @classmethod
    def escape_username(cls: Any, name: str) -> str: ...

def main() -> None: ...
