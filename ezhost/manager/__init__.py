from ezhost import (
    AlreadyRunningException,
    EZHostException,
    NotRunningException,
    PullPolicy,
)
from ezhost.deployment import CONTAINER_PREFIX, Deployment

from typing import Any, Dict, List, Optional, Tuple

from docker import DockerClient
from docker.errors import NotFound
from docker.models.containers import Container


class ImageNotFoundException(EZHostException):
    def __init__(self, repo: str, tag: str):
        super().__init__(self, f"image not found: {repo}@{tag}")


class Manager:
    def __init__(self, client: DockerClient, pull_policy: PullPolicy):
        self._client = client
        self._pull_policy = pull_policy

    def start(self, d: Deployment):
        if self._is_running(d):
            raise AlreadyRunningException(d.name)

        self._maybe_pull(d)
        self._client.containers.run(**self._build_args(d))

    def _maybe_pull(self, d: Deployment):
        policy = d.pull_policy if d.pull_policy is None else self._pull_policy

        if policy == PullPolicy.ALWAYS:
            self._client.images.pull(d.repo, d.tag)
            return
        elif policy == PullPolicy.NEVER:
            return

        try:
            self._client.images.list(d.image)
            return
        except NotFound:
            pass

        try:
            self._client.images.pull(d.repo, d.tag)
        except NotFound:
            raise ImageNotFoundException(d.repo, d.tag)

    def _build_args(self, d: Deployment) -> Dict[str, Any]:
        args = {
            "image": d.image,
            "name": d.container_name,
        }

        env = d.env()
        if env:
            args["environment"] = env

        volumes = d.volumes()
        if volumes:
            args["volumes"] = volumes

        networking = d.networking()
        if networking == "host":
            args["network_mode"] = "host"
        elif networking is not None:
            args["ports"] = networking

        return args

    def stop(self, d: Deployment):
        if not self._is_running(d):
            raise NotRunningException(d.name)

        container = self._find_container(d)
        container.stop(timeout=d.shutdown_timeout().total_seconds())

    def list(self) -> List[Tuple(str, bool)]:
        query_filter = {"name": f"^{CONTAINER_PREFIX}*$"}
        containers = self._client.list(all=True, filters=query_filter)
        return [
            (c.name[len(CONTAINER_PREFIX) :], c.status == "running") for c in containers
        ]

    def _find_container(self, d: Deployment) -> Optional[Container]:
        query_filter = {"name": f"^{d.container_name}$"}
        containers = self._client.list(all=True, filters=query_filter)
        if len(containers) == 0:
            return None

        return containers[0]

    def _is_running(self, d: Deployment) -> bool:
        container = self._find_container(d)
        if not container:
            return False

        return container.status == "running"
