# (generated with --quick)

from typing import Any, Callable, Sequence, Union

sys: module
tldap: Any

class Transaction(object):
    __doc__: str
    entering: Any
    exiting: Any
    using: Any
    def __call__(self, func) -> Callable: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __init__(self, entering, exiting, using) -> None: ...

class TransactionManagementError(Exception):
    __doc__: str

def _transaction_func(entering, exiting, using) -> Union[Transaction, Callable]: ...
def commit(using = ...) -> None: ...
def commit_manually(using = ...) -> Any: ...
def commit_on_success(using = ...) -> Any: ...
def enter_transaction_management(using = ...) -> None: ...
def is_dirty(using = ...) -> Any: ...
def is_managed(using = ...) -> Any: ...
def leave_transaction_management(using = ...) -> None: ...
def rollback(using = ...) -> None: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
