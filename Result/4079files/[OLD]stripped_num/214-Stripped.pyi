# (generated with --quick)

from typing import Any, Dict

REPO: str
argparse: module
json: module
logging: module
os: module
request: module
subprocess: module
tempfile: module

class Party:
    answers: Dict[Any, int]
    id: Any
    name: Any
    def __init__(self, id, name) -> None: ...
    def answer(self, statement, answer) -> None: ...
    def similar(self, party) -> Any: ...

class Renderer:
    parties: Dict[Any, Party]
    prefix: str
    def __init__(self, data_key) -> None: ...
    def create_edges(self, dotfile) -> None: ...
    def create_nodes(self, dotfile) -> None: ...
    def get_parties(self) -> None: ...
    def load_answers(self) -> None: ...
    def render(self, neato, output) -> None: ...

def main() -> None: ...
