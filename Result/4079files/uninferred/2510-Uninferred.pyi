from app.clients.jenkins_client import JenkinsClient
from app.config.triggear_config import TriggearConfig
from typing import Any

class JenkinsesClients:
    config: Any = ...
    __jenkins_clients: Any = ...
    def __init__(self, config: TriggearConfig) -> None: ...
    def get_jenkins(self, url: str) -> JenkinsClient: ...
    def __setup_jenkins_client(self, url: str) -> None: ...