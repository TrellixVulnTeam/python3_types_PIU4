from typing import Any, Optional, Union
from wsproto.extensions import Extension

class FakeExtension(Extension):
    name: str = ...
    offer_response: Any = ...
    accepted_offer: Any = ...
    offered: Any = ...
    accept_response: Any = ...
    def __init__(self, offer_response: Optional[Union[bool, str]]=..., accept_response: Optional[Union[bool, str]]=...) -> None: ...
    def offer(self) -> Union[bool, str]: ...
    def finalize(self, offer: str) -> None: ...
    def accept(self, offer: str) -> Union[bool, str]: ...