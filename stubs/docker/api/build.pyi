from .. import auth as auth, constants as constants, errors as errors, utils as utils
from typing import Any

log: Any

class BuildApiMixin:
    def build(
        self,
        path: Any | None = ...,
        tag: Any | None = ...,
        quiet: bool = ...,
        fileobj: Any | None = ...,
        nocache: bool = ...,
        rm: bool = ...,
        timeout: Any | None = ...,
        custom_context: bool = ...,
        encoding: Any | None = ...,
        pull: bool = ...,
        forcerm: bool = ...,
        dockerfile: Any | None = ...,
        container_limits: Any | None = ...,
        decode: bool = ...,
        buildargs: Any | None = ...,
        gzip: bool = ...,
        shmsize: Any | None = ...,
        labels: Any | None = ...,
        cache_from: Any | None = ...,
        target: Any | None = ...,
        network_mode: Any | None = ...,
        squash: Any | None = ...,
        extra_hosts: Any | None = ...,
        platform: Any | None = ...,
        isolation: Any | None = ...,
        use_config_proxy: bool = ...,
    ): ...
    def prune_builds(self): ...

def process_dockerfile(dockerfile, path): ...
