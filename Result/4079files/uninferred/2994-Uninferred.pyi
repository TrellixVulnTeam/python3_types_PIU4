from scr.logic.solvers.solvers_algorithm.solver_algorithm import Solver_algorithm
from typing import Any

class Root(Solver_algorithm):
    _solution: Any = ...
    def __init__(self) -> None: ...
    def solve(self, circuit: Any, initial_conditions: Any, **kwargs: Any): ...
    def _get_equations_error(self, x: Any, circuit: Any): ...
    def _adapt_solution_to_solution_results(self): ...
