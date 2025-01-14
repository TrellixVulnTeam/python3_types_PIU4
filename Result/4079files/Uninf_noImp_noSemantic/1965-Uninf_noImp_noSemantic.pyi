from .configuration import Config
from .gridforce import Forcing, Grid
from typing import Any

Velocity: Any
State = Any

class Tracker:
    dt: Any = ...
    advect: Any = ...
    diffusion: Any = ...
    D: Any = ...
    def __init__(self, config: Config) -> None: ...
    num_particles: Any = ...
    xmin: Any = ...
    xmax: Any = ...
    ymin: Any = ...
    ymax: Any = ...
    def move_particles(self, grid: Grid, forcing: Forcing, state: State) -> None: ...
    def EF(self, forcing: Forcing, state: State) -> Velocity: ...
    def RK2a(self, forcing: Forcing, state: State) -> Velocity: ...
    def RK2b(self, forcing: Forcing, state: State) -> Velocity: ...
    RK2: Any = ...
    def RK4a(self, forcing: Forcing, state: State) -> Velocity: ...
    def RK4b(self, forcing: Forcing, state: State) -> Velocity: ...
    RK4: Any = ...
    def diffuse(self) -> Velocity: ...
