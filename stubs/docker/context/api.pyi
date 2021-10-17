from docker import errors as errors
from docker.context import Context as Context
from docker.context.config import (
    METAFILE as METAFILE,
    get_current_context_name as get_current_context_name,
    get_meta_dir as get_meta_dir,
    write_context_name_to_docker_config as write_context_name_to_docker_config,
)
from typing import Any

class ContextAPI:
    DEFAULT_CONTEXT: Any
    @classmethod
    def create_context(
        cls,
        name,
        orchestrator: Any | None = ...,
        host: Any | None = ...,
        tls_cfg: Any | None = ...,
        default_namespace: Any | None = ...,
        skip_tls_verify: bool = ...,
    ): ...
    @classmethod
    def get_context(cls, name: Any | None = ...): ...
    @classmethod
    def contexts(cls): ...
    @classmethod
    def get_current_context(cls): ...
    @classmethod
    def set_current_context(cls, name: str = ...) -> None: ...
    @classmethod
    def remove_context(cls, name) -> None: ...
    @classmethod
    def inspect_context(cls, name: str = ...): ...
