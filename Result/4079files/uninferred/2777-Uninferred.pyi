from objp.util import pyref as pyref
from typing import Any

class PyMain:
    callback: Any = ...
    def __init__(self, callback: pyref) -> None: ...
    def hello_(self, name: str) -> Any: ...