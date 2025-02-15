from typing import Any, Optional
from unittest import TestCase

class ExtendedTestCase(TestCase):
    def assertLemmatisationEqual(self, origin: Any, result: Any, message: Optional[Any] = ..., _lemma_obj: bool = ...): ...
    def assertLemmatisationMultipleEqual(self, origin: Any, result: Any, message: Optional[Any] = ..., _lemma_obj: bool = ...): ...
