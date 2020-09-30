# (generated with --quick)

from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar
import unittest.case

AzureScaleSet: Any
AzureVirtualScaleSet: Any
AzureWrapper: Any
KubePod: Any
ResourceGroup: Any
Usage: Any
UsageName: Any
VirtualMachineInstanceView: Any
VirtualMachineScaleSetVM: Any
VirtualMachineSize: Any
collections: module
datetime: Type[datetime.datetime]
mock: module
os: module
pykube: Any
pytz: module
timedelta: Type[datetime.timedelta]
unittest: module
yaml: module

_Tnamedtuple-TestNode-instance_id-unschedulable = TypeVar('_Tnamedtuple-TestNode-instance_id-unschedulable', bound=`namedtuple-TestNode-instance_id-unschedulable`)

class TestCluster(unittest.case.TestCase):
    def test_failed_scale_up(self) -> None: ...
    def test_near_quota_limit(self) -> None: ...
    def test_out_of_quota(self) -> None: ...
    def test_priority(self) -> None: ...
    def test_scale_in(self) -> None: ...
    def test_scale_up(self) -> None: ...
    def test_slow_scale_up(self) -> None: ...
    def test_tainted_scale_set(self) -> None: ...

class `namedtuple-TestNode-instance_id-unschedulable`(tuple):
    __slots__ = ["instance_id", "unschedulable"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    instance_id: Any
    unschedulable: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-TestNode-instance_id-unschedulable`], instance_id, unschedulable) -> `_Tnamedtuple-TestNode-instance_id-unschedulable`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-TestNode-instance_id-unschedulable`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-TestNode-instance_id-unschedulable`: ...
    def _replace(self: `_Tnamedtuple-TestNode-instance_id-unschedulable`, **kwds) -> `_Tnamedtuple-TestNode-instance_id-unschedulable`: ...

def _default_mock_clients(region, instances = ..., quotas = ...) -> Tuple[Any, Any, Any]: ...