from typing import Any
from unittest import TestCase

class TestBasic(TestCase):
    MAKE_PATH: Any = ...
    MAKE_PROCESS: Any = ...
    EXEC_NAME: str = ...
    SIZE: int = ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    exec_path: Any = ...
    algorithms: Any = ...
    def setUp(self) -> None: ...
    def _compare_result_graph_from_two_algorithms(self, input_graph: str, first: str, second: str) -> Any: ...
    def test_GIVEN_source_code_WHEN_compiling_THEN_compile_success(self) -> None: ...
    def test_GIVEN_source_code_WHEN_compiling_THEN_no_error_message(self) -> None: ...
    def test_GIVEN_graph_empty_WHEN_fw_THEN_return_result_empty(self) -> None: ...
    def test_GIVEN_graph_k0_WHEN_fw_THEN_return_k0_result_path(self) -> None: ...
    def test_GIVEN_graph_k1_WHEN_fw_THEN_return_k1_result_path(self) -> None: ...
    def test_GIVEN_graph_kn_WHEN_fw_THEN_return_kn_result_path(self) -> None: ...
    def test_GIVEN_graph_dicircle_WHEN_fw_THEN_return_kn_correct_result_path(self) -> None: ...
    def test_GIVEN_all_small_graphs_WHEN_compare_navie_fw_with_cuda_naive_fw_THEN_results_path_are_the_same(self) -> None: ...
    def test_GIVEN_all_small_graphs_WHEN_compare_navie_fw_with_cuda_blocked_fw_THEN_results_path_are_the_same(self) -> None: ...
    def test_GIVEN_one_big_graph_WHEN_compare_navie_fw_with_cuda_naive_fw_THEN_results_path_are_the_same(self) -> None: ...
    def test_GIVEN_one_big_graph_WHEN_compare_navie_fw_with_cuda_blocked_fw_THEN_results_path_are_the_same(self) -> None: ...
