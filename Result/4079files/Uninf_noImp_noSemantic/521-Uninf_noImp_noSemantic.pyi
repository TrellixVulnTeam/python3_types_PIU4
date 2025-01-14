from enum import Enum
from typing import Any, Optional

__all__: Any
LOG: Any

class ConnectionState(Enum):
    NEW: int = ...
    SETUP: int = ...
    ESTABLISHED: int = ...
    FAILED: int = ...
    FINISHED: int = ...

class ConnectionProtocol:
    name: Any = ...
    version: Any = ...
    state: Any = ...
    def __init__(self, name: Optional[Any] = ..., version: Optional[Any] = ..., state: Optional[Any] = ...) -> None: ...

class Connection:
    address: Any = ...
    port: Any = ...
    socket: Any = ...
    switch: Any = ...
    protocol: Any = ...
    remaining_data: bytes = ...
    def __init__(self, address: Any, port: Any, socket: Any, switch: Optional[Any] = ...) -> None: ...
    def __str__(self): ...
    def __repr__(self): ...
    @property
    def state(self): ...
    _state: Any = ...
    @state.setter
    def state(self, new_state: Any) -> None: ...
    @property
    def id(self): ...
    def send(self, buffer: Any) -> None: ...
    def close(self) -> None: ...
    def is_alive(self): ...
    def is_new(self): ...
    def is_established(self): ...
    def is_during_setup(self): ...
    def set_established_state(self) -> None: ...
    def set_setup_state(self) -> None: ...
    def update_switch(self, switch: Any) -> None: ...
