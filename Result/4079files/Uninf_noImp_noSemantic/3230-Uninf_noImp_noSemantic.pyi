from typing import Any

SITE_NAME: str
PUBLISH_PATH: Any
PREVIEW_PATH: Any
LOCAL_REPOSITORY_PATH: Any
REPOSITORY_PATH: str
WIPE_PROMPT: str
LOCK_PATH: str
DEFAULT_PATH_KWARGS: Any

class Config:
    site_name: Any = ...
    publish_path: Any = ...
    preview_path: Any = ...
    local_repo_path: Any = ...
    repo_path: Any = ...
    author_name: Any = ...
    def __init__(self) -> None: ...
    @property
    def author_email(self): ...

pass_config: Any

def main(config: Any, site_name: Any, publish_path: Any, repo_path: Any) -> None: ...
def init(config: Any, local_repo_path: Any, preview_path: Any) -> None: ...
def preview(config: Any, preview_path: Any, local_repo_path: Any) -> None: ...
def _on_create(file_path: str) -> None: ...
def publish(config: Any, local_repo_path: Any) -> None: ...
def get(config: Any, preview: Any, preview_path: Any, path: Any) -> None: ...
def sync(config: Any, local_repo_path: Any) -> None: ...
def _preview(preview_path: Any, local_repo_path: Any) -> None: ...
def clear_directory(path: str) -> None: ...