#!/usr/bin/python3

from easycsgo import ConfigNotFound, DEFAULT_CONFIG_PATH
from easycsgo.deployment import Deployment

from pathlib import Path
from typing import Dict, Optional

import docker


class Manager:
    def __init__(
        self,
        client: Optional[docker.api.DockerClient] = None,
        config_dir: Path = DEFAULT_CONFIG_PATH,
    ):
        self._docker = client or docker.from_env()
        self._config_dir = config_dir
        self._used_ports: Dict[int, str] = {}

    def deploy(
        self,
        deployment: Deployment,
    ):
        if cfg_path is None:
            # Attempt to use a config file if one exists with the name locally.
            cfg_path = self._resolve_config_path(cfg_name)

        # deployment = Deployment(self._docker, cfg_name)

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
