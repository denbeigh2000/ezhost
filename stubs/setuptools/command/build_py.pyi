import distutils.command.build_py as orig
from setuptools.lib2to3_ex import Mixin2to3 as Mixin2to3
from typing import Any

class Mixin2to3:
    def run_2to3(self, files, doctests: bool = ...) -> None: ...

def make_writable(target) -> None: ...

class build_py(orig.build_py, Mixin2to3):
    package_data: Any
    exclude_package_data: Any
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    data_files: Any
    def __getattr__(self, attr): ...
    def build_module(self, module, module_file, package): ...
    def find_data_files(self, package, src_dir): ...
    def build_package_data(self) -> None: ...
    manifest_files: Any
    def analyze_manifest(self) -> None: ...
    def get_data_files(self) -> None: ...
    def check_package(self, package, package_dir): ...
    packages_checked: Any
    def initialize_options(self) -> None: ...
    def get_package_dir(self, package): ...
    def exclude_data_files(self, package, src_dir, files): ...

def assert_relative(path): ...