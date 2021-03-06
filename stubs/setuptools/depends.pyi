from ._imp import find_module as find_module
from typing import Any

class Require:
    def __init__(
        self,
        name,
        requested_version,
        module,
        homepage: str = ...,
        attribute: Any | None = ...,
        format: Any | None = ...,
    ) -> None: ...
    def full_name(self): ...
    def version_ok(self, version): ...
    def get_version(self, paths: Any | None = ..., default: str = ...): ...
    def is_present(self, paths: Any | None = ...): ...
    def is_current(self, paths: Any | None = ...): ...

def get_module_constant(
    module, symbol, default: int = ..., paths: Any | None = ...
): ...
def extract_constant(code, symbol, default: int = ...): ...
