# (generated with --quick)

from typing import Any, Callable, Dict, List, Optional, Sequence, Set

Contexts: Set[str]
command: Any
commandexecutor: Any
ctx: Any
exceptions: Any
keyAttrs: Dict[str, Callable[[Any], Any]]
mitmproxy: Any
navkeys: List[str]
os: module
requiredKeyAttrs: Set[str]
ruamel: Any
signals: Any
typing: module

class Binding:
    command: Any
    contexts: list
    help: Any
    key: Any
    def __init__(self, key, command, contexts, help) -> None: ...
    def keyspec(self) -> Any: ...
    def sortkey(self) -> Any: ...

class KeyBindingError(Exception): ...

class Keymap:
    bindings: Any
    executor: Any
    keys: Dict[str, Dict[Any, Binding]]
    def __init__(self, master) -> None: ...
    def _check_contexts(self, contexts) -> None: ...
    def add(self, key: str, command: str, contexts: Sequence[str], help = ...) -> None: ...
    def bind(self, binding: Binding) -> None: ...
    def get(self, context: str, key: str) -> Optional[Binding]: ...
    def handle(self, context: str, key: str) -> Optional[str]: ...
    def handle_only(self, context: str, key: str) -> Optional[str]: ...
    def list(self, context: str) -> Sequence[Binding]: ...
    def remove(self, key: str, contexts: Sequence[str]) -> None: ...
    def unbind(self, binding: Binding) -> None: ...

class KeymapConfig:
    defaultFile: str
    keymap_load_path: Any
    def load_path(self, km, p) -> None: ...
    def parse(self, text) -> Any: ...
    def running(self) -> None: ...
