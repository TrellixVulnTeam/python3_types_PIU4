from typing import Any, Optional

class BlockInfo:
    codepoint_from: Any = ...
    _name: Any = ...
    def __init__(self, codepoint_from: int, name: str) -> None: ...
    def block_id(self) -> int: ...
    def name(self) -> str: ...
    def url(self) -> str: ...
    def u_plus(self) -> str: ...

class Block:
    info: Any = ...
    codepoint_to: Any = ...
    wikipedia: Any = ...
    wikipedia_summary: Any = ...
    prev: Any = ...
    next: Any = ...
    def __init__(self, codepoint_from: int, codepoint_to: int, name: str) -> None: ...
    def block_id(self) -> int: ...
    def name(self) -> str: ...
    def url(self) -> str: ...
    def u_plus(self) -> str: ...
    def from_codepoint(self) -> int: ...
    def to_codepoint(self) -> int: ...
    def contains(self, codepoint: int) -> bool: ...
    def codepoints_iter(self): ...
    def fetch_wikipedia(self) -> None: ...
    @staticmethod
    def _format_wikipedia(wikipedia_text: str) -> str: ...

class Subblock:
    codepoint_from: Any = ...
    codepoint_to: Any = ...
    _name: Any = ...
    def __init__(self, codepoint_from: int, codepoint_to: Optional[int], name: str) -> None: ...
    def block_id(self) -> int: ...
    def name(self) -> str: ...
    def from_codepoint(self) -> int: ...
    def to_codepoint(self) -> Optional[int]: ...
    def set_to_codepoint(self, codepoint: Optional[int]) -> Any: ...
    def contains(self, codepoint: int) -> bool: ...
    def codepoints_iter(self): ...