import unittest
from typing import Any

class ChdirTests(unittest.TestCase):
    orig_cwd: Any = ...
    dst_dir: str = ...
    def setUp(self) -> None: ...
    def test_os_chdir_is_called_with_dst_dir_in_entry(self, mock_chdir: Any) -> None: ...
    def test_os_chdir_is_called_with_orig_cwd_in_exit(self, mock_chdir: Any) -> None: ...
    def test_os_chdir_is_called_with_orig_cwd_in_exit_even_if_exception_occurs(self, mock_chdir: Any) -> None: ...
