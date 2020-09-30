# (generated with --quick)

import io
from typing import Any, Type
import unittest.case
import unittest.mock

ConfigurationFile: Any
StringIO: Type[io.StringIO]
TestCase: Type[unittest.case.TestCase]
helper: Any
patch: unittest.mock._patcher

class TestConfigurationFile(unittest.case.TestCase):
    def test_can_save_password_username_defaults_false(self) -> None: ...
    def test_can_save_password_username_defaults_true(self) -> None: ...
    def test_can_save_password_username_false(self) -> None: ...
    def test_can_save_password_username_inherit_false(self) -> None: ...
    def test_can_save_password_username_inherit_true(self) -> None: ...
    def test_can_save_password_username_true(self) -> None: ...
    def test_can_save_password_username_xor_1(self) -> None: ...
    def test_can_save_password_username_xor_2(self) -> None: ...
    def test_has_defaults(self) -> None: ...
    def test_initialise(self) -> None: ...
    def test_is_initialised(self) -> None: ...
    def test_section_get(self) -> None: ...
    def test_section_get_fallback(self) -> None: ...
    def test_supports_default(self) -> None: ...