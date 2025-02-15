# (generated with --quick)

import __future__
import numpy
from typing import Any, List, Tuple

absltest: Any
absolute_import: __future__._Feature
division: __future__._Feature
np: module
print_function: __future__._Feature
quantiles_util: Any
statistics_pb2: Any
text_format: Any

class QuantilesUtilTest(Any):
    def test_find_median(self) -> None: ...
    def test_generate_equi_width_buckets(self) -> None: ...
    def test_generate_equi_width_histogram(self) -> None: ...
    def test_generate_quantiles_histogram(self) -> None: ...
    def test_generate_quantiles_histogram_diff_num_buckets_multiple(self) -> None: ...
    def test_generate_quantiles_histogram_diff_num_buckets_non_multiple(self) -> None: ...
    def test_quantiles_combiner(self) -> None: ...
    def test_quantiles_combiner_with_weights(self) -> None: ...

def _assert_buckets_almost_equal(test, a: List[Tuple[float, float, float]], b: List[Tuple[float, float, float]]) -> None: ...
def _run_quantiles_combiner_test(test, q_combiner, batches: List[List[numpy.ndarray]], expected_result: numpy.ndarray) -> None: ...
