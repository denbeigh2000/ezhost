from .. import auth as auth, types as types, utils as utils
from typing import Any

class DaemonApiMixin:
    def df(self): ...
    def events(
        self,
        since: Any | None = ...,
        until: Any | None = ...,
        filters: Any | None = ...,
        decode: Any | None = ...,
    ): ...
    def info(self): ...
    def login(
        self,
        username,
        password: Any | None = ...,
        email: Any | None = ...,
        registry: Any | None = ...,
        reauth: bool = ...,
        dockercfg_path: Any | None = ...,
    ): ...
    def ping(self): ...
    def version(self, api_version: bool = ...): ...
