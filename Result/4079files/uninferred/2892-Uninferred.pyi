from typing import Any

tmpdir: Any

def _hash(x: Any): ...
def _cache_path(key: Any): ...
def _cache_path_prefix(key: Any): ...
def _prefixes(key: Any): ...
def rm(url: Any, recursive: bool = ...) -> None: ...
def ls(url: Any, recursive: bool = ...): ...
def cp(src: Any, dst: Any, recursive: bool = ...) -> None: ...
def clear_storage() -> None: ...
def main() -> None: ...
