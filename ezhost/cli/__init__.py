#!/usr/bin/python3

from ezhost import ConfigNotFound
from ezhost.cli.deployment import deployment_arg, find_deployables
from ezhost.cli.manager import build_manager
from ezhost.deployment import Deployment
from ezhost.manager import Manager

from dataclasses import dataclass
from typing import Dict

import click


@click.group()
def cli() -> None:
    pass


@cli.command()
@deployment_arg
@build_manager
def start(manager: Manager, deployment: Deployment) -> None:
    manager.start(deployment)


@dataclass
class DeploymentState:
    name: str
    image: str
    created: bool
    running: bool


@cli.command()
@find_deployables
@build_manager
def ps(manager: Manager, deployments: Dict[str, Deployment]) -> None:
    containers = manager.list_containers()

    if not (containers or deployments):
        click.echo('no deployments found')
        return

    all_deployments: Dict[str, DeploymentState] = {}
    for d in deployments.values():
        all_deployments[d.name] = DeploymentState(name=d.name, image=d.image, created=False, running=False)
    for c in containers:
        name, running = c
        state = all_deployments.get(name)
        if not state:
            continue

        state.created = True
        state.running = running
        all_deployments[name] = state

    for ds in all_deployments.values():
        click.echo(f"{ds.name}@{ds.image} | created: {ds.created}, running: {ds.running}")


@cli.command()
@build_manager
@deployment_arg
def stop(deployment: Deployment, manager: Manager) -> None:
    manager.stop(deployment)


@cli.command()
@build_manager
@deployment_arg
def kill(deployment: Deployment, manager: Manager) -> None:
    pass


@cli.command()
def rm() -> None:
    pass
