from .. import errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from ..types import (
    CancellableStream as CancellableStream,
    ContainerConfig as ContainerConfig,
    EndpointConfig as EndpointConfig,
    HostConfig as HostConfig,
    NetworkingConfig as NetworkingConfig,
)
from typing import Any

class ContainerApiMixin:
    def attach(
        self,
        container,
        stdout: bool = ...,
        stderr: bool = ...,
        stream: bool = ...,
        logs: bool = ...,
        demux: bool = ...,
    ): ...
    def attach_socket(self, container, params: Any | None = ..., ws: bool = ...): ...
    def commit(
        self,
        container,
        repository: Any | None = ...,
        tag: Any | None = ...,
        message: Any | None = ...,
        author: Any | None = ...,
        changes: Any | None = ...,
        conf: Any | None = ...,
    ): ...
    def containers(
        self,
        quiet: bool = ...,
        all: bool = ...,
        trunc: bool = ...,
        latest: bool = ...,
        since: Any | None = ...,
        before: Any | None = ...,
        limit: int = ...,
        size: bool = ...,
        filters: Any | None = ...,
    ): ...
    def create_container(
        self,
        image,
        command: Any | None = ...,
        hostname: Any | None = ...,
        user: Any | None = ...,
        detach: bool = ...,
        stdin_open: bool = ...,
        tty: bool = ...,
        ports: Any | None = ...,
        environment: Any | None = ...,
        volumes: Any | None = ...,
        network_disabled: bool = ...,
        name: Any | None = ...,
        entrypoint: Any | None = ...,
        working_dir: Any | None = ...,
        domainname: Any | None = ...,
        host_config: Any | None = ...,
        mac_address: Any | None = ...,
        labels: Any | None = ...,
        stop_signal: Any | None = ...,
        networking_config: Any | None = ...,
        healthcheck: Any | None = ...,
        stop_timeout: Any | None = ...,
        runtime: Any | None = ...,
        use_config_proxy: bool = ...,
    ): ...
    def create_container_config(self, *args, **kwargs): ...
    def create_container_from_config(self, config, name: Any | None = ...): ...
    def create_host_config(self, *args, **kwargs): ...
    def create_networking_config(self, *args, **kwargs): ...
    def create_endpoint_config(self, *args, **kwargs): ...
    def diff(self, container): ...
    def export(self, container, chunk_size=...): ...
    def get_archive(
        self, container, path, chunk_size=..., encode_stream: bool = ...
    ): ...
    def inspect_container(self, container): ...
    def kill(self, container, signal: Any | None = ...) -> None: ...
    def logs(
        self,
        container,
        stdout: bool = ...,
        stderr: bool = ...,
        stream: bool = ...,
        timestamps: bool = ...,
        tail: str = ...,
        since: Any | None = ...,
        follow: Any | None = ...,
        until: Any | None = ...,
    ): ...
    def pause(self, container) -> None: ...
    def port(self, container, private_port): ...
    def put_archive(self, container, path, data): ...
    def prune_containers(self, filters: Any | None = ...): ...
    def remove_container(
        self, container, v: bool = ..., link: bool = ..., force: bool = ...
    ) -> None: ...
    def rename(self, container, name) -> None: ...
    def resize(self, container, height, width) -> None: ...
    def restart(self, container, timeout: int = ...) -> None: ...
    def start(self, container, *args, **kwargs) -> None: ...
    def stats(self, container, decode: Any | None = ..., stream: bool = ...): ...
    def stop(self, container, timeout: Any | None = ...) -> None: ...
    def top(self, container, ps_args: Any | None = ...): ...
    def unpause(self, container) -> None: ...
    def update_container(
        self,
        container,
        blkio_weight: Any | None = ...,
        cpu_period: Any | None = ...,
        cpu_quota: Any | None = ...,
        cpu_shares: Any | None = ...,
        cpuset_cpus: Any | None = ...,
        cpuset_mems: Any | None = ...,
        mem_limit: Any | None = ...,
        mem_reservation: Any | None = ...,
        memswap_limit: Any | None = ...,
        kernel_memory: Any | None = ...,
        restart_policy: Any | None = ...,
    ): ...
    def wait(
        self, container, timeout: Any | None = ..., condition: Any | None = ...
    ): ...
