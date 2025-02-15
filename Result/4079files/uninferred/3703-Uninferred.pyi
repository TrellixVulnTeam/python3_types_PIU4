from discord import Channel as Channel
from src.bunkbot import BunkBot
from typing import Any

class BunkRPG:
    bot: Any = ...
    duels: Any = ...
    def __init__(self, bot: BunkBot) -> None: ...
    async def wire_decay_check(self) -> None: ...
    async def check_decayed_xp(self) -> None: ...
    async def ding(self, member: Any, value: Any, channel: Channel=...) -> None: ...
    async def leader(self, ctx: Any) -> None: ...
    async def level(self, ctx: Any) -> None: ...
    async def duel(self, ctx: Any) -> None: ...
    async def accept(self, ctx: Any) -> None: ...
    async def reject(self, ctx: Any) -> None: ...
    async def cancel(self, ctx: Any) -> None: ...

def setup(bot: BunkBot) -> None: ...
