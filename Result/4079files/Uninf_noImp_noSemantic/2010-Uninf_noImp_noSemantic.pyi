import unittest
from typing import Any

config: Any

def async_test(f: Any): ...

class AsyncTester(unittest.TestCase):
    @staticmethod
    def _do_async_code(coro: Any): ...
    running_loop: Any = ...
    time_track_stack: Any = ...
    def setUp(self, *args: Any, **kwargs: Any) -> None: ...
    def tearDown(self, *args: Any, **kwargs: Any) -> None: ...
    def time_track(self, text: object=...) -> Any: ...

class Tester(AsyncTester):
    executed_requests: int = ...
    def setUp(self, *args: Any, **kwargs: Any) -> None: ...
    async def do_multiple(self, func: Any, times: int=..., text: str=...) -> Any: ...
    async def test_data_endpoints(self) -> None: ...
    async def test_player_search(self) -> None: ...
    async def test_player_endpoints(self) -> None: ...
    async def test_platforms_throughput(self) -> None: ...
    async def test_tiers_throughput(self) -> None: ...
    async def test_seasons_throughput(self) -> None: ...
    async def test_playlists_throughput(self) -> None: ...