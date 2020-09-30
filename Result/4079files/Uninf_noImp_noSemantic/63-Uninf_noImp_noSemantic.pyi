import flask
from flask_restful import Api as FlaskRestfulApi
from injector import Binder, Injector, Module, Provider, Scope
from typing import Any, Callable, Dict, Iterable, List, TypeVar, Union
from werkzeug.local import LocalManager, LocalProxy

__author__: str
__version__: str
__all__: Any
T = TypeVar('T', LocalProxy, Callable)

def instance_method_wrapper(im: T) -> T: ...
def wrap_fun(fun: T, injector: Injector) -> T: ...
def wrap_function(fun: Callable, injector: Injector) -> Callable: ...
def wrap_class_based_view(fun: Callable, injector: Injector) -> Callable: ...
def wrap_flask_restful_resource(fun: Callable, flask_restful_api: FlaskRestfulApi, injector: Injector) -> Callable: ...

class CachedProviderWrapper(Provider):
    _old_provider: Any = ...
    _cache: Any = ...
    def __init__(self, old_provider: Provider) -> None: ...
    def get(self, injector: Injector) -> Any: ...

class RequestScope(Scope):
    _local_manager: LocalManager = ...
    _locals: Any = ...
    def cleanup(self) -> None: ...
    def prepare(self) -> None: ...
    def configure(self) -> None: ...
    def get(self, key: Any, provider: Provider) -> Any: ...

request: Any
_ModuleT = Union[Callable[[Binder], Any], Module]

class FlaskInjector:
    injector: Any = ...
    app: Any = ...
    def __init__(self, app: flask.Flask, modules: Iterable[_ModuleT]=..., injector: Injector=..., request_scope_class: type=...) -> None: ...

def process_dict(d: Dict, injector: Injector) -> None: ...
def process_list(l: List, injector: Injector) -> None: ...

class FlaskModule(Module):
    app: Any = ...
    request_scope_class: Any = ...
    def __init__(self, app: flask.Flask, request_scope_class: type=...) -> None: ...
    def configure(self, binder: Binder) -> None: ...