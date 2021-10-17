#!/usr/bin/python3

from ezhost import ConfigNotFound
from ezhost.cli.deployment import (
    deployment_arg,
    get_deployables,
    deployment_arg_callback,
)
from ezhost.deployment import Deployment
from ezhost.manager import Manager

from dataclasses import dataclass
from typing import Dict

import click


@dataclass
class ApplicationState:
    manager: Manager
    deployable: Dict[str, Deployment]


@click.group()
@click.pass_context
def cli(ctx: click.core.Context) -> None:
    ctx.obj = ApplicationState(
        manager=Manager(),
        deployable=get_deployables(),
    )


@cli.command()
@deployment_arg
@click.pass_obj
def start(obj: ApplicationState, deployment: Deployment) -> None:
    obj.manager.start(deployment)


@dataclass
class DeploymentState:
    name: str
    image: str
    created: bool
    running: bool


@cli.command()
@click.pass_obj
def ps(obj: ApplicationState) -> None:
    manager = obj.manager
    deployments = obj.deployable

    containers = manager.list_containers()

    if not (containers or deployments):
        click.echo("no deployments found")
        return

    all_deployments: Dict[str, DeploymentState] = {}
    for d in deployments.values():
        all_deployments[d.name] = DeploymentState(
            name=d.name, image=d.image, created=False, running=False
        )
    for c in containers:
        name, running = c
        state = all_deployments.get(name)
        if not state:
            continue

        state.created = True
        state.running = running
        all_deployments[name] = state

    for ds in all_deployments.values():
        click.echo(
            f"{ds.name}@{ds.image} | created: {ds.created}, running: {ds.running}"
        )


@cli.command()
@deployment_arg
@click.pass_obj
def stop(obj: ApplicationState, deployment: Deployment) -> None:
    obj.manager.stop(deployment)


@cli.command()
@deployment_arg
def kill(deployment: Deployment) -> None:
    pass


@cli.command()
@click.option("--force/--no-force", is_flag=True, default=False)
@deployment_arg
@click.pass_obj
def rm(obj: ApplicationState, deployment: Deployment, force: bool) -> None:
    obj.manager.rm(deployment, force)
