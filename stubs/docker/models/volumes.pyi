from ..api import APIClient as APIClient
from .resource import Collection as Collection, Model as Model
from typing import Any

class Volume(Model):
    id_attribute: str
    @property
    def name(self): ...
    def remove(self, force: bool = ...): ...

class VolumeCollection(Collection):
    model: Any
    def create(self, name: Any | None = ..., **kwargs): ...
    def get(self, volume_id): ...
    def list(self, **kwargs): ...
    def prune(self, filters: Any | None = ...): ...