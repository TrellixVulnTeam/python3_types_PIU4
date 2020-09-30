# (generated with --quick)

from typing import Any, Callable, Coroutine, List, TypeVar

addonmanager: Any
asyncio: module
command: Any
contextlib: module
core: Any
eventsequence: Any
mitmproxy: Any
script: Any
sys: module

_Tcontext = TypeVar('_Tcontext', bound=context)

class RecordingMaster(Any):
    addons: TestAddons
    logs: List[nothing]
    def __init__(self, *args, **kwargs) -> None: ...
    def await_log(self, txt, level = ...) -> Coroutine[Any, Any, bool]: ...
    def clear(self) -> None: ...
    def dump_log(self, outf = ...) -> None: ...
    def has_log(self, txt, level = ...) -> bool: ...

class TestAddons(Any):
    def __init__(self, master) -> None: ...
    def trigger(self, event, *args, **kwargs) -> None: ...

class context:
    __doc__: str
    cycle: Callable[..., contextlib._GeneratorContextManager]
    master: RecordingMaster
    options: Any
    def __enter__(self: _Tcontext) -> _Tcontext: ...
    def __exit__(self, exc_type, exc_value, traceback) -> bool: ...
    def __init__(self, *addons, options = ..., loadcore = ...) -> None: ...
    def command(self, func, *args) -> Any: ...
    def configure(self, addon, **kwargs) -> None: ...
    def invoke(self, addon, event, *args, **kwargs) -> Any: ...
    def script(self, path) -> Any: ...