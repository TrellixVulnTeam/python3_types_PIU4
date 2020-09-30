import unittest

__author__: str
__version__: str
__date__: str
__revision__: str
__license__: str

class TestEXIFHeader(unittest.TestCase):
    def test_hide_empty_message(self) -> None: ...
    def test_hide_and_reveal(self) -> None: ...
    def test_with_image_without_exif_data(self) -> None: ...
    def test_with_text_file(self) -> None: ...
    def test_with_png_image(self) -> None: ...
    def test_with_bytes(self) -> None: ...
    def tearDown(self) -> None: ...