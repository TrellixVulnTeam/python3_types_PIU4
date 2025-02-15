from mpf.tests.MpfTestCase import MpfTestCase
from typing import Any

class MpfDocsTestCase(MpfTestCase):
    rst_target: str = ...
    _temp_machine_folder: Any = ...
    def __init__(self, methodName: str = ...) -> None: ...
    def setUp(self) -> None: ...
    def getOptions(self): ...
    def tearDown(self) -> None: ...
    def getConfigFile(self): ...
    def getMachinePath(self): ...
    def create_temp_config_files(self) -> None: ...
