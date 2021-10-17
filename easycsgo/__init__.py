#!/usr/bin/python3

from enum import Enum
from pathlib import Path

DEFAULT_IMAGE_REPO = "index.docker.io/cm2network/csgo"
DEFAULT_IMAGE_TAG = "latest"

CONTATINER_SERVER_PATH = "/home/steam/csgo-dedicated/csgo/cfg/server.cfg"

DEFAULT_CONFIG_PATH = Path(__file__) / "../configs"


class PullPolicy(Enum):
    IF_NOT_PRESENT = 0
    ALWAYS = 1
    NEVER = 2


class EasyCSGOException(Exception):
    pass


class AlreadyRunningException(EasyCSGOException):
    def __init__(self, container_name: str):
        super().__init__(
            self, f"container for config {container_name} is already running"
        )


class NotRunningException(EasyCSGOException):
    def __init__(self, container_name: str):
        super().__init__(self, f"container for config {container_name} is not running")


class ConfigNotFound(EasyCSGOException):
    def __init__(self, config_name: str):
        super().__init__(self, f"config {config_name} could not be found")
