import http.client as httplib
import urllib3
from .. import constants as constants
from .npipesocket import NpipeSocket as NpipeSocket
from docker.transport.basehttpadapter import BaseHTTPAdapter as BaseHTTPAdapter
from typing import Any

RecentlyUsedContainer: Any

class NpipeHTTPConnection(httplib.HTTPConnection):
    npipe_path: Any
    timeout: Any
    def __init__(self, npipe_path, timeout: int = ...) -> None: ...
    sock: Any
    def connect(self) -> None: ...

class NpipeHTTPConnectionPool(urllib3.connectionpool.HTTPConnectionPool):
    npipe_path: Any
    timeout: Any
    def __init__(self, npipe_path, timeout: int = ..., maxsize: int = ...) -> None: ...

class NpipeHTTPAdapter(BaseHTTPAdapter):
    __attrs__: Any
    npipe_path: Any
    timeout: Any
    max_pool_size: Any
    pools: Any
    def __init__(
        self, base_url, timeout: int = ..., pool_connections=..., max_pool_size=...
    ): ...
    def get_connection(self, url, proxies: Any | None = ...): ...
    def request_url(self, request, proxies): ...
