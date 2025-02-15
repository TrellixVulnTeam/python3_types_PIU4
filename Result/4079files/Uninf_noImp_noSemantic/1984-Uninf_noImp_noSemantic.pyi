from stoq.data_classes import DispatcherResponse, Payload, RequestMeta, WorkerResponse
from stoq.plugins import DispatcherPlugin, WorkerPlugin
from typing import Any, Optional

class MultiClassPlugin(WorkerPlugin, DispatcherPlugin):
    RAISE_EXCEPTION: bool = ...
    RETURN_ERRORS: bool = ...
    SHOULD_ARCHIVE: bool = ...
    WORKERS: Any = ...
    RULE_COUNT: int = ...
    def scan(self, payload: Payload, request_meta: RequestMeta) -> Optional[WorkerResponse]: ...
    def get_dispatches(self, payload: Payload, request_meta: RequestMeta) -> Optional[DispatcherResponse]: ...
