import docker.errors
from typing import Any

logger: Any

class ValidationError(Exception): ...
class InvalidImage(ValidationError): ...
class InvalidNetwork(ValidationError): ...

def is_valid_image(docker_client: docker.client.DockerClient, image: str) -> bool: ...
def is_valid_network(docker_client: docker.client.DockerClient, network: str) -> bool: ...