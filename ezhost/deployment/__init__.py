from abc import ABC
from datetime import timedelta
from typing import Dict, List, Literal, Optional, Tuple, Union

from ezhost import PullPolicy

CONTAINER_PREFIX = "ezhost_"
DEFAULT_CONTAINER_TIMEOUT = timedelta(seconds=30)

# https://docker-py.readthedocs.io/en/stable/containers.html#container-objects
SharedHost = Literal["host"]
SinglePort = Optional[int]  # None => random port
InterfacePort = Tuple[str, int]
MultiplePorts = List[int]

PortFwdConfig = Dict[str, Union[SinglePort, InterfacePort, MultiplePorts]]
NetworkConfig = Union[SharedHost, PortFwdConfig]

BindMount = Dict[str, Dict[str, str]]
ManualMount = List[str]
VolumeConfig = Union[BindMount, ManualMount]

EnvConfig = Dict[str, str]


class Deployment(ABC):
    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def image(self) -> str:
        return f"{self.repo}:{self.tag}"

    @property
    def repo(self) -> str:
        raise NotImplementedError

    @property
    def tag(self) -> str:
        raise NotImplementedError

    @property
    def container_name(self) -> str:
        return f"{CONTAINER_PREFIX}{self.name}"

    @property
    def shutdown_timeout(self) -> timedelta:
        return DEFAULT_CONTAINER_TIMEOUT

    @property
    def pull_policy(self) -> Optional[PullPolicy]:
        return None

    def env(self) -> Optional[EnvConfig]:
        return None

    def volumes(self) -> Optional[VolumeConfig]:
        return None

    def networking(self) -> Optional[NetworkConfig]:
        return None
