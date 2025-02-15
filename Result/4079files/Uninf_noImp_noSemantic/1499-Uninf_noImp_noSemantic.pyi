from .models import *
from core.permissions import CustomPermission
from rest_framework import permissions as permissions
from typing import Any

def object_check_manager(request: Any, view: Any, obj: Any): ...

class IsManagerOrReadOnly(CustomPermission):
    allow_read_only: bool = ...
    object_permission_functions: Any = ...

class IsManager(CustomPermission):
    require_authentication: bool = ...
    allow_admin: bool = ...
    object_permission_functions: Any = ...

def check_order_ownership(request: Any, view: Any, obj: Any): ...

class IsOrderOwnerOrAdmin(CustomPermission):
    require_authentication: bool = ...
    pass_for_obj: bool = ...
    allow_admin: bool = ...
    allow_create: bool = ...
    object_permission_functions: Any = ...

def allow_only_retrieve_for_non_admin(request: Any, view: Any): ...

class IsOrderOwnerReadOnlyOrAdmin(CustomPermission):
    require_authentication: bool = ...
    permission_functions: Any = ...
    object_permission_functions: Any = ...

def no_delete(request: Any, view: Any, obj: Any): ...

class IsOrderOwnerReadUpdateOrAdmin(CustomPermission):
    require_authentication: bool = ...
    pass_for_obj: bool = ...
    allow_admin: bool = ...
    object_permission_functions: Any = ...
    check_with_or: bool = ...
