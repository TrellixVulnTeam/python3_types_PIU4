from qiime2.core.type.template import PredicateTemplate, TypeTemplate
from typing import Any, Optional

_RESERVED_NAMES: Any

def _validate_name(name: Any) -> None: ...
def SemanticType(name: Any, field_names: Optional[Any] = ..., field_members: Optional[Any] = ..., variant_of: Optional[Any] = ...): ...
def _munge_variant_of(variant_of: Any): ...
def _munge_field_names(field_names: Any): ...
def _munge_field_members(field_names: Any, field_members: Any): ...

class VariantField:
    type_name: Any = ...
    field_name: Any = ...
    field_members: Any = ...
    def __init__(self, type_name: Any, field_name: Any, field_members: Any) -> None: ...
    def is_member(self, semantic_type: Any): ...
    def __repr__(self): ...

class SemanticTemplate(TypeTemplate):
    public_proxy: Any = ...
    name: Any = ...
    field_names: Any = ...
    __field: Any = ...
    variant_of: Any = ...
    def __init__(self, name: Any, field_names: Any, field_members: Any, variant_of: Any) -> None: ...
    @property
    def field(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def get_kind(self): ...
    def get_name(self): ...
    def get_field_names(self): ...
    def is_element_expr(self, self_expr: Any, value: Any): ...
    def is_element(self, value: Any) -> None: ...
    def validate_field(self, name: Any, field: Any) -> None: ...
    def validate_fields_expr(self, self_expr: Any, fields_expr: Any) -> None: ...
    @classmethod
    def is_variant(cls, expr: Any, varf: Any): ...
    def validate_predicate(self, predicate: Any) -> None: ...
    def update_ast(self, ast: Any) -> None: ...

class Properties(PredicateTemplate):
    include: Any = ...
    exclude: Any = ...
    def __init__(self, *include: Any, exclude: Any = ...) -> None: ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __repr__(self): ...
    def is_symbol_subtype(self, other: Any): ...
    def is_symbol_supertype(self, other: Any): ...
    def collapse_intersection(self, other: Any): ...
    def get_kind(self): ...
    def get_name(self): ...
    def is_element(self, expr: Any): ...
    def get_union_membership_expr(self, self_expr: Any): ...
    def update_ast(self, ast: Any) -> None: ...