from .. import errors as errors
from ..utils import normalize_links as normalize_links, version_lt as version_lt
from typing import Any

class EndpointConfig(dict):
    def __init__(
        self,
        version,
        aliases: Any | None = ...,
        links: Any | None = ...,
        ipv4_address: Any | None = ...,
        ipv6_address: Any | None = ...,
        link_local_ips: Any | None = ...,
        driver_opt: Any | None = ...,
    ) -> None: ...

class NetworkingConfig(dict):
    def __init__(self, endpoints_config: Any | None = ...) -> None: ...

class IPAMConfig(dict):
    def __init__(
        self,
        driver: str = ...,
        pool_configs: Any | None = ...,
        options: Any | None = ...,
    ) -> None: ...

class IPAMPool(dict):
    def __init__(
        self,
        subnet: Any | None = ...,
        iprange: Any | None = ...,
        gateway: Any | None = ...,
        aux_addresses: Any | None = ...,
    ) -> None: ...
