from typing import Any

def require_json(req: Any, resp: Any, resource: Any, params: Any) -> None: ...
def parse_json(req: Any, resp: Any, resource: Any, params: Any) -> None: ...
def validate_json(req: Any, resp: Any, resource: Any, params: Any) -> None: ...
def dump_json(req: Any, resp: Any, resource: Any) -> None: ...