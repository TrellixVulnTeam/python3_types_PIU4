# (generated with --quick)

from typing import Any, Dict

TRIES: Dict[str, Any]
data_filename: Any
json: module
langcodes: Any
marisa_trie: Any
warnings: module

def code_to_names(category, code) -> dict: ...
def get_trie_value(trie, key) -> Any: ...
def load_trie(filename) -> Any: ...
def name_to_code(category, name, language = ...) -> Any: ...
def normalize_name(name) -> Any: ...
