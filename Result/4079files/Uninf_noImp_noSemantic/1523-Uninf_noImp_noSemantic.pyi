from collections import OrderedDict as OrderedDict
from typing import Any

LOG: Any

class Experiment:
    resource_limitations: Any = ...
    profile_calculations: Any = ...
    experiment_configurations: Any = ...
    pre_configuration: Any = ...
    configuration_space_list: Any = ...
    overload_vnf_list: Any = ...
    original_definition: Any = ...
    def __init__(self, definition: Any) -> None: ...
    def populate(self) -> None: ...
    def _get_pre_configuration_as_dict(self): ...
    def _get_experiment_header_space_as_dict(self): ...
    def _get_function_resource_space_as_dict(self): ...
    def _get_mp_space_as_dict(self): ...

class ServiceExperiment(Experiment):
    def __init__(self, definition: Any) -> None: ...

class FunctionExperiment(Experiment):
    def __init__(self, definition: Any) -> None: ...

class ExperimentConfiguration:
    RUN_ID: int = ...
    run_id: Any = ...
    name: Any = ...
    experiment: Any = ...
    parameter: Any = ...
    def __init__(self, experiment: Any, p: Any) -> None: ...
    def __repr__(self): ...
