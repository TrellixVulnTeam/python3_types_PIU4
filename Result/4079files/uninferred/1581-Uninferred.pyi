from typing import Any

class TestNohupLocal:
    def read_file(self, filename: Any): ...
    def test_slow(self) -> None: ...
    def test_append(self) -> None: ...
    def test_redir(self) -> None: ...
    def test_closed_filehandles(self) -> None: ...
