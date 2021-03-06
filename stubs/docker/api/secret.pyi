from .. import errors as errors, utils as utils
from typing import Any

class SecretApiMixin:
    def create_secret(
        self, name, data, labels: Any | None = ..., driver: Any | None = ...
    ): ...
    def inspect_secret(self, id): ...
    def remove_secret(self, id): ...
    def secrets(self, filters: Any | None = ...): ...
