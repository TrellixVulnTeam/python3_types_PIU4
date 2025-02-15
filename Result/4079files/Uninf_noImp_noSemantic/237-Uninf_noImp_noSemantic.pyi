import ast
from ..matching import var as var
from typing import Any, Optional

class Translator:
    sorts: Any = ...
    generators: Any = ...
    operations: Any = ...
    axioms: Any = ...
    def __init__(self) -> None: ...
    def register(self, obj: Any) -> None: ...
    def pre_translate(self) -> None: ...
    def translate(self) -> None: ...
    def post_translate(self) -> None: ...
    def register_axiom(self, operation: Any, guards: Any, matchs: Any, return_value: Any) -> None: ...
    def _parse_operation(self, operation: Any, register_axiom: Any) -> None: ...

class _OperationParser(ast.NodeVisitor):
    comparison_operators: Any = ...
    register_axiom: Any = ...
    operation: Any = ...
    stack: Any = ...
    locals: Any = ...
    def __init__(self, register_axiom: Any, operation: Any, stack: Optional[Any] = ..., local_vars: Optional[Any] = ...) -> None: ...
    @property
    def fn_scope(self): ...
    def visit_Assign(self, node: Any) -> None: ...
    def visit_If(self, node: Any) -> None: ...
    def visit_Return(self, node: Any) -> None: ...
    def substitute(self, term: Any, name: Any, substitution: Any): ...
    def parse_conditions(self, var_manager: Any): ...
    def parse_condition(self, node: Any, var_manager: Any): ...
    def parse_expr(self, node: Any, var_manager: Any): ...
    def parse_object(self, obj: Any): ...
    def _dnf(self, node: Any): ...
    def _make_subparser(self, stack: Any): ...

class _Dereferencer(ast.NodeTransformer):
    references: Any = ...
    def __init__(self, references: Any) -> None: ...
    def visit_Name(self, node: Any): ...

class _TransformIfExpReturn(ast.NodeTransformer):
    def visit_Return(self, node: Any): ...

def _unindent(src: Any): ...
