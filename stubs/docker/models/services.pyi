from .resource import Collection as Collection, Model as Model
from docker.errors import (
    InvalidArgument as InvalidArgument,
    create_unexpected_kwargs_error as create_unexpected_kwargs_error,
)
from docker.types import (
    ContainerSpec as ContainerSpec,
    Placement as Placement,
    ServiceMode as ServiceMode,
    TaskTemplate as TaskTemplate,
)
from typing import Any

class Service(Model):
    id_attribute: str
    @property
    def name(self): ...
    @property
    def version(self): ...
    def remove(self): ...
    def tasks(self, filters: Any | None = ...): ...
    def update(self, **kwargs): ...
    def logs(self, **kwargs): ...
    def scale(self, replicas): ...
    def force_update(self): ...

class ServiceCollection(Collection):
    model: Any
    def create(self, image, command: Any | None = ..., **kwargs): ...
    def get(self, service_id, insert_defaults: Any | None = ...): ...
    def list(self, **kwargs): ...

CONTAINER_SPEC_KWARGS: Any
TASK_TEMPLATE_KWARGS: Any
CREATE_SERVICE_KWARGS: Any
PLACEMENT_KWARGS: Any