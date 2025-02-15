from pydotnet.core.io import *
from pydotnet.clr.CLRMessage import CLRMessage
from typing import Any

class CLRObjectRefArray(CLRMessage):
    def __init__(self, v: Any = ...) -> None: ...
    def serialize(self, sock: BinarySocketWriter) -> Any: ...
    value: Any = ...
    def deserialize(self, sock: BinarySocketReader) -> Any: ...
