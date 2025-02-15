from typing import Any, Optional

ZNODE_ACL: Any

class _zk:
    hosts: Any = ...
    client: Any = ...
    started: bool = ...
    def __init__(self, hosts: str=..., **kwargs: Any) -> None: ...
    def start(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def ensure(self, path: Any): ...
    def create(self, path: Any, data: Any): ...
    def set(self, path: Any, data: Any): ...
    def delete(self, path: Any): ...
    def rdelete(self, path: Any): ...
    def gets(self, path: Any): ...
    def get(self, path: Any): ...
    def list(self, path: Any): ...

class Record:
    topic: Any = ...
    broker_id: Any = ...
    partition_id: Any = ...
    consumer_offset: Any = ...
    total_offset: Any = ...
    backlog: Any = ...
    consumer_id: Any = ...
    lastmtime: Any = ...
    def __init__(self, topic: Optional[Any] = ..., broker_id: Optional[Any] = ..., partition_id: Optional[Any] = ..., consumer_offset: Optional[Any] = ..., total_offset: Optional[Any] = ..., backlog: Optional[Any] = ..., consumer_id: Optional[Any] = ..., lastmtime: Optional[Any] = ...) -> None: ...
    def data(self, group: Any): ...

def main(zk: Any) -> None: ...
