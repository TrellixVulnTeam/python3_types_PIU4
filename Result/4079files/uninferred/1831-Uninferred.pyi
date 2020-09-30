import dm_env
import sonnet as snt
from bsuite.baselines import base
from dm_env import specs as specs
from typing import Any

class DQNTF2(base.Agent):
    _num_actions: Any = ...
    _discount: Any = ...
    _batch_size: Any = ...
    _sgd_period: Any = ...
    _target_update_period: Any = ...
    _optimizer: Any = ...
    _epsilon: Any = ...
    _total_steps: int = ...
    _replay: Any = ...
    _min_replay_size: Any = ...
    _rng: Any = ...
    _online_network: Any = ...
    _target_network: Any = ...
    _forward: Any = ...
    def __init__(self, action_spec: specs.DiscreteArray, online_network: snt.Module, target_network: snt.Module, batch_size: int, discount: float, replay_capacity: int, min_replay_size: int, sgd_period: int, target_update_period: int, optimizer: snt.Optimizer, epsilon: float, seed: int=...) -> None: ...
    def policy(self, timestep: dm_env.TimeStep) -> base.Action: ...
    def update(self, timestep: dm_env.TimeStep, action: base.Action, new_timestep: dm_env.TimeStep) -> Any: ...
    def _training_step(self, transitions: Any): ...

def default_agent(obs_spec: specs.Array, action_spec: specs.DiscreteArray) -> Any: ...