# (generated with --quick)

import array
import decimal
import enum
import io
import mmap
import struct
import time
from typing import Any, Generator, List, Tuple, Type, Union

_Frame = Tuple[int, FrameType, Any]

BytesIO: Type[io.BytesIO]
Content: Any
Decimal: Type[decimal.Decimal]
Enum: Type[enum.Enum]
Method: Any
__all__: List[str]
datetime: Type[datetime.datetime]
error: Type[struct.error]

class FrameType(enum.Enum):
    CONTENT_BODY: int
    CONTENT_HEADER: int
    HEARTBEAT: int
    METHOD: int

class IncompleteData(Exception):
    __doc__: str

def _dump_frame(frame_type, channel_id, data) -> Any: ...
def _dump_item(value, _pack = ...) -> Any: ...
def _load_item(stream, _unpack = ...) -> Any: ...
def _parse_frame(stream, _unpack = ...) -> Tuple[Any, FrameType, Any]: ...
def _read(stream, length) -> Any: ...
def dump(fmt, *values, _pack = ...) -> bytearray: ...
def dump_frame_content(channel_id, content, max_frame_size) -> bytes: ...
def dump_frame_heartbeat(channel_id) -> Any: ...
def dump_frame_method(channel_id, method) -> Any: ...
def dump_protocol_header(major, minor, revision) -> bytes: ...
def load(fmt, stream, _unpack = ...) -> list: ...
def pack(fmt: Union[bytes, str], *v) -> bytes: ...
def parse_frames(stream) -> Generator[Tuple[Any, FrameType, Any], Any, None]: ...
def parse_protocol_header(stream) -> list: ...
def timegm(tuple: Union[time.struct_time, Tuple[int, ...]]) -> int: ...
def unpack(fmt: Union[bytes, str], buffer: Union[bytearray, bytes, memoryview, mmap.mmap, array.array[int]]) -> tuple: ...
