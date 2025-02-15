from flask_login import AnonymousUserMixin, UserMixin
from flask_mongoengine import Document
from typing import Any, Dict, Optional, Type

class Group(Document):
    id: Any = ...
    description: Any = ...
    allowed_types: Any = ...
    meta: Any = ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class User(Document, UserMixin):
    username: Any = ...
    password: Any = ...
    name: Any = ...
    email: Any = ...
    active: Any = ...
    admin: Any = ...
    groups: Any = ...
    last_login: Any = ...
    processed: Any = ...
    def is_active(self) -> bool: ...
    def is_admin(self) -> bool: ...
    def is_eligible_for(self, task_type: str) -> bool: ...
    def get_stats(self, task_type: Any) -> Dict[str, int]: ...
    def as_dict(self) -> Dict[str, str]: ...
    @classmethod
    def pre_save(cls: Any, sender: Type, document: Document, **kwargs: Dict) -> Document: ...
    @classmethod
    def get_by_id(cls: Any, user_id: str) -> Optional[Document]: ...
    def __str__(self) -> str: ...

class Anonymous(AnonymousUserMixin):
    name: str = ...
