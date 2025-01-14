import enum
from collections import namedtuple
from typing import Any

class GameOptions:
    PredefinedOptions = namedtuple('PredefinedOptions', ['app_id', 'context_id'])
    STEAM: Any = ...
    DOTA2: Any = ...
    CS: Any = ...
    TF2: Any = ...
    PUBG: Any = ...
    app_id: Any = ...
    context_id: Any = ...
    def __init__(self, app_id: str, context_id: str) -> None: ...

class Asset:
    asset_id: Any = ...
    game: Any = ...
    amount: Any = ...
    def __init__(self, asset_id: str, game: GameOptions, amount: int=...) -> None: ...
    def to_dict(self): ...

class Currency(enum.IntEnum):
    USD: int = ...
    GBP: int = ...
    EURO: int = ...
    CHF: int = ...

class TradeOfferState(enum.IntEnum):
    Invalid: int = ...
    Active: int = ...
    Accepted: int = ...
    Countered: int = ...
    Expired: int = ...
    Canceled: int = ...
    Declined: int = ...
    InvalidItems: int = ...
    ConfirmationNeed: int = ...
    CanceledBySecondaryFactor: int = ...
    StateInEscrow: int = ...

class SteamUrl:
    API_URL: str = ...
    COMMUNITY_URL: str = ...
    STORE_URL: str = ...

class Endpoints:
    CHAT_LOGIN: Any = ...
    SEND_MESSAGE: Any = ...
    CHAT_LOGOUT: Any = ...
    CHAT_POLL: Any = ...
