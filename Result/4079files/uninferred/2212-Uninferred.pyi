from handler.base_plugin import CommandPlugin
from typing import Any, Optional

class VoterPlugin(CommandPlugin):
    __slots__: Any = ...
    command_groups: Any = ...
    votes: Any = ...
    description: Any = ...
    def __init__(self, vote_commands: Optional[Any] = ..., vote_undo_commands: Optional[Any] = ..., votekick_commands: Optional[Any] = ..., prefixes: Optional[Any] = ..., strict: bool = ...) -> None: ...
    async def do_vote(self, msg: Any, title: Any, maximum: Optional[Any] = ..., votetime: int = ..., kick: Optional[Any] = ...) -> None: ...
    async def process_message(self, msg: Any): ...
