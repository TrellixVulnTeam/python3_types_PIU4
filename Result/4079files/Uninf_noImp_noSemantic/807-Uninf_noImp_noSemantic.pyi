from demeter.rl.env import GymEnv
from typing import Any

def env(): ...
def test_transition(env: GymEnv) -> Any: ...
def test_reset(env: GymEnv) -> Any: ...
