from typing import Any

class UrbanDictionary:
    bot: Any = ...
    color: Any = ...
    def __init__(self, bot: Any) -> None: ...
    async def urban(self, ctx: Any, query: str) -> Any: ...
    async def random(self, ctx: Any) -> None: ...

def setup(bot: Any) -> None: ...
