# (generated with --quick)

from typing import Any, Optional, TypeVar

DCOSHTTPException: Any
credentials: Any
dcos_user: Any
http: Any
new_dcos_user: Any
no_user: Any
pytest: Any

AnyStr = TypeVar('AnyStr', str, bytes)

def __getattr__(name) -> Any: ...
def _acl_url() -> str: ...
def add_group(id, description = ...) -> None: ...
def add_user(uid, password, desc = ...) -> None: ...
def add_user_to_group(uid, gid, exist_ok = ...) -> None: ...
def ensure_resource(rid) -> None: ...
def get_group(id) -> Any: ...
def get_user(uid) -> Any: ...
def remove_group(id) -> None: ...
def remove_user(uid) -> None: ...
def remove_user_from_group(uid, gid) -> None: ...
def remove_user_permission(rid, uid, action = ...) -> None: ...
def set_user_permission(rid, uid, action = ...) -> None: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
