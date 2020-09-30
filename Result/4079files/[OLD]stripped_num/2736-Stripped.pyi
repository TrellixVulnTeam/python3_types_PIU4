# (generated with --quick)

import types
from typing import Any, Dict, Optional, Tuple, Union

_config: Any
_r: Any
praw: Any

def _connect_reddit() -> Any: ...
def _ensure_connection() -> bool: ...
def debug(msg, *args, exc_info: Union[BaseException, bool, Tuple[Optional[type], Optional[BaseException], Optional[types.TracebackType]]] = ..., stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ..., **kwargs) -> None: ...
def error(msg, *args, exc_info: Union[BaseException, bool, Tuple[Optional[type], Optional[BaseException], Optional[types.TracebackType]]] = ..., stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ..., **kwargs) -> None: ...
def exception(msg, *args, exc_info: Union[BaseException, bool, Tuple[Optional[type], Optional[BaseException], Optional[types.TracebackType]]] = ..., stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ..., **kwargs) -> None: ...
def get_shortlink_from_id(id) -> str: ...
def info(msg, *args, exc_info: Union[BaseException, bool, Tuple[Optional[type], Optional[BaseException], Optional[types.TracebackType]]] = ..., stack_info: bool = ..., extra: Optional[Dict[str, Any]] = ..., **kwargs) -> None: ...
def init_reddit(config) -> None: ...
def submit_text_post(subreddit, title, body) -> Any: ...