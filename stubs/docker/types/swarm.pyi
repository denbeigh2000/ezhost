from ..errors import InvalidVersion as InvalidVersion
from ..utils import version_lt as version_lt
from typing import Any

class SwarmSpec(dict):
    def __init__(
        self,
        version,
        task_history_retention_limit: Any | None = ...,
        snapshot_interval: Any | None = ...,
        keep_old_snapshots: Any | None = ...,
        log_entries_for_slow_followers: Any | None = ...,
        heartbeat_tick: Any | None = ...,
        election_tick: Any | None = ...,
        dispatcher_heartbeat_period: Any | None = ...,
        node_cert_expiry: Any | None = ...,
        external_cas: Any | None = ...,
        name: Any | None = ...,
        labels: Any | None = ...,
        signing_ca_cert: Any | None = ...,
        signing_ca_key: Any | None = ...,
        ca_force_rotate: Any | None = ...,
        autolock_managers: Any | None = ...,
        log_driver: Any | None = ...,
    ) -> None: ...

class SwarmExternalCA(dict):
    def __init__(
        self,
        url,
        protocol: Any | None = ...,
        options: Any | None = ...,
        ca_cert: Any | None = ...,
    ) -> None: ...
