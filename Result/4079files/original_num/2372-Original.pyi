# (generated with --quick)

from typing import Any, NoReturn, Tuple

address: str
logging: module
os: module
password: str
pika: Any
prom_client: Any
queue: str
sys: module
time: module
username: str

def attempt_decode(s) -> Any: ...
def receive(channel, expected) -> None: ...
def run_test() -> NoReturn: ...
def send(channel, message) -> None: ...
def setup_client() -> Any: ...
def with_metrics(f, valid = ...) -> Any: ...
def with_metrics_or_fail(f, valid = ...) -> Tuple[Any, Any]: ...
