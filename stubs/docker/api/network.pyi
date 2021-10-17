from .. import utils as utils
from ..errors import InvalidVersion as InvalidVersion
from ..utils import (
    check_resource as check_resource,
    minimum_version as minimum_version,
    version_lt as version_lt,
)
from typing import Any

class NetworkApiMixin:
    def networks(
        self, names: Any | None = ..., ids: Any | None = ..., filters: Any | None = ...
    ): ...
    def create_network(
        self,
        name,
        driver: Any | None = ...,
        options: Any | None = ...,
        ipam: Any | None = ...,
        check_duplicate: Any | None = ...,
        internal: bool = ...,
        labels: Any | None = ...,
        enable_ipv6: bool = ...,
        attachable: Any | None = ...,
        scope: Any | None = ...,
        ingress: Any | None = ...,
    ): ...
    def prune_networks(self, filters: Any | None = ...): ...
    def remove_network(self, net_id) -> None: ...
    def inspect_network(
        self, net_id, verbose: Any | None = ..., scope: Any | None = ...
    ): ...
    def connect_container_to_network(
        self,
        container,
        net_id,
        ipv4_address: Any | None = ...,
        ipv6_address: Any | None = ...,
        aliases: Any | None = ...,
        links: Any | None = ...,
        link_local_ips: Any | None = ...,
        driver_opt: Any | None = ...,
    ) -> None: ...
    def disconnect_container_from_network(
        self, container, net_id, force: bool = ...
    ) -> None: ...
