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

from typing import Any, Dict, Optional

from docker.api import DockerClient
from docker.models.containers import Container


class Deployment:
    def __init__(
        self,
        client: DockerClient,
        name: str,
        password: str,
        rcon_password: str,
        img_repo: str = DEFAULT_IMAGE_REPO,
        img_tag: str = DEFAULT_IMAGE_TAG,
        local_cfg: Optional[str] = None,
        server_port: int = DEFAULT_SERVER_PORT,
        server_tv_port: int = DEFAULT_SERVER_TV_PORT,
        max_players: int = DEFAULT_MAX_PLAYERS,
        map_group: str = DEFAULT_MAP_GROUP,
        start_map: str = DEFAULT_START_MAP,
        game_mode: GameMode = GameMode.COMPETITIVE,
        game_type: GameType = GameType.CLASSIC,
        tickrate: int = DEFAULT_TICKRATE,
        gameserver_token: Optional[str] = None,
        workshop_key: Optional[str] = None,
    ):
        self._name = name
        self._docker = client

        self._container_name = f"easycsgo_{self._name}"
        self._image_uri = f"{img_repo}:{img_tag}"

        # Server configuration
        self._local_cfg = local_cfg
        self._port = server_port
        self._tv_port = server_tv_port
        self._password = password
        self._rcon_password = rcon_password

        # Game settings
        self._start_map = start_map
        self._map_group = map_group
        self._max_players = max_players
        self._game_mode = game_mode
        self._game_type = game_type
        self._tickrate = tickrate

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
            "SRCDS_RCONPW": self._rcon_password,
            "SRCDS_PW": self._password,
            "SRCDS_PORT": str(self._port),
            "SRCDS_TV_PORT": str(self._tv_port),
            "SRCDS_TICKRATE": str(self._tickrate),
            "SRCDS_MAXPLAYERS": str(self._max_players),
            "SRCDS_STARTMAP": self._start_map,
            "SRCDS_MAPGROUP": self._map_group,
            "SRCDS_MAXPLAYERS": str(self._max_players)
            "SRCDS_GAMETYPE": str(self._game_type.value),
            "SRCDS_GAMEMODE": str(self._game_mode.value),
            "SRCDS_HOSTNAME": self._name,
        }

        use_workshop = self._workshop_key is not None
        env["SRCDS_HOST_WORKSHOP_COLLECTION"] = "1" if use_workshop else "0"
        if use_workshop:
            env["SRCDS_WORKSHOP_AUTHKEY"] = self._workshop_key

        if self._gameserver_token is not None:
            env["SRCDS_TOKEN"] = self._gameserver_token

        return env

    def _volumes(self) -> Dict[str, Dict[str, str]]:
        if self.local_cfg is None:
            return {}

        return {
            CONTAINER_SERVER_PATH: {
                'bind': self._local_cfg,
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
