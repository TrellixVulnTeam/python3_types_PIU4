# (generated with --quick)

import typing
from typing import Any, Type

Counter: Type[typing.Counter]

def build_codebook(tree, code = ...) -> list: ...
def build_huffman_tree(message) -> Any: ...
def huffman_decode(codebook, encoded_message) -> str: ...
def huffman_encode(codebook, message) -> str: ...
def main() -> None: ...