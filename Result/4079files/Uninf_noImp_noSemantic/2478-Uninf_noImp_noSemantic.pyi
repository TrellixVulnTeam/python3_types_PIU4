from typing import Any, IO, Optional

class Console:
    input_reader: Any = ...
    output_writer: Any = ...
    def __init__(self, input_reader: IO, output_writer: IO) -> None: ...
    def print(self, string: Optional[str]=..., end: str=..., flush: bool=...) -> None: ...
    def input(self, prompt: Optional[str]=...) -> str: ...
