from nodes import Node
from typing import Any

class KillStack(Node):
    char: str = ...
    args: int = ...
    results: int = ...
    default_arg: int = ...
    def __init__(self, amount: Node.NumericLiteral) -> None: ...
    newline_length: Any = ...
    def prepare(self, stack: Any) -> None: ...
    def func(self, *args: Any): ...
    def set_auto_newline(self) -> None: ...