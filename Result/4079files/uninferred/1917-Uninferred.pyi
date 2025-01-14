from core.models import *
from typing import Any

class Auction(models.Model):
    begin: Any = ...
    end: Any = ...
    var_entity: Any = ...
    var_min: Any = ...
    var_step: Any = ...
    commited: Any = ...
    buyer: Any = ...
    status_text: Any = ...
    @property
    def concrete_auction(self): ...
    def is_active(self): ...
    @property
    def ordered_bids(self): ...
    @property
    def effective_offer(self): ...
    @property
    def highest_bid(self): ...
    def __str__(self): ...
    def minimum_bid(self): ...
    def place_bid(self, team: Any, amount: Any) -> None: ...
    def _commit_seller(self, t: Transaction, var_amount: Any) -> Any: ...
    def _commit_buyer(self, t: Transaction, var_amount: Any) -> Any: ...
    def commit(self) -> None: ...
    @property
    def sells(self): ...
    @property
    def visible_sells(self): ...
    @property
    def wants(self): ...
    @property
    def visible_wants(self): ...
    def add_item(self, entity: Entity, amount: Any, *args: Any, **kwargs: Any) -> Any: ...
    def formatted_status(self, seller_name: Any): ...

class AuctionException(Exception): ...

class WhiteAuction(Auction):
    seller: Any = ...
    description: Any = ...
    def __str__(self): ...
    def is_white(self): ...
    def get_seller_name(self): ...
    @staticmethod
    def get_all_active(): ...
    def place_bid(self, team: Any, amount: Any): ...
    def _commit_seller(self, t: Transaction, var_amount: Any) -> Any: ...
    @staticmethod
    def create(team: Team, data: Any) -> Any: ...
    def commit(self) -> None: ...
    class Meta:
        verbose_name_plural: str = ...

class BlackAuction(Auction):
    seller_name: Any = ...
    def __str__(self): ...
    @property
    def description(self): ...
    def is_white(self): ...
    def get_seller_name(self): ...
    def commit(self) -> None: ...
    end: Any = ...
    def place_bid(self, team: Any, amount: Any) -> None: ...
    class Meta:
        verbose_name_plural: str = ...

class AuctionedItem(models.Model):
    auction: Any = ...
    entity: Any = ...
    amount: Any = ...
    visible: Any = ...
    will_sell: Any = ...
    def __str__(self): ...
    def block_expect(self, t: Transaction, bidder: Team, coef: Any=...) -> Any: ...
    def unblock(self, t: Transaction, bidder: Team) -> Any: ...
    class Meta:
        unique_together: Any = ...

class Bid(models.Model):
    auction: Any = ...
    team: Any = ...
    amount: Any = ...
    placed: Any = ...
    def block(self, t: Transaction, coef: Any=...) -> Any: ...
    def unblock(self, t: Transaction) -> Any: ...
    class Meta:
        unique_together: Any = ...
    def __repr__(self): ...
