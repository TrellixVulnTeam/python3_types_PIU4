# (generated with --quick)

import cryptography.hazmat.primitives.ciphers.aead
from typing import Optional, Tuple, Type, Union

AESGCM: Type[cryptography.hazmat.primitives.ciphers.aead.AESGCM]
ciphertext: str
hashlib: module
os: module

def decrypt(passphrase: str, ciphertext: str) -> str: ...
def deriveKey(passphrase: str, salt: Optional[bytes] = ...) -> Tuple[bytes, bytes]: ...
def encrypt(passphrase: str, plaintext: str) -> str: ...
def hexlify(data: bytes) -> bytes: ...
def unhexlify(hexlify: Union[bytes, str]) -> bytes: ...
