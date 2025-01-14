from collections import namedtuple
from typing import Any, Optional

logger: Any
CP_REGEX: Any
ENTITY_REGEX: Any
BAD_UNICODE_CATS: Any

def cldr_sub(value: Any, repl: Any, ignore_space: bool = ...): ...
def decode_u(v: Any, newlines: bool = ...): ...
def encode_u(v: Any): ...
def key_cmp(x: Any): ...
def process_value(*args: Any): ...
def cell_range(ch: Any, from_: Any, to_: Any) -> None: ...
def parse_cell(x: Any): ...
def is_relevant_cell(x: Any): ...

class UnknownNgramException(Exception): ...

def split_for_set(s: Any, string: Any): ...
def keyboard_range(): ...
def is_full_layout(o: Any): ...
def filtered(v: Any): ...
def to_xml(yaml_tree: Any): ...

class CLDRKeyboard:
    @classmethod
    def from_file(cls, f: Any): ...
    _filename: Any = ...
    _modes: Any = ...
    _transforms: Any = ...
    _key_set: Any = ...
    _deadkey_set: Any = ...
    _deadkeys: Any = ...
    _comments: Any = ...
    _space: Any = ...
    _internal_name: Any = ...
    _locale: Any = ...
    _name: Any = ...
    def __init__(self, data: Any, filename: Optional[Any] = ...) -> None: ...
    def _generate_keyset(self, tree: Any) -> None: ...
    def _parse_keymaps(self, tree: Any) -> None: ...
    def _parse_transforms(self, tree: Any) -> None: ...
    def keys(self, mode: Any): ...
    def _as_yaml_transforms(self, x: Any) -> None: ...
    def as_yaml(self): ...

Left: str
Right: str
Both: str
Shift: str
Alt: str
Caps: str
Ctrl: str
OSXCommand: str
TOKENS: Any

ModeToken = namedtuple('CLDRMode', ['name', 'direction', 'required'])

class CLDRMode:
    _raw: Any = ...
    _kbdgen: Any = ...
    def __init__(self, data: Any) -> None: ...
    def _parse_tokens(self, tokens: Any): ...
    def _init_kbdgen(self): ...
    @property
    def kbdgen(self): ...
    @property
    def cldr(self): ...

def cldr2kbdgen_main() -> None: ...
def kbdgen2cldr_main() -> None: ...
