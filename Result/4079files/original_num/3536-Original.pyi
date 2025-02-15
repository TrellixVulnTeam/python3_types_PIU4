# (generated with --quick)

import __builtin__
from typing import Any, Coroutine

AbstractListedStorage: Any
Connector: Any
FieldStorageMixin: Any

class HashStorage(Any, Storage):
    def get(self, key, *, field = ..., fields = ...) -> coroutine: ...
    def set(self, key, value, *, field = ..., fields = ...) -> coroutine: ...

class Storage(Any, Any):
    def get(self, key) -> coroutine: ...
    def length(self) -> Coroutine[Any, Any, int]: ...
    def list(self) -> Coroutine[Any, Any, __builtin__.list]: ...
    def set(self, key, value) -> coroutine: ...
