from interfaces.LTS import LTS
from interfaces.automaton import Automaton
from interfaces.expr import Signal as Signal
from interfaces.func_description import FuncDesc
from synthesis.encoder_interface import EncoderInterface
from typing import Any, Dict, Iterable, List

class CoreachEncoder(EncoderInterface):
    automaton: Any = ...
    inputs: Any = ...
    descr_by_output: Any = ...
    tau_desc: Any = ...
    max_model_states: Any = ...
    reach_func_desc: Any = ...
    model_init_state: Any = ...
    last_allowed_states: Any = ...
    max_k: Any = ...
    forbidding_atoms: Any = ...
    def __init__(self, automaton: Automaton, tau_desc: FuncDesc, inputs: Iterable[Signal], descr_by_output: Dict[Signal, FuncDesc], all_model_states: Iterable[int], max_k: int, model_init_state: int=...): ...
    def encode_headers(self) -> List[str]: ...
    def _encode_model_functions(self) -> List[str]: ...
    def _encode_automata_functions(self) -> List[str]: ...
    def _encode_counters(self) -> List[str]: ...
    def _declare_forbidding_atoms(self) -> List[str]: ...
    def _encode_meaning_of_forbidding_atoms(self) -> List[str]: ...
    def encode_initialization(self) -> List[str]: ...
    def encode_run_graph(self, states_to_encode: Any) -> List[str]: ...
    def encode_model_bound(self, allowed_model_states: Iterable[int]) -> List[str]: ...
    def encode_assumption_forbid_k(self, k: int) -> List[str]: ...
    def encode_get_model_values(self) -> List[str]: ...
    def parse_model(self, smt_get_value_lines: Any) -> LTS: ...
