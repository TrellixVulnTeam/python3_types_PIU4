# (generated with --quick)

import decimal
from typing import Any, Dict, List, Optional, Tuple, Type

Adapter: Any
Decimal: Type[decimal.Decimal]
libcloud: Any
os: module
parse: module
socket: module

class Ovh(Any):
    __doc__: str
    _plans: List[Tuple[str, str]]
    _pricing: dict
    _sizes: Dict[str, list]
    auth_credential_fields: List[List[str]]
    auth_instructions: str
    generic_credentials: Dict[str, str]
    id: str
    name: str
    server_external_iface: None
    server_internal_iface: str
    server_ssh_key_method: str
    server_ssh_user: str
    def __init__(self, **kwargs) -> None: ...
    def _find_image(self, driver, location, id) -> Any: ...
    def _find_size(self, driver, location, id) -> Any: ...
    def _get_cpu(self, location, plan, size) -> Any: ...
    def _get_create_args(self, data) -> Dict[str, Any]: ...
    def _get_hourly_price(self, location, plan, size) -> Optional[float]: ...
    @classmethod
    def _get_id(cls) -> str: ...
    def _get_int_ip(self, server) -> Any: ...
    def _get_monthly_price(self, location, plan, size) -> Optional[float]: ...
    def _get_plans(self, location) -> List[Tuple[str, str]]: ...
    def _get_request_credentials(self, headers) -> Dict[str, Any]: ...
    def _get_size_id(self, location, plan, size) -> Any: ...
    def _get_sizes(self, location, plan) -> list: ...
    def _get_user_driver(self, **auth_credentials) -> Any: ...
    def get_default_plan(self) -> str: ...
    def get_default_region(self) -> str: ...
    def get_default_size(self) -> str: ...