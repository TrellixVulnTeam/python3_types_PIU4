from typing import Any

async def test_send_message(cli: Any, tmpdir: Any, worker: Any) -> None: ...
async def test_send_message_usa(cli: Any, settings: Any, tmpdir: Any, worker: Any) -> None: ...
async def test_validate_number(cli: Any, tmpdir: Any) -> None: ...
async def test_repeat_uuid(cli: Any, tmpdir: Any, worker: Any) -> None: ...
async def test_invalid_number(cli: Any, tmpdir: Any, worker: Any) -> None: ...
async def test_exceed_cost_limit(cli: Any, tmpdir: Any, worker: Any) -> None: ...
async def test_send_messagebird(cli: Any, tmpdir: Any, dummy_server: Any, worker: Any) -> None: ...
async def test_messagebird_no_hlr(cli: Any, tmpdir: Any, dummy_server: Any, worker: Any) -> None: ...
async def test_messagebird_no_network(cli: Any, tmpdir: Any, dummy_server: Any, worker: Any) -> None: ...
async def test_messagebird_webhook(cli: Any, db_conn: Any, dummy_server: Any, worker: Any) -> None: ...
async def test_failed_render(cli: Any, tmpdir: Any, db_conn: Any, worker: Any) -> None: ...
async def test_link_shortening(cli: Any, tmpdir: Any, db_conn: Any, worker: Any) -> None: ...
async def test_send_multi_part(cli: Any, tmpdir: Any, worker: Any) -> None: ...
async def test_send_too_long(cli: Any, tmpdir: Any) -> None: ...
