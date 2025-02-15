import unittest
from typing import Any

def _default_mock_clients(region: Any, instances: Any = ..., quotas: Any = ...): ...

class TestCluster(unittest.TestCase):
    def test_failed_scale_up(self) -> None: ...
    def test_scale_up(self) -> None: ...
    def test_priority(self) -> None: ...
    def test_slow_scale_up(self) -> None: ...
    def test_tainted_scale_set(self) -> None: ...
    def test_out_of_quota(self) -> None: ...
    def test_near_quota_limit(self) -> None: ...
    def test_scale_in(self) -> None: ...
