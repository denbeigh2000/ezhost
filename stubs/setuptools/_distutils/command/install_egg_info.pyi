from distutils.cmd import Command
from typing import Any

class install_egg_info(Command):
    description: str
    user_options: Any
    install_dir: Any
    def initialize_options(self) -> None: ...
    target: Any
    outputs: Any
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_outputs(self): ...

def safe_name(name): ...
def safe_version(version): ...
def to_filename(name): ...