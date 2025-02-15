from .panel import Panel
from PyQt5.QtWidgets import QWidget as QWidget
from typing import Any, Optional

class ExperimentsPanel(Panel):
    _network: Any = ...
    _layer: Any = ...
    _data: Any = ...
    def __init__(self, parent: Optional[Any] = ...) -> None: ...
    matrix_view: Any = ...
    connections_view: Any = ...
    def initUI(self) -> None: ...
    def setNetwork(self, network: Any=...) -> None: ...
    def setLayer(self, layer: Any=...) -> None: ...
    def setInputData(self, data: Optional[Any] = ...) -> None: ...
    def updateActivation(self) -> None: ...
