from typing import Any

static_response: bytes

def make_class(flavor: Any): ...
async def handle_requests(queue: Any, transport: Any) -> None: ...
async def handle_request(request: Any, transport: Any) -> None: ...
def handle_request_block(request: Any, transport: Any, response: Any) -> None: ...
def handle_dump(request: Any, transport: Any, response: Any) -> None: ...
