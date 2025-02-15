from test_framework.test_framework import BitcoinTestFramework
from typing import Any

class HelpTest(BitcoinTestFramework):
    setup_clean_chain: bool = ...
    num_nodes: int = ...
    def set_test_params(self) -> None: ...
    def setup_network(self) -> None: ...
    def get_node_output(self, ret_code_expected: Any): ...
    def run_test(self) -> None: ...
