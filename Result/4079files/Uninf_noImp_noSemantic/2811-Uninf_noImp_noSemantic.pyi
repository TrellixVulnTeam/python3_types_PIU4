from typing import Any, Optional

def get_value(_file: Any, key: Optional[Any] = ...): ...
def set_value(_file: Any, key: Any, value: Any): ...
def rm_value(_file: Any, key: Any): ...
def add_value(orig_file: Any, orig_key: Any, value: Any): ...