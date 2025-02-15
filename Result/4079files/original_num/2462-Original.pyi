# (generated with --quick)

from typing import Any, Type

FileGenerator: Type[FileGenerator.FileGenerator]
IndentScope: Type[FileGenerator.IndentScope]
TBeautifulCapiParams: Any
TBeautifulCapiRoot: Any
TFunction: Any
TNamespace: Any
TProlog: Any

def create_get_version_component_function(name: str, namespace, params) -> Any: ...
def generate_check_version(out: FileGenerator.FileGenerator, namespace_name: str, shared_library_name: str) -> None: ...
def generate_get_version_component_function(out: FileGenerator.FileGenerator, function_name: str, value) -> None: ...
def generate_get_version_functions(out: FileGenerator.FileGenerator, namespace_name: str, params, api_root) -> None: ...
def get_c_name(name: str) -> str: ...
def get_implementation_name(name: str, namespace_name: str, params) -> str: ...
def process(root_node, params) -> None: ...
def process_namespace(namespace, params) -> None: ...
