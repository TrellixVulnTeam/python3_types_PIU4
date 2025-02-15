# (generated with --quick)

import collections
from typing import Any, Callable, Dict, Iterable, Sized, Tuple, Type, TypeVar, Union

constants: Any

_Tnamedtuple-Playlist-id-name-platform-population-last_updated = TypeVar('_Tnamedtuple-Playlist-id-name-platform-population-last_updated', bound=`namedtuple-Playlist-id-name-platform-population-last_updated`)
_Tnamedtuple-Season-id-is_current-time_started-time_ended = TypeVar('_Tnamedtuple-Season-id-is_current-time_started-time_ended', bound=`namedtuple-Season-id-is_current-time_started-time_ended`)
_Tnamedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier = TypeVar('_Tnamedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier', bound=`namedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier`)
_Tnamedtuple-Tier-id-name = TypeVar('_Tnamedtuple-Tier-id-name', bound=`namedtuple-Tier-id-name`)

class Player(object):
    __doc__: str
    avatar_url: Any
    display_name: Any
    platform: Any
    platform_id: Any
    profile_url: Any
    ranked_seasons: Any
    signature_url: Any
    stats: Any
    uid: Any
    def __init__(self, uid, display_name, platform, avatar_url = ..., profile_url = ..., signature_url = ..., stats = ..., ranked_seasons = ...) -> None: ...

class Playlist(`namedtuple-Playlist-id-name-platform-population-last_updated`):
    __doc__: str

class RankedSeason(dict):
    __doc__: str
    def __getitem__(self, item) -> Any: ...

class RankedSeasons(object):
    __doc__: str
    ranked_seasons: Dict[Any, RankedSeason]
    def __contains__(self, item) -> bool: ...
    def __getattr__(self, item) -> Any: ...
    def __getitem__(self, item) -> RankedSeason: ...
    def __init__(self, data) -> None: ...
    def __iter__(self) -> `dictionary-keyiterator`: ...
    def __len__(self) -> int: ...

class Season(`namedtuple-Season-id-is_current-time_started-time_ended`):
    __doc__: str

class SeasonPlaylistRank(`namedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier`): ...

class Tier(`namedtuple-Tier-id-name`):
    __doc__: str

class `namedtuple-Playlist-id-name-platform-population-last_updated`(tuple):
    __slots__ = ["id", "last_updated", "name", "platform", "population"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str]
    id: Any
    last_updated: Any
    name: Any
    platform: Any
    population: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Playlist-id-name-platform-population-last_updated`], id, name, platform, population, last_updated) -> `_Tnamedtuple-Playlist-id-name-platform-population-last_updated`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Playlist-id-name-platform-population-last_updated`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Playlist-id-name-platform-population-last_updated`: ...
    def _replace(self: `_Tnamedtuple-Playlist-id-name-platform-population-last_updated`, **kwds) -> `_Tnamedtuple-Playlist-id-name-platform-population-last_updated`: ...

class `namedtuple-Season-id-is_current-time_started-time_ended`(tuple):
    __slots__ = ["id", "is_current", "time_ended", "time_started"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str]
    id: Any
    is_current: Any
    time_ended: Any
    time_started: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Season-id-is_current-time_started-time_ended`], id, is_current, time_started, time_ended) -> `_Tnamedtuple-Season-id-is_current-time_started-time_ended`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Season-id-is_current-time_started-time_ended`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Season-id-is_current-time_started-time_ended`: ...
    def _replace(self: `_Tnamedtuple-Season-id-is_current-time_started-time_ended`, **kwds) -> `_Tnamedtuple-Season-id-is_current-time_started-time_ended`: ...

class `namedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier`(tuple):
    __slots__ = ["division", "matchesPlayed", "rankPoints", "tier"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str]
    division: Any
    matchesPlayed: Any
    rankPoints: Any
    tier: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier`], rankPoints, division, matchesPlayed, tier) -> `_Tnamedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier`: ...
    def _replace(self: `_Tnamedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier`, **kwds) -> `_Tnamedtuple-SeasonPlaylistRank-rankPoints-division-matchesPlayed-tier`: ...

class `namedtuple-Tier-id-name`(tuple):
    __slots__ = ["id", "name"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    id: Any
    name: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Tier-id-name`], id, name) -> `_Tnamedtuple-Tier-id-name`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Tier-id-name`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Tier-id-name`: ...
    def _replace(self: `_Tnamedtuple-Tier-id-name`, **kwds) -> `_Tnamedtuple-Tier-id-name`: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
