from .. import errors as errors
from ..utils.utils import (
    convert_port_bindings as convert_port_bindings,
    convert_tmpfs_mounts as convert_tmpfs_mounts,
    convert_volume_binds as convert_volume_binds,
    format_environment as format_environment,
    format_extra_hosts as format_extra_hosts,
    normalize_links as normalize_links,
    parse_bytes as parse_bytes,
    parse_devices as parse_devices,
    split_command as split_command,
    version_gte as version_gte,
    version_lt as version_lt,
)
from .base import DictType as DictType
from .healthcheck import Healthcheck as Healthcheck
from typing import Any

class LogConfigTypesEnum:
    JSON: Any
    SYSLOG: Any
    JOURNALD: Any
    GELF: Any
    FLUENTD: Any
    NONE: Any

class LogConfig(DictType):
    types: Any
    def __init__(self, **kwargs) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, value) -> None: ...
    @property
    def config(self): ...
    def set_config_value(self, key, value) -> None: ...
    def unset_config(self, key) -> None: ...

class Ulimit(DictType):
    def __init__(self, **kwargs) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, value) -> None: ...
    @property
    def soft(self): ...
    @soft.setter
    def soft(self, value) -> None: ...
    @property
    def hard(self): ...
    @hard.setter
    def hard(self, value) -> None: ...

class DeviceRequest(DictType):
    def __init__(self, **kwargs) -> None: ...
    @property
    def driver(self): ...
    @driver.setter
    def driver(self, value) -> None: ...
    @property
    def count(self): ...
    @count.setter
    def count(self, value) -> None: ...
    @property
    def device_ids(self): ...
    @device_ids.setter
    def device_ids(self, value) -> None: ...
    @property
    def capabilities(self): ...
    @capabilities.setter
    def capabilities(self, value) -> None: ...
    @property
    def options(self): ...
    @options.setter
    def options(self, value) -> None: ...

class HostConfig(dict):
    def __init__(
        self,
        version,
        binds: Any | None = ...,
        port_bindings: Any | None = ...,
        lxc_conf: Any | None = ...,
        publish_all_ports: bool = ...,
        links: Any | None = ...,
        privileged: bool = ...,
        dns: Any | None = ...,
        dns_search: Any | None = ...,
        volumes_from: Any | None = ...,
        network_mode: Any | None = ...,
        restart_policy: Any | None = ...,
        cap_add: Any | None = ...,
        cap_drop: Any | None = ...,
        devices: Any | None = ...,
        extra_hosts: Any | None = ...,
        read_only: Any | None = ...,
        pid_mode: Any | None = ...,
        ipc_mode: Any | None = ...,
        security_opt: Any | None = ...,
        ulimits: Any | None = ...,
        log_config: Any | None = ...,
        mem_limit: Any | None = ...,
        memswap_limit: Any | None = ...,
        mem_reservation: Any | None = ...,
        kernel_memory: Any | None = ...,
        mem_swappiness: Any | None = ...,
        cgroup_parent: Any | None = ...,
        group_add: Any | None = ...,
        cpu_quota: Any | None = ...,
        cpu_period: Any | None = ...,
        blkio_weight: Any | None = ...,
        blkio_weight_device: Any | None = ...,
        device_read_bps: Any | None = ...,
        device_write_bps: Any | None = ...,
        device_read_iops: Any | None = ...,
        device_write_iops: Any | None = ...,
        oom_kill_disable: bool = ...,
        shm_size: Any | None = ...,
        sysctls: Any | None = ...,
        tmpfs: Any | None = ...,
        oom_score_adj: Any | None = ...,
        dns_opt: Any | None = ...,
        cpu_shares: Any | None = ...,
        cpuset_cpus: Any | None = ...,
        userns_mode: Any | None = ...,
        uts_mode: Any | None = ...,
        pids_limit: Any | None = ...,
        isolation: Any | None = ...,
        auto_remove: bool = ...,
        storage_opt: Any | None = ...,
        init: Any | None = ...,
        init_path: Any | None = ...,
        volume_driver: Any | None = ...,
        cpu_count: Any | None = ...,
        cpu_percent: Any | None = ...,
        nano_cpus: Any | None = ...,
        cpuset_mems: Any | None = ...,
        runtime: Any | None = ...,
        mounts: Any | None = ...,
        cpu_rt_period: Any | None = ...,
        cpu_rt_runtime: Any | None = ...,
        device_cgroup_rules: Any | None = ...,
        device_requests: Any | None = ...,
    ) -> None: ...

def host_config_type_error(param, param_value, expected): ...
def host_config_version_error(param, version, less_than: bool = ...): ...
def host_config_value_error(param, param_value): ...
def host_config_incompatible_error(param, param_value, incompatible_param): ...

class ContainerConfig(dict):
    def __init__(
        self,
        version,
        image,
        command,
        hostname: Any | None = ...,
        user: Any | None = ...,
        detach: bool = ...,
        stdin_open: bool = ...,
        tty: bool = ...,
        ports: Any | None = ...,
        environment: Any | None = ...,
        volumes: Any | None = ...,
        network_disabled: bool = ...,
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
    ) -> None: ...
