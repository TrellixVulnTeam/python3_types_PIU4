# (generated with --quick)

import types
from typing import Any, Dict, Optional, Pattern, Tuple, Type, TypeVar, Union

AbstractServiceHandler: Any
Episode: Any
UnprocessedStream: Any
_episode_count_fix: Pattern[str]
_episode_name_correct: Pattern[str]
_slug_regex: Pattern[str]
datetime: Type[datetime.datetime]
re: module
timedelta: Type[datetime.timedelta]

_T0 = TypeVar('_T0')

class ServiceHandler(Any):
    _backup_rss: str
    _episode_rss: str
    _season_url: str
    _show_re: Pattern[str]
    _show_url: str
    _title_fix: Pattern[str]
    def __init__(self) -> None: ...
    def _get_feed_episodes(self, show_key, **kwargs) -> Any: ...
    @classmethod
    def _get_feed_url(cls, show_key) -> Any: ...
    def _get_stream_info(self, show_key) -> Tuple[int, int]: ...
    def extract_show_key(self, url) -> Optional[str]: ...
    def get_all_episodes(self, stream, **kwargs) -> list: ...
    def get_seasonal_streams(self, **kwargs) -> list: ...
    def get_stream_info(self, stream: _T0, **kwargs) -> Optional[_T0]: ...
    def get_stream_link(self, stream) -> str: ...

def _digest_episode(feed_episode) -> Any: ...
def _get_slug(episode_link) -> Optional[str]: ...
def _is_valid_episode(feed_episode, show_id) -> bool: ...
def _verify_feed(feed) -> bool: ...
def debug(msg, *args, exc_info: Union[BaseException, bool, Tuple[Optional[type], Optional[BaseException], Optional[types.TracebackType]]] = ..., stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ..., **kwargs) -> None: ...
def error(msg, *args, exc_info: Union[BaseException, bool, Tuple[Optional[type], Optional[BaseException], Optional[types.TracebackType]]] = ..., stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ..., **kwargs) -> None: ...
def exception(msg, *args, exc_info: Union[BaseException, bool, Tuple[Optional[type], Optional[BaseException], Optional[types.TracebackType]]] = ..., stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ..., **kwargs) -> None: ...
def info(msg, *args, exc_info: Union[BaseException, bool, Tuple[Optional[type], Optional[BaseException], Optional[types.TracebackType]]] = ..., stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ..., **kwargs) -> None: ...
def warning(msg, *args, exc_info: Union[BaseException, bool, Tuple[Optional[type], Optional[BaseException], Optional[types.TracebackType]]] = ..., stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ..., **kwargs) -> None: ...
