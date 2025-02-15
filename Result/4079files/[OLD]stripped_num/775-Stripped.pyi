# (generated with --quick)

from typing import Any, Coroutine, Dict, Pattern, Tuple

Organiser: Any
logger: logging.Logger
logging: module
re: module

class GatherBot:
    actions: Dict[Any, Tuple[Pattern, Any]]
    message_handlers: list
    organiser: Any
    username: Any
    def __init__(self, username) -> None: ...
    def announce_players(self, channel) -> Coroutine[Any, Any, None]: ...
    def member_went_afk(self, before) -> Coroutine[Any, Any, None]: ...
    def member_went_offline(self, before) -> Coroutine[Any, Any, None]: ...
    def on_message(self, message) -> Coroutine[Any, Any, None]: ...
    def player_count_display(self, channel) -> str: ...
    def register_action(self, regex, coro) -> None: ...
    def register_message_handler(self, handler) -> None: ...
    def say(self, channel, message) -> Coroutine[Any, Any, None]: ...
    def say_lines(self, channel, messages) -> Coroutine[Any, Any, None]: ...
