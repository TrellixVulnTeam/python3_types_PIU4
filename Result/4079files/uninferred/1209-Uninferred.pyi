from settings import *
from mixins import *
from abc import ABCMeta
from typing import Any, Dict, List

class Item(ReprMixin, DataFileMixin):
    EQUIPMENT: Any = ...
    ID: Any = ...
    name: Any = ...
    slot: Any = ...
    descriptions: Any = ...
    attack: Any = ...
    defence: Any = ...
    specialAttack: Any = ...
    stackable: Any = ...
    combinations: Any = ...
    combinations2: Any = ...
    metadata: Any = ...
    _count: Any = ...
    def __init__(self, id_num: int, **kwargs: Any) -> None: ...
    def __eq__(self, item: object) -> bool: ...
    def __lt__(self, item: object) -> bool: ...
    def __gt__(self, item: object) -> bool: ...
    @property
    def description(self): ...

class Container(ReprMixin):
    max_capacity: Any = ...
    name: Any = ...
    items: Any = ...
    def __init__(self, items: List=..., max_capacity: int=..., **kwargs: Any) -> None: ...
    def __len__(self) -> int: ...
    def append(self, item: Item) -> str: ...
    def remove(self, item: Item, count: int=...) -> str: ...

class Inventory(Container):
    GEAR_SLOTS: Any = ...
    gear: Any = ...
    def __init__(self, gear: Dict=..., items: List=..., **kwargs: Any) -> None: ...
    def equip(self, item: Item) -> str: ...
    def equip_from_index(self, item_index: int) -> str: ...
    def unequip(self, slot: str) -> str: ...
    def combine_item(self, *items: Any): ...
    def better_combine_item(self, base_item: Item, combination: int, *materials: Any) -> str: ...

class Character(ReprMixin, LevelMixin, SpritesMixin, metaclass=ABCMeta):
    name: Any = ...
    inventory: Any = ...
    def __init__(self, name: Any, inventory: Inventory=..., **kwargs: Any) -> None: ...

class Player(Character):
    def __init__(self, name: Any, inventory: Inventory=..., **kwargs: Any) -> None: ...
