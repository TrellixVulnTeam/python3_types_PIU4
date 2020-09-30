def key_is_involutary(pKey: int, pModulus: int) -> bool: ...
def key_is_trivial(pKey: int, pModulus: int) -> bool: ...
def do_encrypt(pByte: int, pKey: int, pModulus: int) -> int: ...
def do_decrypt(pByte: int, pKey: int, pModulus: int) -> int: ...
def encrypt(pPlaintextBytes: bytearray, pKey: int, pModulus: int) -> bytearray: ...
def decrypt(pCiphertextBytes: bytearray, pKey: int, pModulus: int) -> bytearray: ...
def print_plaintext(pInput: bytearray, pKey: int, pModulus: int, pVerbose: bool) -> None: ...
def is_unprintable(pBytes: bytearray) -> bool: ...
def print_ciphertext(pInput: bytearray, pKey: int, pModulus: int, pVerbose: bool, pOutputFormat: str) -> None: ...
def bruteforce_plaintext(pInput: bytearray, pModulus: int, pVerbose: bool) -> None: ...
def derive_key(pKeyString: str, pModulus: int) -> int: ...