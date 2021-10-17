#!/usr/bin/python3

from easycsgo import (
    AlreadyRunningException,
    DEFAULT_IMAGE_REPO,
    DEFAULT_IMAGE_TAG,
    NotRunningException,
)

from typing import Optional

from docker.api import DockerClient
from docker.models.containers import Container


class Deployment:
    def __init__(
        self,
        name: str,
        client: DockerClient,
        img_repo: str = DEFAULT_IMAGE_REPO,
        img_tag: str = DEFAULT_IMAGE_TAG,
        local_cfg: Optional[str] = None,
    ):
        self._name = name
        self._docker = client
        self._container_name = f"easycsgo_{self._name}"
        self._image_uri = f"{img_repo}:{img_tag}"

    def _get_container(self) -> Optional[Container]:
        query_filter = {"name": f"^{self._container_name}$"}
        containers = self._docker.list(all=True, filters=query_filter)
        if len(containers) == 0:
            return None

        return containers[0]

    def _is_running(self) -> bool:
        container = self._get_container()
        return container is not None and container.status == "running"

    def start(self):
        if self._is_running():
            raise AlreadyRunningException(self._name)

        self._docker.containers.run(
            image=self._image_uri,
            name=self._container_name,
            detach=True,
        )

    def stop(self):
        if not self._is_running():
            raise NotRunningException(self._name)

        self._get_container().stop()

    def kill(self):
        if not self._is_running():
            raise NotRunningException(self._name)

        self._get_container().kill()
