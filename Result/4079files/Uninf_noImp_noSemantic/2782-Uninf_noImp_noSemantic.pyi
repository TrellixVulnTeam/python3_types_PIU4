from typing import Any

def get_root_folder(): ...
def get_build_folder(): ...
def get_dependency_folder(): ...
def get_sdl2_folder(): ...
def get_freetype2_folder(): ...
def get_assimp_folder(): ...
def get_assimp_install_folder(): ...
def get_sdl2_build_folder(): ...
def cmake_project(generator: str) -> Any: ...
def on_cmd_install(arg: Any) -> None: ...
def on_cmd_cmake(arg: Any) -> None: ...
def on_cmd_build(arg: Any) -> None: ...
def run(args: Any) -> str: ...
def on_cmd_test(args: Any) -> None: ...
def add_options(parser: Any) -> None: ...
def main() -> None: ...
