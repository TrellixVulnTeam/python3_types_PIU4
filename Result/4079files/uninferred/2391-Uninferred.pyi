from typing import Any

_TEST_CURIO: Any
helper: Any
default_skt_ctx: Any

class OutputTestCase:
    async def test_html_escape(self) -> None: ...
    async def test_no_escape(self) -> None: ...
    async def test_json_escape(self) -> None: ...
    async def test_url_escape(self) -> None: ...
    async def test_url_without_plus_escape(self) -> None: ...
    async def test_custom_escape_fn(self) -> None: ...
