from collections import namedtuple
from typing import Any

__all__: Any
nan: Any

class Object:
    __slots__: Any = ...
    defaults: dict = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __repr__(self): ...
    __str__: Any = ...
    def __eq__(self, other: Any) -> Any: ...
    def tuple(self): ...
    def dict(self): ...
    def update(self, **kwargs: Any): ...
    def diff(self, other: Any): ...
    def nonDefaults(self): ...

class DynamicObject:
    def __init__(self, **kwargs: Any) -> None: ...
    def __repr__(self): ...

class ContractDetails(Object):
    defaults: Any = ...
    __slots__: Any = ...

class ContractDescription(Object):
    defaults: Any = ...
    __slots__: Any = ...

class ComboLeg(Object):
    defaults: Any = ...
    __slots__: Any = ...

class DeltaNeutralContract(Object):
    defaults: Any = ...
    __slots__: Any = ...

class OrderComboLeg(Object):
    defaults: Any = ...
    __slots__: Any = ...

class OrderState(Object):
    defaults: Any = ...
    __slots__: Any = ...

class ScannerSubscription(Object):
    defaults: Any = ...
    __slots__: Any = ...

class SoftDollarTier(Object):
    defaults: Any = ...
    __slots__: Any = ...

class Execution(Object):
    defaults: Any = ...
    __slots__: Any = ...

class CommissionReport(Object):
    defaults: Any = ...
    __slots__: Any = ...

class ExecutionFilter(Object):
    defaults: Any = ...
    __slots__: Any = ...

class BarData(Object):
    defaults: Any = ...
    __slots__: Any = ...

class RealTimeBar(Object):
    defaults: Any = ...
    __slots__: Any = ...

class TickAttrib(Object):
    defaults: Any = ...
    __slots__: Any = ...

class TickAttribBidAsk(Object):
    defaults: Any = ...
    __slots__: Any = ...

class TickAttribLast(Object):
    defaults: Any = ...
    __slots__: Any = ...

class HistogramData(Object):
    defaults: Any = ...
    __slots__: Any = ...

class NewsProvider(Object):
    defaults: Any = ...
    __slots__: Any = ...

class DepthMktDataDescription(Object):
    defaults: Any = ...
    __slots__: Any = ...

class PnL(Object):
    defaults: Any = ...
    __slots__: Any = ...

class PnLSingle(Object):
    defaults: Any = ...
    __slots__: Any = ...

class FundamentalRatios(DynamicObject): ...

class BarList(list):
    events: Any = ...
    __slots__: Any = ...
    updateEvent: Any = ...
    def __init__(self, *args: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

class BarDataList(BarList):
    __slots__: Any = ...

class RealTimeBarList(BarList):
    __slots__: Any = ...

class ScanDataList(list):
    events: Any = ...
    __slots__: Any = ...
    updateEvent: Any = ...
    def __init__(self, *args: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...

TagValue = namedtuple('TagValue', 'tag value')

AccountValue = namedtuple('AccountValue', 'account tag value currency modelCode')

TickData = namedtuple('TickData', 'time tickType price size')

HistoricalTick = namedtuple('HistoricalTick', 'time price size')

HistoricalTickBidAsk = namedtuple('HistoricalTickBidAsk', 'time tickAttribBidAsk priceBid priceAsk sizeBid sizeAsk')

HistoricalTickLast = namedtuple('HistoricalTickLast', 'time tickAttribLast price size exchange specialConditions')

TickByTickAllLast = namedtuple('TickByTickAllLast', 'tickType time price size tickAttribLast exchange specialConditions')

TickByTickBidAsk = namedtuple('TickByTickBidAsk', 'time bidPrice askPrice bidSize askSize tickAttribBidAsk')

TickByTickMidPoint = namedtuple('TickByTickMidPoint', 'time midPoint')

MktDepthData = namedtuple('MktDepthData', 'time position marketMaker operation side price size')

DOMLevel = namedtuple('DOMLevel', 'price size marketMaker')

BracketOrder = namedtuple('BracketOrder', 'parent takeProfit stopLoss')

TradeLogEntry = namedtuple('TradeLogEntry', 'time status message')

PriceIncrement = namedtuple('PriceIncrement', 'lowEdge increment')

ScanData = namedtuple('ScanData', 'rank contractDetails distance benchmark projection legsStr')

PortfolioItem = namedtuple('PortfolioItem', 'contract position marketPrice marketValue averageCost unrealizedPNL realizedPNL account')

Position = namedtuple('Position', 'account contract position avgCost')

Fill = namedtuple('Fill', 'contract execution commissionReport time')

OptionComputation = namedtuple('OptionComputation', 'impliedVol delta optPrice pvDividend gamma vega theta undPrice')

OptionChain = namedtuple('OptionChain', 'exchange underlyingConId tradingClass multiplier expirations strikes')

Dividends = namedtuple('Dividends', 'past12Months next12Months nextDate nextAmount')

NewsArticle = namedtuple('NewsArticle', 'articleType articleText')

HistoricalNews = namedtuple('HistoricalNews', 'time providerCode articleId headline')

NewsTick = namedtuple('NewsTick', 'timeStamp providerCode articleId headline extraData')

NewsBulletin = namedtuple('NewsBulletin', 'msgId msgType message origExchange')

FamilyCode = namedtuple('FamilyCode', 'accountID familyCodeStr')

SmartComponent = namedtuple('SmartComponent', 'bitNumber exchange exchangeLetter')

ConnectionStats = namedtuple('ConnectionStats', 'startTime duration numBytesRecv numBytesSent numMsgRecv numMsgSent')
