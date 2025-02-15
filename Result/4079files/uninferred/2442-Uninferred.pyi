from typing import Any, Optional

log: Any

class GithubCards:
    __author__: str = ...
    __version__: str = ...
    bot: Any = ...
    settings: Any = ...
    ignore: bool = ...
    colour: Any = ...
    def __init__(self, bot: Any) -> None: ...
    async def githubcards(self, ctx: Any) -> None: ...
    async def add(self, ctx: Any, prefix: Any, github: Any) -> None: ...
    async def edit(self, ctx: Any, prefix: Any, field: Optional[Any] = ...) -> None: ...
    async def remove(self, ctx: Any, prefix: Any) -> None: ...
    async def list(self, ctx: Any) -> None: ...
    async def get_issue(self, message: Any): ...
    async def post_issue(self, message: Any, prefix: Any, number: Any): ...
    def save_json(self) -> None: ...

def check_folder() -> None: ...
def check_file() -> None: ...
def setup(bot: Any) -> None: ...
