from typing import Any

SAMPLE_OBJECTS: Any
EXPECTED_PATHS: Any
EXPECTED_VALUES: Any

def nested_data(request: Any): ...
def test_map_nested(nested_data: tuple) -> Any: ...
def _verify_logged_metrics(mock_logger: Any, expected_submissions_processed: Any) -> None: ...
def test_json_transform_to_model(session: Any, raw_data: Any, transformer: Any, mock_logger: Any): ...
def test_json_transform_to_dict(session: Any, raw_data: Any, transformer: Any): ...
def test_node_path_map_caching(monkeypatch: Any, session: Any, transformer: Any, mock_logger: Any, simple_form: Any, num_responses_with_same_schema: Any): ...
