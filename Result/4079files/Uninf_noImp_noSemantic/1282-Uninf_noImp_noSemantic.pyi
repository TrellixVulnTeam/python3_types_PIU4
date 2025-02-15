from typing import Any

class MilitaryInfo:
    path: str = ...
    servers: Any = ...
    def __init__(self) -> None: ...
    def setData(self, serverId: Any, key: Any, value: Any) -> None: ...
    def load(self) -> None: ...
    def save(self) -> None: ...

class Military:
    startDate: Any = ...
    def __init__(self, startDate: Any) -> None: ...
    def getStartDate(self): ...
    def getDischargeDate(self): ...
    def getEmojiSet(self): ...
    def getSymbol(self): ...
    def encode(self): ...

class Airforce(Military):
    def getDischargeDate(self): ...
    def getEmojiSet(self): ...
    def getSymbol(self): ...
    def encode(self): ...

class PublicService(Military):
    def getEmojiSet(self): ...
    def encode(self): ...
