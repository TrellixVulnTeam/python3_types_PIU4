from dog import Cog
from dog.core.context import DogbotContext
from dog.core.converters import RawMember
from typing import Any

logger: Any

class About(Cog):
    maker: Any = ...
    def __init__(self, bot: Any) -> None: ...
    async def invite(self, ctx: DogbotContext) -> Any: ...
    async def generate_invite(self, ctx: Any, *client_ids: RawMember) -> Any: ...
    async def wiki(self, ctx: Any) -> None: ...
    async def about(self, ctx: Any) -> None: ...
    async def _github(self, ctx: Any) -> None: ...

def setup(bot: Any) -> None: ...
