from .. import auth as auth, errors as errors, utils as utils
from ..types import ServiceMode as ServiceMode
from typing import Any

class ServiceApiMixin:
    def create_service(
        self,
        task_template,
        name: Any | None = ...,
        labels: Any | None = ...,
        mode: Any | None = ...,
        update_config: Any | None = ...,
        networks: Any | None = ...,
        endpoint_config: Any | None = ...,
        endpoint_spec: Any | None = ...,
        rollback_config: Any | None = ...,
    ): ...
    def inspect_service(self, service, insert_defaults: Any | None = ...): ...
    def inspect_task(self, task): ...
    def remove_service(self, service): ...
    def services(self, filters: Any | None = ...): ...
    def service_logs(
        self,
        service,
        details: bool = ...,
        follow: bool = ...,
        stdout: bool = ...,
        stderr: bool = ...,
        since: int = ...,
        timestamps: bool = ...,
        tail: str = ...,
        is_tty: Any | None = ...,
    ): ...
    def tasks(self, filters: Any | None = ...): ...
    def update_service(
        self,
        service,
        version,
        task_template: Any | None = ...,
        name: Any | None = ...,
        labels: Any | None = ...,
        mode: Any | None = ...,
        update_config: Any | None = ...,
        networks: Any | None = ...,
        endpoint_config: Any | None = ...,
        endpoint_spec: Any | None = ...,
        fetch_current_spec: bool = ...,
        rollback_config: Any | None = ...,
    ): ...
