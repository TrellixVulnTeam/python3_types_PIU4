from typing import Any

def test_integer_conversion(roman_numeral: str, expected_integer: int) -> None: ...
def test_invalid_types(non_strings: Any) -> None: ...
def test_invalid_numerals(invalid_numerals: Any) -> None: ...
