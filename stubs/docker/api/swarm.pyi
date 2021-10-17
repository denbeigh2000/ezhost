from .. import errors as errors, types as types, utils as utils
from ..constants import (
    DEFAULT_SWARM_ADDR_POOL as DEFAULT_SWARM_ADDR_POOL,
    DEFAULT_SWARM_SUBNET_SIZE as DEFAULT_SWARM_SUBNET_SIZE,
)
from typing import Any

log: Any

class SwarmApiMixin:
    def create_swarm_spec(self, *args, **kwargs): ...
    def get_unlock_key(self): ...
    def init_swarm(
        self,
        advertise_addr: Any | None = ...,
        listen_addr: str = ...,
        force_new_cluster: bool = ...,
        swarm_spec: Any | None = ...,
        default_addr_pool: Any | None = ...,
        subnet_size: Any | None = ...,
        data_path_addr: Any | None = ...,
    ): ...
    def inspect_swarm(self): ...
    def inspect_node(self, node_id): ...
    def join_swarm(
        self,
        remote_addrs,
        join_token,
        listen_addr: str = ...,
        advertise_addr: Any | None = ...,
        data_path_addr: Any | None = ...,
    ): ...
    def leave_swarm(self, force: bool = ...): ...
    def nodes(self, filters: Any | None = ...): ...
    def remove_node(self, node_id, force: bool = ...): ...
    def unlock_swarm(self, key): ...
    def update_node(self, node_id, version, node_spec: Any | None = ...): ...
    def update_swarm(
        self,
        version,
        swarm_spec: Any | None = ...,
        rotate_worker_token: bool = ...,
        rotate_manager_token: bool = ...,
        rotate_manager_unlock_key: bool = ...,
    ): ...
