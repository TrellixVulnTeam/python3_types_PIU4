from typing import Any, Optional

password: Any
username: Any
address: Any
queue: str

def with_metrics(f: Any, valid: Optional[Any] = ...): ...
def with_metrics_or_fail(f: Any, valid: Optional[Any] = ...): ...
def setup_client(): ...
def send(channel: Any, message: Any): ...
def attempt_decode(s: Any): ...
def receive(channel: Any, expected: Any): ...
def run_test() -> None: ...
