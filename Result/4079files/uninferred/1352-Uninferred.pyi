from audio_io.audio_io import AudioSource as AudioSource, AudioSourceInfo as AudioSourceInfo
from typing import Any, Iterable, NamedTuple, Tuple

def get_log_path(in_path: Any): ...

class LogGroup(NamedTuple):
    performers: Iterable[str]
    albums: Iterable[str]
    channels: int
    sample_rate: int
    tracks_dr: Iterable[Tuple[int, float, float, int, str]]

def get_group_title(group: LogGroup) -> Any: ...
def format_time(seconds: Any): ...
def write_log(out_path: Any, dr_log_groups: Iterable[LogGroup], average_dr: Any) -> Any: ...
def flatmap(f: Any, items: Any) -> None: ...
def make_log_groups(l: Iterable[Tuple[AudioSourceInfo, Iterable[Tuple[int, float, float, int, str]]]]) -> Any: ...
def parse_args(): ...
def main() -> None: ...
def fix_tty() -> None: ...
def analyze_dr(in_path: str, track_cb: Any) -> Any: ...
