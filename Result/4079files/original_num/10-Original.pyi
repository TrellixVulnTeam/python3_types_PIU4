# (generated with --quick)

from typing import Any, Dict, Optional, Tuple

Account: Any
Address: Any
Web3: Any
_registered_accounts: Dict[Tuple[Any, Any], Any]
construct_sign_and_send_raw_middleware: Any
getpass: module

def register_key(web3, key: str) -> None: ...
def register_key_file(web3, key_file: str, pass_file: Optional[str] = ...) -> None: ...
def register_keys(web3, keys: Optional[list]) -> None: ...
def register_private_key(web3, private_key) -> None: ...
