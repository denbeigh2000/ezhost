#!/usr/bin/python3

from enum import Enum
from pathlib import Path

DEFAULT_IMAGE_REPO = "index.docker.io/cm2network/csgo"
DEFAULT_IMAGE_TAG = "latest"

DEFAULT_CONFIG_PATH = Path(__file__) / "../configs"
CONTAINER_SERVER_PATH = "/home/steam/csgo-dedicated/csgo/cfg/server.cfg"

DEFAULT_MAP_GROUP = "mg_active"
DEFAULT_MAX_PLAYERS = 14
DEFAULT_START_MAP = "de_dust2"
DEFAULT_TICKRATE = 128

DEFAULT_SERVER_PORT = 27015
DEFAULT_SERVER_TV_PORT = 27020


class PullPolicy(Enum):
    IF_NOT_PRESENT = 0
    ALWAYS = 1
    NEVER = 2


class EZHostException(Exception):
    pass


class AlreadyRunningException(EZHostException):
    def __init__(self, container_name: str):
        super().__init__(
            self, f"container for config {container_name} is already running"
        )


class NotRunningException(EZHostException):
    def __init__(self, container_name: str):
        super().__init__(self, f"container for config {container_name} is not running")


class ConfigNotFound(EZHostException):
    def __init__(self, config_name: str):
        super().__init__(self, f"config {config_name} could not be found")
