from typing import Any, Iterator

__author__: str
__version__: str
__date__: str
__revision__: str
__license__: str

def identity() -> Iterator[int]: ...
def triangular_numbers() -> Iterator[int]: ...
def fermat() -> Iterator[int]: ...
def mersenne() -> Iterator[int]: ...
def eratosthenes() -> Iterator[int]: ...
def composite() -> Iterator[int]: ...
def carmichael() -> Iterator[int]: ...
def ackermann_slow(m: int, n: int) -> int: ...
def ackermann_naive(m: int) -> Iterator[int]: ...
def ackermann_fast(m: int, n: int) -> int: ...
def ackermann(m: int) -> Iterator[int]: ...
def fibonacci() -> Iterator[int]: ...
def log_gen() -> Iterator[int]: ...

polys: Any

def LFSR(m: int) -> Iterator[int]: ...
