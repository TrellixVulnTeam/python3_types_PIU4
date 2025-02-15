# (generated with --quick)

import meeseeksdev.meeseeksbox.utils
from typing import Any, Callable, Generator, Type, TypeVar

Session: Type[meeseeksdev.meeseeksbox.utils.Session]
tag: Any
untag: Any

_T0 = TypeVar('_T0')

def _format_doc(function, name) -> str: ...
def admin(function: _T0) -> _T0: ...
def close(*, session, payload, arguments, local_config = ...) -> None: ...
def dedent(text: str) -> str: ...
def everyone(function: _T0) -> _T0: ...
def fix_comment_body(body, original_poster, original_url, original_org, original_repo) -> str: ...
def fix_issue_body(body, original_poster, original_repo, original_org, original_number, migration_requester) -> str: ...
def help_make(commands) -> Callable[[], Any]: ...
def merge(*, session, payload, arguments, method = ..., local_config = ...) -> None: ...
def migrate_issue_request(*, session: meeseeksdev.meeseeksbox.utils.Session, payload: dict, arguments: str, local_config = ...) -> Generator[str, Any, None]: ...
def open(*, session, payload, arguments, local_config = ...) -> None: ...
def pr_author(function: _T0) -> _T0: ...
def ready(*, session, payload, arguments, local_config = ...) -> None: ...
def write(function: _T0) -> _T0: ...
