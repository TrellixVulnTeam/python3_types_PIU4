from tests.test_api_base import N26TestBase

class AccountTests(N26TestBase):
    def test_get_account_info_cli(self) -> None: ...
    def test_get_account_statuses_cli(self) -> None: ...
    def test_limits_cli(self) -> None: ...
    def test_addresses_cli(self) -> None: ...
    def test_get_contacts(self) -> None: ...
    def test_contacts_cli(self) -> None: ...
    def test_get_statements_cli(self) -> None: ...
