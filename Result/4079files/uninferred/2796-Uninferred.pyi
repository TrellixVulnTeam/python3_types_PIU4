from typing import Any

vowel_data_y_dimension: int

def vowel_data(): ...
def SAHeart_data(): ...
def test_vowel_data() -> None: ...
def test_indicator_matrix(vowel_data: Any) -> None: ...
def test_LDA(vowel_data: Any) -> None: ...
def test_QDA(vowel_data: Any) -> None: ...
def test_RDA(vowel_data: Any) -> None: ...
def test_LDA_computation(vowel_data: Any) -> None: ...
def test_RRLDA(vowel_data: Any) -> None: ...
def test_SAHeart_data_set(SAHeart_data: Any) -> None: ...
def test_binary_logistic_regression(SAHeart_data: Any) -> None: ...
