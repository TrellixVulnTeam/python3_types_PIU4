from csv import DictReader
from email_hunter import EmailHunterClient
from typing import Any, Optional

THROTTLE: float

def reduce_sources(sources: Any): ...
def validate_search_file(reader: DictReader) -> Any: ...
def validate_generate_file(reader: DictReader) -> Any: ...
def validate_exist_file(reader: DictReader) -> Any: ...
def search(client: EmailHunterClient, domain: Any, offset: Any, type_: Any, print_header: Any=..., is_file_output: Any=...) -> Any: ...
def generate(client: EmailHunterClient, domain: Any, first_name: Any, last_name: Any, print_header: Any=..., is_file_output: Any=...) -> Any: ...
def exist(client: EmailHunterClient, email: Any, print_header: Any=..., is_file_output: Any=...) -> Any: ...
def handle_search_file(client: EmailHunterClient, reader: DictReader) -> Any: ...
def handle_generate_file(client: EmailHunterClient, reader: DictReader) -> Any: ...
def handle_exist_file(client: EmailHunterClient, reader: DictReader) -> Any: ...
def handle_cli(command: Any, api_key: Any, domain: Optional[Any] = ..., offset: int = ..., type: Optional[Any] = ..., first_name: Optional[Any] = ..., last_name: Optional[Any] = ..., email: Optional[Any] = ..., file: Optional[Any] = ...) -> None: ...
def main() -> None: ...
