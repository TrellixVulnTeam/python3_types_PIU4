from typing import Any

ECHO: int

def _debugEcho(self, message: Any, *args: Any, **kwargs: Any) -> Any: ...

logger: Any
format: Any
screen: Any

def read_config(ctx: Any, param: Any, value: Any): ...
def cli(ctx: Any, **kwargs: Any): ...
def pubyun(self, **kwargs: Any) -> None: ...
def duckdns(self, **kwargs: Any) -> None: ...
def main() -> None: ...
