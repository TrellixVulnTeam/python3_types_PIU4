# (generated with --quick)

from typing import Any, Callable

Qt: Any
asyncio: module
functools: module

def asyncified_done(parent, task) -> None: ...
def asyncified_unblock(dlg, cursor, task) -> None: ...
def asyncify(fn) -> Callable: ...
def asyncify_blocking(fn) -> Callable: ...
