# (generated with --quick)

from typing import Any, Dict

engine: Any
event: Any
extensions: Any
sqla_session: Any

class AutocommitDatabase:
    _transaction_connections: Dict[Any, set]
    engine: Any
    session_factory: Any
    def __init__(self) -> None: ...
    def _get_dbapi_connection(self, connection) -> Any: ...
    def _handle_after_transaction_begin(self, session, transaction, connection) -> None: ...
    def _handle_after_transaction_end(self, session, transaction) -> None: ...
    def _should_disable_autocommit(self, transaction, connection) -> Any: ...
    def _should_reenable_autocommit(self, transaction) -> bool: ...
    def configure(self, database_url, **kwargs) -> None: ...
    def configure_engine(self, database_url, **kwargs) -> None: ...
    def create_connection_with_bound_session(self) -> Any: ...
    def disable_autocommit(self, transaction, connection) -> None: ...
    def reenable_autocommit(self, transaction) -> None: ...

class Session(Any):
    _has_only_root_transaction: Any
    _in_transaction: bool
    fake_root_transaction: Any
    transaction: Any
    def __init__(self, *args, fake_root_transaction = ..., **kwargs) -> None: ...
    def _create_faked_root_transaction(self) -> None: ...
    def _should_fake_transaction(self) -> Any: ...
    def begin(self, *args, nested = ..., **kwargs) -> Any: ...
    def commit(self) -> None: ...
    def revert_faked_transaction_if_needed(self) -> None: ...