from typing import Any

class OptionHelpInfo:
    def comma_separated_display_args(self): ...

class OptionScopeHelpInfo: ...

class HelpInfoExtracter:
    @classmethod
    def get_option_scope_help_info_from_parser(cls, parser: Any): ...
    @staticmethod
    def compute_default(kwargs: Any): ...
    @staticmethod
    def compute_metavar(kwargs: Any): ...
    _scope: Any = ...
    _scope_prefix: Any = ...
    def __init__(self, scope: Any) -> None: ...
    def get_option_scope_help_info(self, option_registrations_iter: Any): ...
    def get_option_help_info(self, args: Any, kwargs: Any): ...
