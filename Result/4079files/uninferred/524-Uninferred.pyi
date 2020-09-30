import unittest
from typing import Any

TEEKA_SETTINGS: Any
CURREN_DIR: Any

class TestStringMethods(unittest.TestCase):
    settings_file: Any = ...
    settings_parser_instance: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def test_port(self) -> None: ...
    def test_ip(self) -> None: ...
    def test_data_path(self) -> None: ...
    def test_meta_store_engine(self) -> None: ...
    def test_meta_store_name(self) -> None: ...