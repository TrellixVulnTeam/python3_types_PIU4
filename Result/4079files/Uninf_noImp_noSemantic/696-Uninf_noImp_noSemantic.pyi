from .. import db
from PIL import ImageDraw as ImageDraw
from typing import Any

message_handlers: Any

def on_message(pattern: Any, *flags: Any, start_only: bool = ...): ...
async def dad_jokes(ctx: Any, match: Any): ...
def load(category: Any, name: Any): ...

cat_head: Any
cat_body: Any
cat_tail: Any

async def longcat(ctx: Any, match: Any) -> None: ...
async def brutal_savage_rekt(ctx: Any, match: Any): ...

faces: Any

async def pointing_faces(ctx: Any, match: Any) -> None: ...
async def hat_hat(ctx: Any, match: Any) -> None: ...
async def message_listener(ctx: Any) -> None: ...
def setup(bot: Any) -> None: ...

response_names: Any

class GuildResponses(db.DatabaseObject):
    __tablename__: str = ...
    id: Any = ...

class ChannelResponses(db.DatabaseObject):
    __tablename__: str = ...
    id: Any = ...

class UserResponses(db.DatabaseObject):
    __tablename__: str = ...
    id: Any = ...
