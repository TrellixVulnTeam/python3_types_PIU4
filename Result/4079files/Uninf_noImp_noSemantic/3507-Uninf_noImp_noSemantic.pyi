from typing import Any

class Frame:
    def __init__(self, locals_: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...

class RegularFrame(Frame):
    TYPE_BYTE: bytes = ...
    def to_bytes(self): ...
    @classmethod
    def from_byte(cls, buffer: Any): ...

class PaddingFrame(RegularFrame):
    TYPE_BYTE: bytes = ...

class ResetStreamFrame(RegularFrame):
    TYPE_BYTE: bytes = ...
    def __init__(self, stream_id: Any, offset: Any, error: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class ConnectionCloseFrame(RegularFrame):
    TYPE_BYTE: bytes = ...
    def __init__(self, error: Any, reason: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class GoAwayFrame(RegularFrame):
    TYPE_BYTE: bytes = ...
    def __init__(self, largest_client_stream_id: Any, largest_server_stream_id: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class MaxDataFrame(Frame):
    TYPE_BYTE: bytes = ...
    def __init__(self, max_data: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class MaxStreamDataFrame(Frame):
    TYPE_BYTE: bytes = ...
    stream_id: Any = ...
    offset: Any = ...
    def __init__(self, stream_id: Any, offset: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class MaxStreamIDFrame(Frame):
    TYPE_BYTE: bytes = ...
    def __init__(self, max_stream_id: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class PingFrame(RegularFrame):
    TYPE_BYTE: bytes = ...

class BlockedFrame(Frame):
    TYPE_BYTE: bytes = ...
    stream_id: Any = ...
    def __init__(self, stream_id: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class StreamBlockedFrame(Frame):
    TYPE_BYTE: bytes = ...
    def __init__(self, stream_id: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class StreamIDNeededFrame(RegularFrame):
    TYPE_BYTE: bytes = ...

class NewConnectionIDFrame(Frame):
    TYPE_BYTE: bytes = ...
    def __init__(self, sequence: Any, connection_id: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class StreamFrame(Frame):
    stream_id: Any = ...
    offset: Any = ...
    fin: Any = ...
    payload: Any = ...
    def __init__(self, stream_id: Any, offset: Any, fin: Any, payload: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def _get_sream_id_length(self): ...
    def _get_offset_length(self): ...
    def to_bytes(self): ...

class AckFrame(Frame):
    def __init__(self, largest_acknowledged: Any, ack_delay: Any, ack_blocks: Any, timestapms: Any) -> None: ...
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self): ...

class QUICPacket:
    @classmethod
    def from_bytes(cls, buffer: Any): ...
    def to_bytes(self) -> None: ...

class LongHeaderPacket(QUICPacket): ...
class ShortHeaderPacket(QUICPacket): ...
