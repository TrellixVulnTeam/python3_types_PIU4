import marshmallow as ma
from typing import Any, Optional

hello_args: Any
hello_multiple: Any

class HelloSchema(ma.Schema):
    name: Any = ...

strict_kwargs: Any
hello_many_schema: Any

def echo(request: Any): ...
def echo_query(request: Any): ...
def echo_use_args(request: Any, args: Any): ...
def echo_use_args_validated(request: Any, args: Any): ...
def echo_use_kwargs(request: Any, name: Any): ...
def echo_multi(request: Any): ...
def echo_many_schema(request: Any): ...
def echo_use_args_with_path_param(request: Any, args: Any): ...
def echo_use_kwargs_with_path_param(request: Any, value: Any): ...
def always_error(request: Any): ...
def echo_headers(request: Any): ...
def echo_cookie(request: Any): ...
def echo_file(request: Any): ...
def echo_nested(request: Any): ...
def echo_nested_many(request: Any): ...
def echo_matchdict(request: Any): ...

class EchoCallable:
    request: Any = ...
    def __init__(self, request: Any) -> None: ...
    def __call__(self, args: Any): ...

def add_route(config: Any, route: Any, view: Any, route_name: Optional[Any] = ..., renderer: str = ...) -> None: ...
def create_app(): ...
