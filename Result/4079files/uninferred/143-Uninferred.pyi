import unittest

class TestDQNTrainer(unittest.TestCase):
    MODEL_PATH: str = ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def test_trainer(self) -> None: ...
