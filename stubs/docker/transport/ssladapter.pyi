from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter
from typing import Any

PoolManager: Any

class SSLHTTPAdapter(BaseHTTPAdapter):
    __attrs__: Any
    ssl_version: Any
    assert_hostname: Any
    assert_fingerprint: Any
    def __init__(
        self,
        ssl_version: Any | None = ...,
        assert_hostname: Any | None = ...,
        assert_fingerprint: Any | None = ...,
        **kwargs
    ) -> None: ...
    poolmanager: Any
    def init_poolmanager(self, connections, maxsize, block: bool = ...) -> None: ...
    def get_connection(self, *args, **kwargs): ...
    def can_override_ssl_version(self): ...
