from typing import Any, Iterator, Sequence

_PRINTABLE: Any
_EMPTY_BLOCK: Any

def get_mask(n: int) -> int: ...
def get_stream(key: bytes, nonce: bytes) -> Iterator[int]: ...
def get_password(kdf_rounds: int, character_set: Sequence[str], length: int, increment: int, site_name: str, master_password: str) -> str: ...
