# (generated with --quick)

import __future__
import numpy
from typing import Any

IS_PY3: Any
TestConstantBytes: Any
TypingError: Any
a0: numpy.ndarray
a1: Any
a2: Any
a3: Any
a4: Any
a5: Any
a6: Any
compile_isolated: Any
dt: Any
myarray: numpy.ndarray
np: module
print_function: __future__._Feature
s1: Any
typeof: Any
types: Any
unittest: Any

class TestConstantArray(Any):
    __doc__: str
    def check_array_const(self, pyfunc) -> None: ...
    def test_array_const_0d(self) -> None: ...
    def test_array_const_1d_contig(self) -> None: ...
    def test_array_const_1d_noncontig(self) -> None: ...
    def test_array_const_2d(self) -> None: ...
    def test_array_const_alignment(self) -> None: ...
    def test_arrayscalar_const(self) -> None: ...
    def test_issue_1850(self) -> None: ...
    def test_record_array_const_contig(self) -> None: ...
    def test_record_array_const_noncontig(self) -> None: ...
    def test_too_big_to_freeze(self) -> None: ...
    def test_write_to_global_array(self) -> None: ...

def bytes_as_const_array() -> Any: ...
def getitem0(i) -> Any: ...
def getitem1(i) -> Any: ...
def getitem2(i) -> Any: ...
def getitem3(i) -> Any: ...
def getitem4(i) -> Any: ...
def getitem5(i) -> Any: ...
def getitem6(i) -> Any: ...
def jit(signature_or_function = ..., locals = ..., target = ..., cache = ..., pipeline_class = ..., **options) -> Any: ...
def use_arrayscalar_const() -> Any: ...
def write_to_global_array() -> None: ...
