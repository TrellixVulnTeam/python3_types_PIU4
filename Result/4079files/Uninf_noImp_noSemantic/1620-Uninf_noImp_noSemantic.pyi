from .. import Params, Parseable
from typing import Any, Tuple

__all__: Any

class StatusAttribute(Parseable[bytes]):
    valid_statuses: Any = ...
    status: Any = ...
    def __init__(self, status: bytes) -> None: ...
    @property
    def value(self) -> bytes: ...
    @classmethod
    def parse(cls: Any, buf: memoryview, params: Params) -> Tuple[StatusAttribute, memoryview]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __bytes__(self) -> bytes: ...