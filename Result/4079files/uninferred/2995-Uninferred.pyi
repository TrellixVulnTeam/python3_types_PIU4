from hypothesis import reproduce_failure as reproduce_failure, seed as seed
from typing import Any

class TestVersionStrategy:
    @staticmethod
    def _ver_2_list(version: Any): ...
    def test_greater_than_minimum(self, data: Any, min_version: Any) -> None: ...
    def test_less_than_maximum(self, data: Any, max_version: Any) -> None: ...
    def test_inbetween_min_and_max(self, data: Any, versions: Any) -> None: ...
    def test_produces_with_more_digits_than_min(self, data: Any, min_digits: Any) -> None: ...
    def test_produces_with_less_digits_than_max(self, data: Any, max_digits: Any) -> None: ...
    def test_produces_inbetween_min_and_max_digits(self, data: Any, digits: Any) -> None: ...
    def test_mixture(self, data: Any, versions: Any, digits: Any) -> None: ...
