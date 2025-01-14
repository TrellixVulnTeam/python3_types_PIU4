from copy import deepcopy as deepcopy
from typing import Any, Optional

class Action:
    _actions: Any = ...
    action: bool = ...
    name: Any = ...
    method: Any = ...
    types: Any = ...
    def __init__(self, method: Any) -> None: ...
    def apply(self, state: Any, *args: Any): ...
    def ground(self, *args: Any): ...
    def __call__(self, *args: Any): ...

class GroundAction:
    action: Any = ...
    args: Any = ...
    def __init__(self, action: Any, *args: Any) -> None: ...
    def __str__(self): ...
    def __repr__(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def apply(self, s: Any): ...

class Object:
    _objects: Any = ...
    @staticmethod
    def get_types(): ...
    @staticmethod
    def get_objects_of_type(t: Any): ...
    name: Any = ...
    def __init__(self, name: Any) -> None: ...
    def __str__(self): ...
    def __repr__(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

class State:
    def __str__(self): ...
    def __repr__(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def copy(self): ...
    def actions(self) -> None: ...
    def pick_action(self) -> None: ...
    def action_sequence(self, length: Any) -> None: ...
    def plan_bfs(self, goal: Any, cur_len: int = ..., max_len: Optional[Any] = ...) -> None: ...

class UnsatisfiedPreconditions(Exception): ...
