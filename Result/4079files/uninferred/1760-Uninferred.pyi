from cortexutils.analyzer import Analyzer
from typing import Any

class VMRayAnalyzer(Analyzer):
    url: Any = ...
    vmrc: Any = ...
    def __init__(self) -> None: ...
    def run(self) -> None: ...
    def summary(self, raw: dict) -> dict: ...
