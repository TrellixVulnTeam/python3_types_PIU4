from . import zynthian_engine
from os.path import isdir as isdir
from typing import Any, Optional

class zynthian_engine_csound(zynthian_engine):
    _ctrls: Any = ...
    _ctrl_screens: Any = ...
    type: str = ...
    name: str = ...
    nickname: str = ...
    jackname: str = ...
    preset: str = ...
    preset_config: Any = ...
    bank_dirs: Any = ...
    nogui: bool = ...
    base_command: str = ...
    def __init__(self, zyngui: Optional[Any] = ...) -> None: ...
    def get_bank_list(self, layer: Optional[Any] = ...): ...
    def set_bank(self, layer: Any, bank: Any): ...
    def get_preset_list(self, bank: Any): ...
    command: Any = ...
    def set_preset(self, layer: Any, preset: Any, preload: bool = ...): ...
    def load_preset_config(self, preset_dir: Any): ...
    def get_preset_filepath(self, preset_dir: Any): ...
    def get_fixed_preset_filepath(self, preset_dir: Any): ...
    def cmp_presets(self, preset1: Any, preset2: Any): ...
    def get_controllers_dict(self, layer: Any): ...
