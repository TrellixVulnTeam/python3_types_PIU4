# (generated with --quick)

import numpy
from typing import Any, Optional

np: module
plt: Any

class FPlots:
    @staticmethod
    def Magnitude(x, ylabel: str, legend: Optional[str] = ..., place: int = ...) -> Any: ...
    @staticmethod
    def Phase(x, ylabel: str, legend: Optional[str] = ..., place: int = ...) -> Any: ...
    @staticmethod
    def Real(x, ylabel: str, legend: Optional[str] = ..., place: int = ...) -> Any: ...
    @staticmethod
    def X(x, ylabel: str, legend: Optional[str] = ..., place: int = ...) -> Any: ...
    @staticmethod
    def plot(func, D, ylabel: str, legend: Optional[str] = ...) -> Any: ...

class Plots:
    @staticmethod
    def plot(x: numpy.ndarray, D: Optional[numpy.ndarray] = ..., label: str = ..., title: Optional[str] = ..., legend: Optional[str] = ..., place: int = ...) -> Any: ...
    @staticmethod
    def plotRealAndImag(vector: numpy.ndarray, n: numpy.ndarray, title: Optional[str] = ..., place: int = ..., label: Optional[str] = ...) -> Any: ...

class Signal:
    def create(func: Signal, D) -> numpy.ndarray: ...
    @staticmethod
    def d(n: int) -> int: ...
    @staticmethod
    def hermitianTransposed(x) -> Any: ...
    @staticmethod
    def u(n: int) -> int: ...

class Transforms:
    @staticmethod
    def convolute(x, y, n: int, D) -> int: ...

class VectorSignal:
    @staticmethod
    def d(n: numpy.ndarray, n1: int = ...) -> numpy.ndarray: ...
    @staticmethod
    def u(n: numpy.ndarray, n1: int = ...) -> numpy.ndarray: ...