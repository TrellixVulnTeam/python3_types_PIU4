# (generated with --quick)

from typing import Any

SysUtil: Any
client: Any
iden: bytes
time: module

def crc32(__data: bytes, __value: int = ...) -> int: ...
def main() -> None: ...
def on_connect(client, *args) -> None: ...
def on_message(client, userdata, msg) -> None: ...
def setupmqtt() -> None: ...