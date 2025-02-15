# (generated with --quick)

from typing import Any, Dict, TypeVar, Union

EVENTS_LOG_EVENT_WEIGHTS: Dict[str, int]
EVENTS_LOG_SIZE_DEFAULT: int
EVENT_TYPE_CHAINED_TO: str
EVENT_TYPE_CLOSE: str
EVENT_TYPE_COMMENT: str
EVENT_TYPE_OPEN: str
EVENT_TYPE_SHOW: str
EVENT_TYPE_SLUG: str
EVENT_TYPE_TAGGED: str
datetime: module
issue: Any
json: module
os: module
typing: module

_T0 = TypeVar('_T0')

def _bug_event_without_assigned_weight(event) -> None: ...
def append_event(issue_uid: str, event_type: str, parameters: dict = ...) -> None: ...
def append_event_chained_to(issue_uid: str, chained_to_these_issues: list) -> None: ...
def append_event_close(issue_uid: str) -> None: ...
def append_event_open(issue_uid: str, message: str) -> None: ...
def append_event_show(issue_uid) -> None: ...
def append_event_slug(issue_uid: str, slug: str) -> None: ...
def append_event_tagged(issue_uid: str, tags: list) -> None: ...
def read() -> list: ...
def rfind_if(seq, pred) -> int: ...
def sort(events_log) -> list: ...
def squash_events_log(events_log: _T0, aggressive = ...) -> Union[list, _T0]: ...
def squash_events_log_aggressive_1(events_log: _T0) -> Union[list, _T0]: ...
def squash_events_log_aggressive_2(events_log: _T0) -> Union[list, _T0]: ...
def timestamp(dt = ...) -> Any: ...
def write(events_log: list) -> None: ...
