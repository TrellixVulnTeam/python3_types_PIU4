# (generated with --quick)

import __future__
import cryptography.hazmat.primitives.asymmetric.padding
from typing import Any, Optional, TextIO, Type

GITHUB_REPO: str
PKCS1v15: Type[cryptography.hazmat.primitives.asymmetric.padding.PKCS1v15]
TRAVIS_CONFIG_FILE: str
argparse: module
args: argparse.Namespace
base64: module
json: module
os: module
parser: argparse.ArgumentParser
print_function: __future__._Feature
urlopen: Any
yaml: module

def default_backend() -> Any: ...
def encrypt(pubkey, password) -> bytes: ...
def fetch_public_key(repo) -> Any: ...
def getpass(prompt: str = ..., stream: Optional[TextIO] = ...) -> str: ...
def load_key(pubkey) -> Any: ...
def load_pem_public_key(data: bytes, backend) -> Any: ...
def load_yaml_config(filepath) -> Any: ...
def main(args) -> None: ...
def prepend_line(filepath, line) -> None: ...
def save_yaml_config(filepath, config) -> None: ...
def update_travis_deploy_password(encrypted_password) -> None: ...
