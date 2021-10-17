from .. import errors as errors
from ..constants import IS_WINDOWS_PLATFORM as IS_WINDOWS_PLATFORM
from ..utils import (
    check_resource as check_resource,
    convert_service_networks as convert_service_networks,
    format_environment as format_environment,
    format_extra_hosts as format_extra_hosts,
    parse_bytes as parse_bytes,
    split_command as split_command,
)
from typing import Any

class TaskTemplate(dict):
    def __init__(
        self,
        container_spec,
        resources: Any | None = ...,
        restart_policy: Any | None = ...,
        placement: Any | None = ...,
        log_driver: Any | None = ...,
        networks: Any | None = ...,
        force_update: Any | None = ...,
    ) -> None: ...
    @property
    def container_spec(self): ...
    @property
    def resources(self): ...
    @property
    def restart_policy(self): ...
    @property
    def placement(self): ...

class ContainerSpec(dict):
    def __init__(
        self,
        image,
        command: Any | None = ...,
        args: Any | None = ...,
        hostname: Any | None = ...,
        env: Any | None = ...,
        workdir: Any | None = ...,
        user: Any | None = ...,
        labels: Any | None = ...,
        mounts: Any | None = ...,
        stop_grace_period: Any | None = ...,
        secrets: Any | None = ...,
        tty: Any | None = ...,
        groups: Any | None = ...,
        open_stdin: Any | None = ...,
        read_only: Any | None = ...,
        stop_signal: Any | None = ...,
        healthcheck: Any | None = ...,
        hosts: Any | None = ...,
        dns_config: Any | None = ...,
        configs: Any | None = ...,
        privileges: Any | None = ...,
        isolation: Any | None = ...,
        init: Any | None = ...,
        cap_add: Any | None = ...,
        cap_drop: Any | None = ...,
    ) -> None: ...

class Mount(dict):
    def __init__(
        self,
        target,
        source,
        type: str = ...,
        read_only: bool = ...,
        consistency: Any | None = ...,
        propagation: Any | None = ...,
        no_copy: bool = ...,
        labels: Any | None = ...,
        driver_config: Any | None = ...,
        tmpfs_size: Any | None = ...,
        tmpfs_mode: Any | None = ...,
    ) -> None: ...
    @classmethod
    def parse_mount_string(cls, string): ...

class Resources(dict):
    def __init__(
        self,
        cpu_limit: Any | None = ...,
        mem_limit: Any | None = ...,
        cpu_reservation: Any | None = ...,
        mem_reservation: Any | None = ...,
        generic_resources: Any | None = ...,
    ) -> None: ...

class UpdateConfig(dict):
    def __init__(
        self,
        parallelism: int = ...,
        delay: Any | None = ...,
        failure_action: str = ...,
        monitor: Any | None = ...,
        max_failure_ratio: Any | None = ...,
        order: Any | None = ...,
    ) -> None: ...

class RollbackConfig(UpdateConfig): ...

class RestartConditionTypesEnum:
    NONE: Any
    ON_FAILURE: Any
    ANY: Any

class RestartPolicy(dict):
    condition_types: Any
    def __init__(
        self,
        condition=...,
        delay: int = ...,
        max_attempts: int = ...,
        window: int = ...,
    ) -> None: ...

class DriverConfig(dict):
    def __init__(self, name, options: Any | None = ...) -> None: ...

class EndpointSpec(dict):
    def __init__(self, mode: Any | None = ..., ports: Any | None = ...) -> None: ...

def convert_service_ports(ports): ...

class ServiceMode(dict):
    def __init__(self, mode, replicas: Any | None = ...) -> None: ...
    @property
    def mode(self): ...
    @property
    def replicas(self): ...

class SecretReference(dict):
    def __init__(
        self,
        secret_id,
        secret_name,
        filename: Any | None = ...,
        uid: Any | None = ...,
        gid: Any | None = ...,
        mode: int = ...,
    ) -> None: ...

class ConfigReference(dict):
    def __init__(
        self,
        config_id,
        config_name,
        filename: Any | None = ...,
        uid: Any | None = ...,
        gid: Any | None = ...,
        mode: int = ...,
    ) -> None: ...

class Placement(dict):
    def __init__(
        self,
        constraints: Any | None = ...,
        preferences: Any | None = ...,
        platforms: Any | None = ...,
        maxreplicas: Any | None = ...,
    ) -> None: ...

class PlacementPreference(dict):
    def __init__(self, strategy, descriptor) -> None: ...

class DNSConfig(dict):
    def __init__(
        self,
        nameservers: Any | None = ...,
        search: Any | None = ...,
        options: Any | None = ...,
    ) -> None: ...

class Privileges(dict):
    def __init__(
        self,
        credentialspec_file: Any | None = ...,
        credentialspec_registry: Any | None = ...,
        selinux_disable: Any | None = ...,
        selinux_user: Any | None = ...,
        selinux_role: Any | None = ...,
        selinux_type: Any | None = ...,
        selinux_level: Any | None = ...,
    ) -> None: ...

class NetworkAttachmentConfig(dict):
    def __init__(
        self, target, aliases: Any | None = ..., options: Any | None = ...
    ) -> None: ...
