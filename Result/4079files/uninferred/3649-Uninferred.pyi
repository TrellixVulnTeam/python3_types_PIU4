from typing import Any

GOOD_SUBFOLDERS: Any

def check_group(target_dir: Any, prefix: Any, target_ext: str = ...): ...
def check(target: Any, prefix: Any): ...
def format_results(results: Any, partial: bool = ...): ...
def check_dirs(*, dirs: Any = ..., output_dir: str = ..., prefix: str = ..., partial: bool = ...): ...
def post_merge_check(check_file: Any) -> None: ...
def check_final(*, dirs: Any = ..., output_dir: str = ...) -> None: ...
