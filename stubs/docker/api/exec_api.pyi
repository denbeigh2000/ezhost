from .. import errors as errors, utils as utils
from typing import Any

class ExecApiMixin:
    def exec_create(
        self,
        container,
        cmd,
        stdout: bool = ...,
        stderr: bool = ...,
        stdin: bool = ...,
        tty: bool = ...,
        privileged: bool = ...,
        user: str = ...,
        environment: Any | None = ...,
        workdir: Any | None = ...,
        detach_keys: Any | None = ...,
    ): ...
    def exec_inspect(self, exec_id): ...
    def exec_resize(
        self, exec_id, height: Any | None = ..., width: Any | None = ...
    ) -> None: ...
    def exec_start(
        self,
        exec_id,
        detach: bool = ...,
        tty: bool = ...,
        stream: bool = ...,
        socket: bool = ...,
        demux: bool = ...,
    ): ...
