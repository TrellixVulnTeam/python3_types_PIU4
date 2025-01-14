from elliptic.Kernel.Context import ContextDelegate
from elliptic.Kernel.DSL import DSLMeta
from elliptic.Kernel.TemplateManager import TemplateManagerBase
from examples.DSL_Example.src.DSL import VectorImplementationBase
from typing import Any, List, Type

class VectorTemplateManager(TemplateManagerBase):
    def __init__(self) -> None: ...

class VectorMeta(DSLMeta):
    def include_dirs(self) -> List[str]: ...
    def libs(self) -> List[str]: ...

class VectorImplementation(VectorImplementationBase):
    def base_delegate(self) -> Type[ContextDelegate]: ...
    def range_delegate(self, start: Any, count: Any) -> Type[ContextDelegate]: ...
    def scalar_mult_delegate(self, scalar: int) -> Type[ContextDelegate]: ...
    def scalar_sum_delegate(self, scalar: int) -> Type[ContextDelegate]: ...
    def sum_delegate(self) -> Type[ContextDelegate]: ...
