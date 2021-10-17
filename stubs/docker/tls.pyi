from . import errors as errors
from .transport import SSLHTTPAdapter as SSLHTTPAdapter
from typing import Any

class TLSConfig:
    cert: Any
    ca_cert: Any
    verify: Any
    ssl_version: Any
    assert_hostname: Any
    assert_fingerprint: Any
    def __init__(
        self,
        client_cert: Any | None = ...,
        ca_cert: Any | None = ...,
        verify: Any | None = ...,
        ssl_version: Any | None = ...,
        assert_hostname: Any | None = ...,
        assert_fingerprint: Any | None = ...,
    ) -> None: ...
    def configure_client(self, client) -> None: ...
