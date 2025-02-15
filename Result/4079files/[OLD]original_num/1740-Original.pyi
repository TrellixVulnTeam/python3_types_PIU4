# (generated with --quick)

import pynamodb.connection.base
from typing import Any, Type

Connection: Type[pynamodb.connection.base.Connection]

class TableConnection(object):
    __doc__: str
    _hash_keyname: None
    _range_keyname: None
    connection: pynamodb.connection.base.Connection
    table_name: Any
    def __init__(self, table_name, region = ..., host = ..., session_cls = ..., request_timeout_seconds = ..., max_retry_attempts = ..., base_backoff_ms = ..., aws_access_key_id = ..., aws_secret_access_key = ...) -> None: ...
    def batch_get_item(self, keys, consistent_read = ..., return_consumed_capacity = ..., attributes_to_get = ...) -> Any: ...
    def batch_write_item(self, put_items = ..., delete_items = ..., return_consumed_capacity = ..., return_item_collection_metrics = ...) -> Any: ...
    def create_table(self, attribute_definitions = ..., key_schema = ..., read_capacity_units = ..., write_capacity_units = ..., global_secondary_indexes = ..., local_secondary_indexes = ..., stream_specification = ...) -> Any: ...
    def delete_item(self, hash_key, range_key = ..., condition = ..., expected = ..., conditional_operator = ..., return_values = ..., return_consumed_capacity = ..., return_item_collection_metrics = ...) -> Any: ...
    def delete_table(self) -> Any: ...
    def describe_table(self) -> Any: ...
    def get_item(self, hash_key, range_key = ..., consistent_read = ..., attributes_to_get = ...) -> Any: ...
    def get_meta_table(self, refresh = ...) -> Any: ...
    def put_item(self, hash_key, range_key = ..., attributes = ..., condition = ..., expected = ..., conditional_operator = ..., return_values = ..., return_consumed_capacity = ..., return_item_collection_metrics = ...) -> Any: ...
    def query(self, hash_key, range_key_condition = ..., filter_condition = ..., attributes_to_get = ..., consistent_read = ..., exclusive_start_key = ..., index_name = ..., key_conditions = ..., query_filters = ..., limit = ..., return_consumed_capacity = ..., scan_index_forward = ..., conditional_operator = ..., select = ...) -> Any: ...
    def rate_limited_scan(self, filter_condition = ..., attributes_to_get = ..., page_size = ..., limit = ..., conditional_operator = ..., scan_filter = ..., segment = ..., total_segments = ..., exclusive_start_key = ..., timeout_seconds = ..., read_capacity_to_consume_per_second = ..., allow_rate_limited_scan_without_consumed_capacity = ..., max_sleep_between_retry = ..., max_consecutive_exceptions = ..., consistent_read = ..., index_name = ...) -> Any: ...
    def scan(self, filter_condition = ..., attributes_to_get = ..., limit = ..., conditional_operator = ..., scan_filter = ..., return_consumed_capacity = ..., segment = ..., total_segments = ..., exclusive_start_key = ..., consistent_read = ..., index_name = ...) -> Any: ...
    def update_item(self, hash_key, range_key = ..., actions = ..., attribute_updates = ..., condition = ..., expected = ..., conditional_operator = ..., return_consumed_capacity = ..., return_item_collection_metrics = ..., return_values = ...) -> Any: ...
    def update_table(self, read_capacity_units = ..., write_capacity_units = ..., global_secondary_index_updates = ...) -> Any: ...
