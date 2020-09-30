# (generated with --quick)

import game.table
import optparse
import tenhou.decoder
from typing import Any, List, Tuple, Type, TypeVar, Union

Meld: Any
OptionParser: Type[optparse.OptionParser]
Table: Type[game.table.Table]
TenhouClient: Any
TenhouDecoder: Type[tenhou.decoder.TenhouDecoder]
TilesConverter: Any
logger: logging.Logger
logging: module
os: module
re: module
requests: module

_T0 = TypeVar('_T0')

class SocketMock(object):
    __doc__: str
    commands: list
    log_path: Any
    text: Any
    def __init__(self, log_path, log_content = ...) -> None: ...
    def _load_text(self) -> str: ...
    def _parse_text(self) -> None: ...
    def close(self) -> None: ...
    def connect(self, _) -> None: ...
    def recv(self, _) -> Any: ...
    def sendall(self, message) -> None: ...
    def shutdown(self, _) -> None: ...

class TenhouLogReproducer(object):
    __doc__: str
    decoder: tenhou.decoder.TenhouDecoder
    player_position: Any
    round_content: Any
    stop_tag: Any
    def __init__(self, log_url, stop_tag = ...) -> None: ...
    def _download_log_content(self, log_id) -> str: ...
    def _get_attribute_content(self, tag, attribute_name) -> Any: ...
    def _is_discard(self, tag) -> bool: ...
    def _is_draw(self, tag) -> bool: ...
    def _is_init_tag(self, tag: _T0) -> Union[bool, _T0]: ...
    def _normalize_position(self, who, from_who) -> Any: ...
    def _parse_rounds(self, log_content) -> List[list]: ...
    def _parse_tile(self, tag) -> int: ...
    def _parse_url(self, log_url) -> Tuple[Any, int, int]: ...
    def reproduce(self, dry_run = ...) -> None: ...

def main() -> None: ...
def parse_args_and_start_reproducer() -> None: ...
def set_up_logging(save_to_file = ...) -> None: ...