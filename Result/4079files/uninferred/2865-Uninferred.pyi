from typing import Any

class TestERC20Token:
    web3: Any = ...
    our_address: Any = ...
    second_address: Any = ...
    third_address: Any = ...
    token: Any = ...
    def setup_method(self) -> None: ...
    def test_fail_when_no_token_with_that_address(self) -> None: ...
    def test_symbol_for_dstoken_which_returns_bytes32(self) -> None: ...
    def test_total_supply(self) -> None: ...
    def test_balance_of(self) -> None: ...
    def test_transfer(self) -> None: ...
    def test_transfer_async(self) -> None: ...
    def test_transfer_failed(self) -> None: ...
    def test_transfer_failed_async(self) -> None: ...
    def test_transfer_out_of_gas(self) -> None: ...
    def test_transfer_out_of_gas_async(self) -> None: ...
    def test_transfer_generates_transfer(self) -> None: ...
    def test_transfer_from(self) -> None: ...
    def test_allowance_of(self) -> None: ...
    def test_approve(self) -> None: ...
    def test_equals(self) -> None: ...
    def test_should_have_printable_representation(self) -> None: ...

class TestDSToken:
    web3: Any = ...
    our_address: Any = ...
    second_address: Any = ...
    dstoken: Any = ...
    def setup_method(self) -> None: ...
    def test_fail_when_no_contract_under_that_address(self) -> None: ...
    def test_authority(self) -> None: ...
    def test_mint(self) -> None: ...
    def test_mint_to_other_address(self) -> None: ...
    def test_mint_generates_transfer(self) -> None: ...
    def test_burn(self) -> None: ...
    def test_burn_from_other_address(self) -> None: ...
    def test_burn_generates_transfer(self) -> None: ...
    def test_should_have_printable_representation(self) -> None: ...

class TestDSEthToken:
    web3: Any = ...
    our_address: Any = ...
    dsethtoken: Any = ...
    def setup_method(self) -> None: ...
    def test_fail_when_no_contract_under_that_address(self) -> None: ...
    def test_deposit(self) -> None: ...
    def test_withdraw(self) -> None: ...
    def test_should_have_printable_representation(self) -> None: ...
