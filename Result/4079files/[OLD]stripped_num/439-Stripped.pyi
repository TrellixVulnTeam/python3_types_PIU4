# (generated with --quick)

from typing import Any

ContentType: Any
LogEntry: Any
constants: Any
model_to_dict: Any

def log_action(action = ..., action_type = ..., user = ..., instance = ..., object_repr = ..., old_data = ..., new_data = ...) -> Any: ...
def log_create_object(instance, user = ..., fields = ..., exclude = ...) -> Any: ...
def log_delete_object(instance, user = ..., fields = ..., exclude = ...) -> Any: ...
def log_update_object(instance, old_data = ..., new_data = ..., user = ..., object_repr = ..., fields = ..., exclude = ...) -> Any: ...
