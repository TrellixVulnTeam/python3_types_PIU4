from ..model.base import *
from typing import Any

dir_path: Any

class plfr2014(Reform):
    name: str = ...
    class reduction_impot_exceptionnelle(Variable):
        definition_period: Any = ...
        def formula_2013_01_01(foyer_fiscal: Any, period: Any, parameters: Any): ...
    class reductions(Variable):
        label: str = ...
        definition_period: Any = ...
        def formula_2013_01_01(foyer_fiscal: Any, period: Any, parameters: Any): ...
    def apply(self) -> None: ...

def modify_parameters(parameters: Any): ...
