from gui.contextMenu import ContextMenuCombined
from typing import Any

class RemoveItem(ContextMenuCombined):
    mainFrame: Any = ...
    def __init__(self) -> None: ...
    srcContext: Any = ...
    def display(self, callingWindow: Any, srcContext: Any, mainItem: Any, selection: Any): ...
    def getText(self, callingWindow: Any, itmContext: Any, mainItem: Any, selection: Any): ...
    def activate(self, callingWindow: Any, fullContext: Any, mainItem: Any, selection: Any, i: Any) -> None: ...
    def __handleModule(self, callingWindow: Any, mainItem: Any, selection: Any) -> None: ...
    def __handleDrone(self, callingWindow: Any, mainItem: Any, selection: Any) -> None: ...
    def __handleFighter(self, callingWindow: Any, mainItem: Any, selection: Any) -> None: ...
    def __handleImplant(self, callingWindow: Any, mainItem: Any, selection: Any) -> None: ...
    def __handleBooster(self, callingWindow: Any, mainItem: Any, selection: Any) -> None: ...
    def __handleCargo(self, callingWindow: Any, mainItem: Any, selection: Any) -> None: ...
    def __handleProjectedItem(self, callingWindow: Any, mainItem: Any, selection: Any) -> None: ...
    def __handleCommandFit(self, callingWindow: Any, mainItem: Any, selection: Any) -> None: ...
    def __handleGraphItem(self, callingWindow: Any, mainItem: Any, selection: Any) -> None: ...
