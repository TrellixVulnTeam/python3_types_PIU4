from unittest import TestCase

class BooleanCastTestCase(TestCase):
    def test_basic_boolean_cast(self) -> None: ...
    def test_more_valid_boolean_values(self) -> None: ...
    def test_fail_invalid_boolean_cast(self) -> None: ...

class SequenceCastTestCase(TestCase):
    def test_basic_list_cast(self) -> None: ...
    def test_basic_tuple_cast(self) -> None: ...

class OptionCastTestCase(TestCase):
    def test_options(self) -> None: ...
    def test_fail_invalid_option_config(self) -> None: ...

class EvalCastTestCase(TestCase):
    def test_if_cast_is_unbounded(self) -> None: ...
