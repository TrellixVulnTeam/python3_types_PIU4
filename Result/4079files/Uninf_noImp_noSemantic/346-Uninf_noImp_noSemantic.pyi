from nougat import Nougat
from typing import Any

class TestSignal:
    async def test_signal(self, app: Nougat) -> Any: ...
    async def test_before_start_signal(self, app: Nougat, port: int) -> Any: ...
    async def test_after_start_signal(self, app: Nougat, port: int) -> Any: ...
    async def test_signals(self, app: Nougat, port: int) -> Any: ...
    async def test_multiple_signal_sender(self, app: Nougat, port: int) -> Any: ...
    async def test_sync_signal_sender(self, app: Nougat, port: int) -> Any: ...
