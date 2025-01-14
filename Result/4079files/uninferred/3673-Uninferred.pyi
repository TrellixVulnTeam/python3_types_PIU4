from ....database import db
from typing import Any

class Subject(db.Model):
    __tablename__: str = ...
    id: Any = ...
    name: Any = ...
    title: Any = ...
    type_: Any = ...
    def __init__(self, name: str, title: str, type_: str) -> None: ...
    def __repr__(self) -> str: ...
