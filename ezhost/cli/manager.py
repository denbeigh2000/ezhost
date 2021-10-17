#!/usr/bin/python3

from ezhost.manager import Manager

from functools import update_wrapper
from typing import Any

import click


def build_manager(f: Any) -> Any:
    @click.pass_context
    def run_with_manager(ctx: click.Context, *args, **kwargs):
        mgr = Manager()
        return ctx.invoke(f, mgr, *args, **kwargs)

    return update_wrapper(run_with_manager, f)

