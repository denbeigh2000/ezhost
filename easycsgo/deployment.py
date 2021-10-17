#!/usr/bin/python3

from easycsgo import (
    AlreadyRunningException,
    CONTAINER_SERVER_PATH,
    DEFAULT_IMAGE_REPO,
    DEFAULT_IMAGE_TAG,
    DEFAULT_MAP_GROUP,
    DEFAULT_MAX_PLAYERS,
    DEFAULT_SERVER_PORT,
    DEFAULT_SERVER_TV_PORT,
    DEFAULT_START_MAP,
    DEFAULT_TICKRATE,
    GameMode,
    GameType,
    NotRunningException,
)

from dataclasses import dataclass
from typing import Any, Dict, Optional

from docker.api import DockerClient
from docker.models.containers import Container


@dataclass
class ServerConfig:
    rcon_password: str
    game_password: Optional[str] = None
    local_cfg: Optional[str] = None
    port: int = DEFAULT_SERVER_PORT
    tv_port: int = DEFAULT_SERVER_TV_PORT


@dataclass
class GameSettings:
    max_players: int = DEFAULT_MAX_PLAYERS
    map_group: str = DEFAULT_MAP_GROUP
    start_map: str = DEFAULT_START_MAP
    game_mode: GameMode = GameMode.COMPETITIVE
    game_type: GameType = GameType.CLASSIC
    tickrate: int = DEFAULT_TICKRATE


class Deployment:
    def __init__(
        self,
        client: DockerClient,
        deployment_name: str,
        server_config: ServerConfig,
        game_settings: GameSettings,
        img_repo: str = DEFAULT_IMAGE_REPO,
        img_tag: str = DEFAULT_IMAGE_TAG,
        gameserver_token: Optional[str] = None,
        workshop_key: Optional[str] = None,
    ):
        self._name = deployment_name
        self._docker = client

        self._container_name = f"easycsgo_{self._name}"
        self._image_uri = f"{img_repo}:{img_tag}"

        self._server_config = server_config
        self._game_settings = game_settings

        # Keys
        self._gameserver_token = gameserver_token
        self._workshop_key = workshop_key

    def _get_container(self) -> Optional[Container]:
        query_filter = {"name": f"^{self._container_name}$"}
        containers = self._docker.list(all=True, filters=query_filter)
        if len(containers) == 0:
            return None

        return containers[0]

    def _is_running(self) -> bool:
        container = self._get_container()
        return container is not None and container.status == "running"

    def _env(self) -> Dict[str, str]:
        env = {
            "SRCDS_RCONPW": self._server_config.rcon_password,
            "SRCDS_PORT": str(self._server_config.port),
            "SRCDS_TV_PORT": str(self._server_config.tv_port),
            "SRCDS_TICKRATE": str(self._game_settings.tickrate),
            "SRCDS_MAXPLAYERS": str(self._game_settings.max_players),
            "SRCDS_STARTMAP": self._game_settings.start_map,
            "SRCDS_MAPGROUP": self._game_settings.map_group,
            "SRCDS_GAMETYPE": str(self._game_settings.game_type.value),
            "SRCDS_GAMEMODE": str(self._game_settings.game_mode.value),
            "SRCDS_HOSTNAME": self._name,
        }

        game_pw = self._server_config.game_password
        if game_pw is not None:
            env["SRCDS_PW"] = game_pw

        if self._workshop_key is not None:
            env["SRCDS_HOST_WORKSHOP_COLLECTION"] = "1"
            env["SRCDS_WORKSHOP_AUTHKEY"] = self._workshop_key
        else:
            env["SRCDS_HOST_WORKSHOP_COLLECTION"] = "0"

        if self._gameserver_token is not None:
            env["SRCDS_TOKEN"] = self._gameserver_token

        return env

    def _volumes(self) -> Dict[str, Dict[str, str]]:
        if self._server_config.local_cfg is None:
            return {}

        return {
            CONTAINER_SERVER_PATH: {
                'bind': self._server_config.local_cfg,
                'mode': 'ro',
            }
        }

    def start(self):
        if self._is_running():
            raise AlreadyRunningException(self._name)

        # TODO: The docker hub README says I should limit this to a specifc set of
        # CPUs/threads by using --cpuset-cpus. I will probably do this if I end
        # up running it on a beefier machine(?)
        self._docker.containers.run(
            image=self._image_uri,
            name=self._container_name,
            detach=True,
            volumes=self._volumes(),
            environment=self._env(),
            # TODO: Consider looking up the external IP to stop using net=host.
            # We make assumptions about running on the host in other places for
            # things like locally-bound files.
            network_mode="host",
        )

    def stop(self):
        if not self._is_running():
            raise NotRunningException(self._name)

        self._get_container().stop()

    def kill(self):
        if not self._is_running():
            raise NotRunningException(self._name)

        self._get_container().kill()
