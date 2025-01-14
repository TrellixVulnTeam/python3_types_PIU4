from marshmallow import Schema
from typing import Any

class CommandArgumentSchema(Schema):
    value: Any = ...

class CommandResultSchema(Schema):
    result: Any = ...
    value: Any = ...

def make_command(graph: Any, ns: Any, request_schema: Any, response_schema: Any): ...

class TestCommand:
    graph: Any = ...
    ns: Any = ...
    client: Any = ...
    def setup(self): ...
    def test_url_for(self) -> None: ...
    def test_command(self) -> None: ...
    def test_swagger(self) -> None: ...
