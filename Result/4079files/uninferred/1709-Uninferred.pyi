from i3configger import config
from typing import Any

log: Any

def build_all() -> None: ...
def generate_contents(cnf: config.I3configgerConfig, prts: Any, msg: Any) -> Any: ...
def make_header(partialsPath: Any): ...
def generate_main_content(partialsPath: Any, selected: Any, ctx: Any): ...
def get_bar_setting(barCnf: Any, prts: Any, ctx: Any): ...
def generate_i3bar_content(prts: Any, selectValue: Any, ctx: Any): ...
def check_config(content: Any) -> None: ...
def persist_results(pathContentsMap: Any) -> None: ...