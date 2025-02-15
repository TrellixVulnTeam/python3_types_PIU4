# (generated with --quick)

import collections
from typing import Any, Callable, Dict, List, NoReturn, Optional, Type, Union

HAS_SSLCONTEXT: bool
__logger: logging.Logger
base64: module
default_log_handler: logging.StreamHandler
deque: Type[collections.deque]
hashlib: module
json: module
logging: module
re: module
socket: module
ssl: module
string: module
sys: module
urllib2: Any

class APITimeout(ZabbixAPIException): ...

class Already_Exists(ZabbixAPIException): ...

class InvalidProtoError(ZabbixAPIException):
    __doc__: str

class ZabbixAPI(object):
    __password__: Any
    __username__: Any
    auth: Any
    httppasswd: Any
    httpuser: Any
    id: int
    kwargs: Dict[str, Any]
    logger: logging.Logger
    method: None
    params: None
    proto: Any
    r_query: collections.deque[str]
    server: Any
    timeout: Any
    url: Any
    validate_certs: Any
    def __checkauth__(self) -> NoReturn: ...
    def __getattr__(self, name) -> ZabbixAPISubClass: ...
    def __init__(self, server = ..., user = ..., passwd = ..., log_level = ..., timeout = ..., r_query_len = ..., validate_certs = ..., **kwargs) -> None: ...
    def _setuplogging(self) -> None: ...
    def api_version(self, **options) -> NoReturn: ...
    def debug(self, level, var = ..., msg = ...) -> None: ...
    def do_request(self, json_obj) -> Any: ...
    def json_obj(self, method, params = ..., auth = ...) -> str: ...
    def logged_in(self) -> bool: ...
    def login(self, user = ..., password = ..., save = ...) -> None: ...
    def recent_query(self) -> List[str]: ...
    def set_log_level(self, level) -> None: ...
    def test_login(self) -> bool: ...

class ZabbixAPIException(Exception):
    __doc__: str

class ZabbixAPISubClass(ZabbixAPI):
    __doc__: str
    data: Any
    logger: logging.Logger
    parent: Any
    def __checkauth__(self) -> None: ...
    def __getattr__(self, name) -> Callable: ...
    def __init__(self, parent, data, **kwargs) -> None: ...
    def do_request(self, req) -> Any: ...
    def json_obj(self, method, param) -> Any: ...
    def universal(self, method, opts) -> Any: ...

def _create_unverified_context(protocol: int = ..., *, cert_reqs: Optional[int] = ..., check_hostname: bool = ..., purpose = ..., certfile: Optional[str] = ..., keyfile: Optional[str] = ..., cafile: Optional[str] = ..., capath: Optional[str] = ..., cadata: Optional[Union[bytes, str]] = ...) -> ssl.SSLContext: ...
def checkauth(fn) -> Callable: ...
def dojson(fn) -> Callable[[Any, Any, Any], Any]: ...
