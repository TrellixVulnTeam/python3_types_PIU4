from .api import API, CustomList
from typing import Any, Optional

__all__: Any

class NetworkAPI(API):
    _serviceType: str = ...
    def __init__(self, token: Any, baseURIPrefix: Optional[Any] = ...) -> None: ...

class SecurityGroupList(NetworkAPI, CustomList):
    def __init__(self, token: Any, info: Optional[Any] = ...) -> None: ...
    def _getitem(self, key: Any, item: Any): ...
    def __str__(self): ...
    def update(self, res: Optional[Any] = ...) -> None: ...
    def getSecurityGroup(self, sgid: Optional[Any] = ..., name: Optional[Any] = ...): ...
    def add(self, name: Any, description: Optional[Any] = ...): ...
    def delete(self, securityGroupID: Any) -> None: ...

class SecurityGroup(NetworkAPI):
    id_: Any = ...
    name: Any = ...
    description: Any = ...
    rules: Any = ...
    def __init__(self, token: Any, info: Any) -> None: ...
    def updateName(self, name: Any) -> None: ...
    def updateDescription(self, description: Any) -> None: ...

class SecurityGroupRuleList(NetworkAPI, CustomList):
    securityGroupID: Any = ...
    def __init__(self, token: Any, id_: Any, info: Any) -> None: ...
    def _getitem(self, key: Any, item: Any): ...
    def update(self) -> None: ...
    def add(self, direction: Any, ethertype: Any, portMin: Optional[Any] = ..., portMax: Optional[Any] = ..., protocol: Optional[Any] = ..., remoteIPPrefix: Optional[Any] = ...) -> None: ...
    def delete(self, securityGroupRuleID: Any) -> None: ...

class SecurityGroupRule(NetworkAPI):
    id_: Any = ...
    direction: Any = ...
    ethertype: Any = ...
    rangeMin: Any = ...
    rangeMax: Any = ...
    protocol: Any = ...
    remoteIPPrefix: Any = ...
    def __init__(self, info: Any) -> None: ...

class AddressList(CustomList):
    def __init__(self, info: Any) -> None: ...
    def _getitem(self, key: Any, item: Any): ...
    def __str__(self): ...

class Address:
    version: Any = ...
    addr: Any = ...
    def __init__(self, info: Any) -> None: ...
