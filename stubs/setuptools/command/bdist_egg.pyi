from setuptools import Command as Command
from setuptools.extension import Library as Library
from typing import Any

def strip_module(filename): ...
def sorted_walk(dir) -> None: ...
def write_stub(resource, pyfile) -> None: ...

class bdist_egg(Command):
    description: str
    user_options: Any
    boolean_options: Any
    bdist_dir: Any
    plat_name: Any
    keep_temp: int
    dist_dir: Any
    skip_build: int
    egg_output: Any
    exclude_source_files: Any
    def initialize_options(self) -> None: ...
    egg_info: Any
    def finalize_options(self) -> None: ...
    def do_install_data(self) -> None: ...
    def get_outputs(self): ...
    def call_command(self, cmdname, **kw): ...
    stubs: Any
    def run(self) -> None: ...
    def zap_pyfiles(self) -> None: ...
    def zip_safe(self): ...
    def gen_header(self): ...
    def copy_metadata_to(self, target_dir) -> None: ...
    def get_ext_outputs(self): ...

NATIVE_EXTENSIONS: Any

def walk_egg(egg_dir) -> None: ...
def analyze_egg(egg_dir, stubs): ...
def write_safety_flag(egg_dir, safe) -> None: ...

safety_flags: Any

def scan_module(egg_dir, base, name, stubs): ...
def iter_symbols(code) -> None: ...
def can_scan(): ...

INSTALL_DIRECTORY_ATTRS: Any

def make_zipfile(
    zip_filename,
    base_dir,
    verbose: int = ...,
    dry_run: int = ...,
    compress: bool = ...,
    mode: str = ...,
): ...
