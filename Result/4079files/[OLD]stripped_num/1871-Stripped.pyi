# (generated with --quick)

from typing import Any, AsyncGenerator, List, Tuple, Union

API_BASE: str
ChandereError: Any
FIELD_NAMES: List[str]
RES_BASE: str
__author__: str
__licence__: str
__version__: str
aiohttp: Any
check_http_status: Any
contains_uri_scheme: Any
html: module
parse_crosslink: Any
parse_imageboard_uri_factory: Any
parse_uri: Any

def _catalog_url(board) -> str: ...
def _collect_files_board(board) -> AsyncGenerator[Tuple[Any, Any], Any]: ...
def _collect_files_thread(board, thread) -> AsyncGenerator[Tuple[Any, str], Any]: ...
def _collect_posts_board(board) -> asyncgenerator: ...
def _collect_posts_thread(board, thread) -> asyncgenerator: ...
def _collect_threads(board) -> asyncgenerator: ...
def _file_url(board, tim, ext) -> str: ...
def _thread_url(board, thread) -> str: ...
def _threads_from_page(page) -> List[int]: ...
def _tidy_post_fields(post) -> None: ...
def collect_files(target) -> asyncgenerator: ...
def collect_posts(target) -> asyncgenerator: ...
def parse_target(target) -> Tuple[Any, Any]: ...
@overload
def quote(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
