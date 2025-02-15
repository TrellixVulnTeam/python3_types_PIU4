# (generated with --quick)

import decimal
from typing import Any, Dict, Type

ConversionRate: Any
Decimal: Type[decimal.Decimal]
Money: Any
MoneyRange: Any
RATES: Dict[str, decimal.Decimal]
TaxedMoney: Any
TaxedMoneyRange: Any
base_currency: Any
conversion_rates: Any
exchange_currency: Any
functools: module
get_rates: Any
percentage_discount: Any
prices_multicurrency: Any
pytest: Any

def test_base_currency_to_another() -> None: ...
def test_conversionrate__str_repr(conversion_rates) -> None: ...
def test_convert_other_currency_to_base_currency() -> None: ...
def test_convert_two_non_base_currencies() -> None: ...
def test_exchange_currency_for_money_range() -> None: ...
def test_exchange_currency_for_money_range_uses_passed_conversion_rate() -> None: ...
def test_exchange_currency_for_taxed_money() -> None: ...
def test_exchange_currency_for_taxed_money_range() -> None: ...
def test_exchange_currency_for_taxed_money_range_uses_passed_conversion_rate() -> None: ...
def test_exchange_currency_for_taxed_money_uses_passed_conversion_rate() -> None: ...
def test_exchange_currency_raises_for_nonsupported_type() -> None: ...
def test_exchange_currency_uses_passed_conversion_rate() -> None: ...
def test_get_rates_caches_results(conversion_rates) -> None: ...
def test_get_rates_force_update_cache(conversion_rates) -> None: ...
def test_template_filter_money_in_currency() -> None: ...
def test_the_same_currency_uses_no_conversion() -> None: ...
def test_two_base_currencies_convert_price_uses_passed_conversion_rate() -> None: ...
def test_two_base_currencies_the_same_currency_uses_no_conversion() -> None: ...
