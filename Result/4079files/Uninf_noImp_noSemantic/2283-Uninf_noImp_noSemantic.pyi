from typing import Any, Optional

class Config:
    _path: Any = ...
    _protect_rewrites: bool = ...
    _config: Any = ...
    def __init__(self, path: Any) -> None: ...
    def get_pathdir(self): ...
    pathdir: Any = ...
    def __contains__(self, key: Any): ...
    def __delitem__(self, key: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any): ...
    def __getattr__(self, key: Any): ...
    def __setattr__(self, key: Any, value: Any) -> None: ...
    def _rewrite(self) -> None: ...
    def update(self, d: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def change_file(self, filename: Any) -> None: ...
    def copy_file(self, directory: Optional[Any] = ..., switch: bool = ...) -> None: ...
