from typing import Any
from unittest import TestCase

class TestSentimentAnalyser(TestCase):
    analyser: Any = ...
    def setUp(self) -> None: ...
    def test_get_sentiment(self) -> None: ...
