from ezhost.deployment import Deployment, NetworkConfig, VolumeConfig, EnvConfig

from dataclasses import dataclass
from enum import Enum
from typing import Optional

DEFAULT_IMAGE_REPO = "index.docker.io/cm2network/csgo"
DEFAULT_IMAGE_TAG = "latest"

CONTAINER_SERVER_PATH = "/home/steam/csgo-dedicated/csgo/cfg/server.cfg"

DEFAULT_MAP_GROUP = "mg_active"
DEFAULT_MAX_PLAYERS = 14
DEFAULT_START_MAP = "de_dust2"
DEFAULT_TICKRATE = 128

DEFAULT_SERVER_PORT = 27015
DEFAULT_SERVER_TV_PORT = 27020


# See this URL for an explanation of game modes
# https://developer.valvesoftware.com/wiki/CS:GO_Game_Mode_Commands#Game_Type_and_Game_Mode
class GameType(Enum):
    CLASSIC = 0
    GUN_GAME = 1
    TRAINING = 2
    CUSTOM = 3
    COOPERATIVE = 4
    SKIRMISH = 5
    FREE_FOR_ALL = 6


class GameMode(Enum):
    DEFAULT_CASUAL = 0
    COMPETITIVE = 1
    WINGMAN = 2
    WEAPONS_EXPERT = 3


@dataclass
class ServerOptions:
    rcon_password: str
    game_password: Optional[str] = None
    local_cfg: Optional[str] = None
    port: int = DEFAULT_SERVER_PORT
    tv_port: int = DEFAULT_SERVER_TV_PORT


@dataclass
class GameOptions:
    max_players: int = DEFAULT_MAX_PLAYERS
    map_group: str = DEFAULT_MAP_GROUP
    start_map: str = DEFAULT_START_MAP
    game_mode: GameMode = GameMode.COMPETITIVE
    game_type: GameType = GameType.CLASSIC
    tickrate: int = DEFAULT_TICKRATE


@dataclass
class CSGOConfiguration:
    server_options: ServerOptions
    game_options: GameOptions
    gameserver_token: Optional[str] = None
    workshop_key: Optional[str] = None


class CSGODeployment(Deployment):
    def __init__(
        self,
        name: str,
        config: CSGOConfiguration,
        image_repo: str = DEFAULT_IMAGE_REPO,
        image_tag: str = DEFAULT_IMAGE_TAG,
    ):
        self._name = name
        self._config = config
        self._image_repo = image_repo
        self._image_tag = image_tag

    @property
    def name(self):
        return f"csgo_{self._name}"

    @property
    def repo(self) -> str:
        return self._image_repo

    @property
    def tag(self) -> str:
        return self._image_tag

    def env(self) -> Optional[EnvConfig]:
        env = {
            "SRCDS_RCONPW": self._config.server_options.rcon_password,
            "SRCDS_PORT": str(self._config.server_options.port),
            "SRCDS_TV_PORT": str(self._config.server_options.tv_port),
            "SRCDS_TICKRATE": str(self._config.game_options.tickrate),
            "SRCDS_MAXPLAYERS": str(self._config.game_options.max_players),
            "SRCDS_STARTMAP": self._config.game_options.start_map,
            "SRCDS_MAPGROUP": self._config.game_options.map_group,
            "SRCDS_GAMETYPE": str(self._config.game_options.game_type.value),
            "SRCDS_GAMEMODE": str(self._config.game_options.game_mode.value),
            "SRCDS_HOSTNAME": self.name,
        }

        game_pw = self._config.server_options.game_password
        if game_pw is not None:
            env["SRCDS_PW"] = game_pw

        if self._config.workshop_key is not None:
            env["SRCDS_HOST_WORKSHOP_COLLECTION"] = "1"
            env["SRCDS_WORKSHOP_AUTHKEY"] = self._config.workshop_key
        else:
            env["SRCDS_HOST_WORKSHOP_COLLECTION"] = "0"

        if self._config.gameserver_token is not None:
            env["SRCDS_TOKEN"] = self._config.gameserver_token

        return env

    def volumes(self) -> Optional[VolumeConfig]:
        if self._config.server_options.local_cfg is None:
            return None

        return {
            CONTAINER_SERVER_PATH: {
                "bind": self._config.server_options.local_cfg,
                "mode": "ro",
            }
        }

    def networking(self) -> Optional[NetworkConfig]:
        return "host"
