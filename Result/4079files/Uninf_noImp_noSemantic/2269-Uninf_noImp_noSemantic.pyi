from utils import *
from typing import Any, List

tests_performed_cache_loc: Any
dictionaries_loc: Any
tests_performed: Any
proper_nouns: Any

def load_proper_noun_data() -> List[str]: ...
def write_cache() -> None: ...
def open_cache() -> None: ...
def prompt_and_confirm(prompt: str) -> bool: ...
def get_first_word(line: str) -> str: ...
def check_test_performed(text: Any, test: str) -> bool: ...
def set_test_performed(text: Any, test: str) -> None: ...
def decapitalize_beginnings_of_lines(the_poem: List[str], poem_path: str) -> List[str]: ...
def check_file(what_file: str) -> None: ...
