import subprocess
from google.auth import credentials
from typing import Any, Dict

class DeployNewAppError(Exception): ...

class DeploygaeWorkflow:
    _appengine_service: Any = ...
    def __init__(self, credentials: credentials.Credentials) -> None: ...
    def _create_app(self, project_id: str, region: str) -> Any: ...
    @staticmethod
    def _app_deploy_with_retry(gcloud_path: str, project: str, app_yaml_path: str, env_vars: Dict[str, Any]) -> subprocess.CompletedProcess: ...
    def deploy_gae_app(self, project_id: str, django_directory_path: str, region: str=..., is_new: bool=...) -> str: ...
