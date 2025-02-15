# (generated with --quick)

import collections
from typing import Any, Type

CONFIG_KEY: Any
OrderedDict: Type[collections.OrderedDict]
Response: Any
app: Any
asyncio: module
client: Any
negotiation: Any
pytest: Any
test_renders_to_json_by_default: Any
web: Any

def add_routes(app) -> None: ...
def configure_app(app, overrides = ..., setup = ...) -> None: ...
def dummy_renderer(request, data) -> Any: ...
def test_configuration_through_app_key(app, client) -> None: ...
def test_nonordered_dict_of_renderers(app, client) -> None: ...
def test_renderer_no_nego(app, client) -> None: ...
def test_renderer_override(app, client) -> None: ...
def test_renderer_override_force(app, client) -> None: ...
def test_renderer_override_force_rendering(app, client) -> None: ...
def test_renderer_override_multiple_classes(app, client) -> None: ...
