# (generated with --quick)

from typing import Any, Optional

DEFAULT_CONFIG: Any
DEFAULT_ENV: Any
DEFAULT_TENANT: Any
__version__: str
apansible: module
apyaml: module
fire: Any
json: module
os: module
tools: module
utils: module

class AppFlow(object):
    __doc__: str
    def add(self, file, key, value) -> None: ...
    def checkin(self, tenant = ..., env = ..., commit = ...) -> None: ...
    def checkout(self, tenant = ..., env = ...) -> None: ...
    def decrypt(self, tenant = ..., env = ...) -> None: ...
    def encrypt(self, tenant = ..., env = ...) -> None: ...
    def get(self, file, key = ...) -> None: ...
    def init(self, tenant = ..., env = ...) -> None: ...
    def provision(self, tenant = ..., env = ..., limit: Optional[str] = ..., tags: Optional[str] = ..., skip_tags: Optional[str] = ..., firstrun: bool = ..., local: bool = ..., debug: bool = ...) -> None: ...
    def reset(self, tenant = ..., env = ...) -> None: ...
    def rm(self, file, key) -> None: ...
    def set(self, file, key, value) -> None: ...
    def ssh(self, tenant = ..., env = ...) -> None: ...
    def status(self, tenant = ..., env = ...) -> None: ...
    def tags(self, tenant = ..., env = ...) -> None: ...
    def update(self, branch = ...) -> None: ...
    def version(self) -> None: ...
    def vhosts(self, tenant = ...) -> None: ...
