import http.client as httplib
import socket
import urllib3
from .. import constants as constants
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter
from typing import Any

RecentlyUsedContainer: Any

class SSHSocket(socket.socket):
    host: Any
    port: Any
    user: Any
    proc: Any
    def __init__(self, host) -> None: ...
    def connect(self, **kwargs) -> None: ...
    def sendall(self, data) -> None: ...
    def send(self, data): ...
    def recv(self, n): ...
    def makefile(self, mode): ...
    def close(self) -> None: ...

class SSHConnection(httplib.HTTPConnection):
    ssh_transport: Any
    timeout: Any
    ssh_host: Any
    def __init__(
        self,
        ssh_transport: Any | None = ...,
        timeout: int = ...,
        host: Any | None = ...,
    ) -> None: ...
    sock: Any
    def connect(self) -> None: ...

class SSHConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    scheme: str
    ssh_transport: Any
    timeout: Any
    ssh_host: Any
    def __init__(
        self,
        ssh_client: Any | None = ...,
        timeout: int = ...,
        maxsize: int = ...,
        host: Any | None = ...,
    ) -> None: ...

class SSHHTTPAdapter(BaseHTTPAdapter):
    __attrs__: Any
    ssh_client: Any
    ssh_host: Any
    timeout: Any
    max_pool_size: Any
    pools: Any
    def __init__(
        self,
        base_url,
        timeout: int = ...,
        pool_connections=...,
        max_pool_size=...,
        shell_out: bool = ...,
    ): ...
    def get_connection(self, url, proxies: Any | None = ...): ...
    def close(self) -> None: ...
