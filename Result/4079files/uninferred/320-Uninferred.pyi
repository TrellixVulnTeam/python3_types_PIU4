from typing import Any

def merge(a: Any, lo: Any, mid: Any, hi: Any, buf: Any) -> None: ...
def merge_inplace(a: Any, lo: Any, mid: Any, hi: Any) -> None: ...
def merge_n(a: Any, run: Any) -> None: ...
def merge_lists(xs: Any, ys: Any): ...
def merge_n_lists(lsts: Any): ...

MIN_MERGE: int

def merge_sort(arr: Any, lo: Any, hi: Any) -> None: ...
