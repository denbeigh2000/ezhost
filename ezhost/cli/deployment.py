#!/usr/bin/python3

from ezhost import ConfigNotFound
from ezhost.deployment.csgo import (
    CSGOConfiguration,
    CSGODeployment,
    Deployment,
    GameOptions,
    ServerOptions,
)

from functools import update_wrapper
from typing import Any, Dict

import click


def get_deployables() -> Dict[str, Deployment]:
    deployment = CSGODeployment(
        name="default",
        config=CSGOConfiguration(
            server_options=ServerOptions("test123", "test123"),
            game_options=GameOptions(),
        ),
    )

    return {deployment.name: deployment}


def deployment_arg(wrapped: Any) -> Any:
    @click.argument("deployment", type=str, required=True, callback=deployment_arg_callback)
    def wrapper(*args, **kwargs):
        wrapped(*args, **kwargs)

    return update_wrapper(wrapper, wrapped)


def deployment_arg_callback(ctx: click.Context, param: str, value: str) -> Deployment:
    deployables = get_deployables()
    if value in deployables:
        ctx.params['deployment'] = deployables[value]
        return deployables[value]

    raise ConfigNotFound(value)
