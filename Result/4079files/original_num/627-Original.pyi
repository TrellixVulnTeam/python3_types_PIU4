# (generated with --quick)

from typing import Any, Tuple

Address: Any
Web3: Any
_registered_accounts: Any
bytes_to_hexstring: Any
defunct_hash_message: Any
encode_hex: Any

def eth_sign(message: bytes, web3) -> Any: ...
def to_vrs(signature: str) -> Tuple[int, bytes, bytes]: ...
