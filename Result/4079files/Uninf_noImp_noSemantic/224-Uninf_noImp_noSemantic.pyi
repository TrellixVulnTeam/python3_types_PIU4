import pykube
from k8s_snapshots.context import Context
from typing import Any, AsyncGenerator, Callable, Iterable, Optional, Type, TypeVar

_logger: Any
Resource = TypeVar('Resource', bound=pykube.objects.APIObject)
ClientFactory: Any
_WatchEvent: Any

class SnapshotRule(pykube.objects.APIObject):
    version: str = ...
    endpoint: str = ...
    kind: str = ...

class Kubernetes:
    client_factory: Any = ...
    def __init__(self, client_factory: Optional[ClientFactory]=...) -> None: ...
    def get_or_none(self, resource_type: Type[Resource], name: str, namespace: Optional[str]=...) -> Optional[Resource]: ...
    def watch(self, resource_type: Type[Resource]) -> Iterable[_WatchEvent]: ...

def get_resource_or_none_sync(client_factory: ClientFactory, resource_type: Type[Resource], name: str, namespace: Optional[str]=...) -> Optional[Resource]: ...
async def get_resource_or_none(client_factory: ClientFactory, resource_type: Type[Resource], name: str, namespace: Optional[str]=..., *, loop: Any=...) -> Optional[Resource]: ...
def watch_resources_sync(client_factory: ClientFactory, resource_type: pykube.objects.APIObject) -> Iterable: ...
async def watch_resources(ctx: Context, resource_type: Resource, delay: int, *, allow_missing: bool=..., loop: Any=...) -> AsyncGenerator[_WatchEvent, None]: ...
async def _watch_resources_thread_wrapper(client_factory: Callable[[], pykube.HTTPClient], resource_type: Type[Resource], allow_missing: bool=..., *, loop: Any=...) -> AsyncGenerator[_WatchEvent, None]: ...
