import typing as t
from typing import Any

__updated__: str
SETUP_TEMPLATE: str
HERE: Any

def find_version(package_name: str, version_module_name: str=..., version_variable_name: str=...) -> str: ...
def find_packages(root_directory: str=...) -> t.List[str]: ...
def parse_requirements(requirements_path: str=...) -> t.List[str]: ...
def partition_version_classifiers(classifiers: t.Sequence[str], version_prefix: str=..., only_suffix: str=...) -> t.Tuple[t.List[str], t.List[str]]: ...
def find_required_python_version(classifiers: t.Sequence[str], version_prefix: str=..., only_suffix: str=...) -> t.Optional[str]: ...
def resolve_relative_rst_links(text: str, base_link: str) -> Any: ...

class Package:
    root_directory: str = ...
    name: str = ...
    version: str = ...
    description: str = ...
    long_description: str = ...
    long_description_content_type: str = ...
    url: str = ...
    download_url: str = ...
    author: str = ...
    author_email: str = ...
    license_str: str = ...
    classifiers: t.List[str] = ...
    keywords: t.List[str] = ...
    packages: t.List[str] = ...
    package_data: Any = ...
    exclude_package_data: Any = ...
    install_requires: t.List[str] = ...
    extras_require: t.Mapping[str, t.List[str]] = ...
    python_requires: str = ...
    entry_points: t.Mapping[str, t.List[str]] = ...
    test_suite: str = ...
    @classmethod
    def try_fields(cls: Any, *names: Any) -> t.Optional[t.Any]: ...
    @classmethod
    def parse_readme(cls: Any, readme_path: str=..., encoding: str=...) -> t.Tuple[str, str]: ...
    @classmethod
    def prepare(cls: Any) -> None: ...
    @classmethod
    def setup(cls: Any) -> None: ...
