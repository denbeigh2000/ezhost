from distutils.errors import DistutilsPlatformError as DistutilsPlatformError
from typing import Any

def spawn(
    cmd,
    search_path: int = ...,
    verbose: int = ...,
    dry_run: int = ...,
    env: Any | None = ...,
) -> None: ...
def find_executable(executable, path: Any | None = ...): ...
