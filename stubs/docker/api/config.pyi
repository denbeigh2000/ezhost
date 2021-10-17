from .. import utils as utils
from typing import Any

class ConfigApiMixin:
    def create_config(
        self, name, data, labels: Any | None = ..., templating: Any | None = ...
    ): ...
    def inspect_config(self, id): ...
    def remove_config(self, id): ...
    def configs(self, filters: Any | None = ...): ...