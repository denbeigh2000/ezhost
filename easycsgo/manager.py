#!/usr/bin/python3

from easycsgo import DEFAULT_CONFIG_PATH

from pathlib import Path
from typing import Optional

import docker


class Manager:
    def __init__(
        self,
        client: Optional[docker.api.DockerClient] = None,
        config_dir: Path = DEFAULT_CONFIG_PATH,
    ):
        self._docker = client or docker.from_env()
        self._config_dir = config_dir

    def deploy(self, config: str, cfg: Optional[Path] = None):
        if cfg is None:
            cfg = self._resolve_config_path(config)

        if cfg is None:
            raise ConnectionAbortedError

    def _resolve_config_path(self, name: str) -> Optional[Path]:
        path = Path(name)
        if path.is_absolute():
            return path if path.exists() else None

        path = self._config_dir / name
        if path.exists():
            return path

        if path.name.endswith(".cfg"):
            return None

        path = path.parent / (path.name + ".cfg")
        return path if path.exists() else None
