# (generated with --quick)

from typing import Any, Iterable, List, Mapping, Optional, Sequence, Union

TaskQueue: Any
os: module

class Printer:
    queue_printers: List[QueuePrinter]
    def __init__(self, queues) -> None: ...
    @classmethod
    def clear(cls) -> None: ...
    def format_queue_string(self) -> str: ...

class QueuePrinter:
    layout: str
    queue: Any
    def __init__(self, queue) -> None: ...
    def _format_execution_stats(self) -> str: ...
    def _format_queue_length_change_sign(self) -> str: ...
    def _format_queue_length_visualization(self) -> str: ...
    def format_string(self) -> str: ...

def tabulate(tabular_data: Union[Iterable[Iterable], Mapping[str, Iterable]], headers: Union[str, Sequence[str]] = ..., tablefmt: Union[str, tabulate.TableFormat] = ..., floatfmt: Union[str, Iterable[str]] = ..., numalign: Optional[str] = ..., stralign: Optional[str] = ..., missingval: Union[str, Iterable[str]] = ..., showindex: Union[bool, Iterable] = ..., disable_numparse: Union[bool, Iterable[int]] = ..., colalign: Optional[Iterable[Optional[str]]] = ...) -> str: ...
