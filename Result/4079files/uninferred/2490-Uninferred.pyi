from pip.backwardcompat import u as u
from typing import Any

stringEscapeSequence: str
irirefEscapeSequence: str
stringEscapeReplacements: Any
semactEscapeReplacements: Any

def sub_unicode4(unicode4: Any): ...
def sub_unicode8(unicode8: Any): ...
def f(sequence: Any, unicode4: Any, unicode8: Any, escaped_char: Any): ...
def unescape(string: Any, regex: Any, replacements: Any): ...
def unescape_string(string: str, trim_length: int=...) -> str: ...