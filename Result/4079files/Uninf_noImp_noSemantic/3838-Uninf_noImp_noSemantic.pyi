import aiozmq.rpc
import asyncio
from typing import Any

class Point:
    x: Any = ...
    y: Any = ...
    def __init__(self, x: Any, y: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...

translation_table: Any

class ServerHandler(aiozmq.rpc.AttrHandler):
    def remote(self, val: Any): ...

@asyncio.coroutine
def go() -> None: ...
def main() -> None: ...
