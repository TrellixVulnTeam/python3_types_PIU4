from atcodertools.codegen.code_style_config import CodeStyleConfig
from atcodertools.codegen.models.code_gen_args import CodeGenArgs
from atcodertools.fmtprediction.models.format import Format as Format, Pattern
from atcodertools.fmtprediction.models.type import Type
from atcodertools.fmtprediction.models.variable import Variable
from typing import Any, Dict, Optional

def _loop_header(var: Variable, for_second_index: bool) -> Any: ...

class CppCodeGenerator:
    _format: Any = ...
    _config: Any = ...
    def __init__(self, format_: Optional[Format[Variable]], config: CodeStyleConfig) -> None: ...
    def generate_parameters(self) -> Dict[str, Any]: ...
    def _input_part(self): ...
    def _convert_type(self, type_: Type) -> str: ...
    def _get_declaration_type(self, var: Variable) -> Any: ...
    def _actual_arguments(self) -> str: ...
    def _formal_arguments(self): ...
    def _generate_declaration(self, var: Variable) -> Any: ...
    def _input_code_for_var(self, var: Variable) -> str: ...
    @staticmethod
    def _get_var_name(var: Variable) -> Any: ...
    def _render_pattern(self, pattern: Pattern) -> Any: ...
    def _indent(self, depth: Any): ...

class NoPredictionResultGiven(Exception): ...

def main(args: CodeGenArgs) -> str: ...
