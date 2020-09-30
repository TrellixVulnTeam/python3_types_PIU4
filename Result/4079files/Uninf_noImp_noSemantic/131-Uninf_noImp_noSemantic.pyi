from ....database import BaseQuery, db
from ....typing import UserID
from ..transfer.models import ChannelID, ItemID
from typing import Any

class ItemQuery(BaseQuery):
    def for_channel(self, channel_id: ChannelID) -> BaseQuery: ...
    def published(self) -> BaseQuery: ...
    def with_current_version(self) -> BaseQuery: ...

class Item(db.Model):
    __tablename__: str = ...
    __table_args__: Any = ...
    query_class: Any = ...
    id: Any = ...
    created_at: Any = ...
    channel_id: Any = ...
    channel: Any = ...
    slug: Any = ...
    published_at: Any = ...
    current_version: Any = ...
    def __init__(self, channel_id: ChannelID, slug: str) -> None: ...
    @property
    def title(self) -> str: ...
    @property
    def published(self) -> bool: ...
    def __repr__(self) -> str: ...

class ItemVersionQuery(BaseQuery):
    def for_item(self, item_id: ItemID) -> BaseQuery: ...

class ItemVersion(db.Model):
    __tablename__: str = ...
    query_class: Any = ...
    id: Any = ...
    item_id: Any = ...
    item: Any = ...
    created_at: Any = ...
    creator_id: Any = ...
    creator: Any = ...
    title: Any = ...
    body: Any = ...
    image_url_path: Any = ...
    def __init__(self, item: Item, creator_id: UserID, title: str, body: str) -> None: ...
    @property
    def is_current(self) -> bool: ...
    def render_body(self) -> str: ...
    def __repr__(self) -> str: ...

class CurrentVersionAssociation(db.Model):
    __tablename__: str = ...
    item_id: Any = ...
    item: Any = ...
    version_id: Any = ...
    version: Any = ...
    def __init__(self, item: Item, version: ItemVersion) -> None: ...