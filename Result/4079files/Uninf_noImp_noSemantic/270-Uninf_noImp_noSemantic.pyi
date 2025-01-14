from django.test import TestCase
from typing import Any

class TestAcmeChallenge(TestCase):
    def test_acme_url(self) -> None: ...
    def test_acme_url_no_reverse_match(self) -> None: ...
    def test_challenge(self) -> None: ...
    def test_response(self) -> None: ...
    def test_str(self) -> None: ...

class TestAcmeChallengeViews(TestCase):
    factory: Any = ...
    detail_url: str = ...
    expected_challenge: str = ...
    expected_response: str = ...
    expected_response_bytes: bytes = ...
    expected_response_decode: str = ...
    test_challenge: Any = ...
    def setUp(self) -> None: ...
    def test_detail(self) -> None: ...
    def test_detail_404(self) -> None: ...
