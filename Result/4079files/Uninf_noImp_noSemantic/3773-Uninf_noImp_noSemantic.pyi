import unittest
from typing import Any

class TestConfig(unittest.TestCase):
    configFilePath: Any = ...
    def setUp(self) -> None: ...
    def test_class_method_generation(self) -> None: ...
    def test_file_not_found(self) -> None: ...
    def test_cannot_load_again(self) -> None: ...
    def test_empty_config(self) -> None: ...
    def test_invalid_yaml(self) -> None: ...
    def _write_config(self, config: Any) -> None: ...
    def tearDown(self) -> None: ...
