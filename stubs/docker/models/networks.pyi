from ..api import APIClient as APIClient
from ..utils import version_gte as version_gte
from .containers import Container as Container
from .resource import Collection as Collection, Model as Model
from typing import Any

class Network(Model):
    @property
    def name(self): ...
    @property
    def containers(self): ...
    def connect(self, container, *args, **kwargs): ...
    def disconnect(self, container, *args, **kwargs): ...
    def remove(self): ...

class NetworkCollection(Collection):
    model: Any
    def create(self, name, *args, **kwargs): ...
    def get(self, network_id, *args, **kwargs): ...
    def list(self, *args, **kwargs): ...
    def prune(self, filters: Any | None = ...): ...