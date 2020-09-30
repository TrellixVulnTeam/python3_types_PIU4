from typing import Any

class TestFetchCountryByIp:
    def test_calls_ip_api_endpoint(self, mock_ipdata: Any) -> None: ...

class TestFetchDocument:
    call_args: Any = ...
    def test_extra_headers(self, mock_get: Any) -> None: ...
    def test_raises_without_url_and_host(self) -> None: ...
    def test_url_is_called(self, mock_get: Any) -> None: ...
    def test_host_is_called_with_https_first_then_http(self, mock_get: Any): ...
    def test_host_is_sanitized(self, mock_get: Any) -> None: ...
    def test_path_is_sanitized(self, mock_get: Any) -> None: ...
    def test_exception_is_raised_if_both_protocols_fail(self, mock_get: Any) -> None: ...
    def test_exception_is_raised_if_url_fails(self, mock_get: Any) -> None: ...
    def test_exception_is_raised_if_http_fails_and_raise_ssl_errors_true(self, mock_get: Any) -> None: ...
    def test_exception_is_raised_on_network_error(self, mock_get: Any) -> None: ...

class TestFetchHostIp:
    def test_calls(self, mock_get_ip: Any) -> None: ...

class TestFetchHostIpAndCountry:
    def test_calls(self, mock_get_ip: Any, mock_fetch_country: Any) -> None: ...

class TestSendDocument:
    call_args: Any = ...
    def test_post_is_called(self, mock_post: Any) -> None: ...
    def test_post_raises_and_returns_exception(self, mock_post: Any) -> None: ...
    def test_post_called_with_only_one_headers_kwarg(self, mock_post: Any) -> None: ...
    def test_headers_in_either_case_are_handled_without_exception(self, mock_post: Any) -> None: ...