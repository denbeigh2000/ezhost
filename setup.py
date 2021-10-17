#!/usr/bin/python3

from pathlib import Path
from pkg_resources import parse_requirements
from setuptools import setup

REQS_TXT_PATH = Path(__file__).parent / "requirements.txt"

def parse_reqs(path: Path):
    with path.open() as f:
        return [str(r) for r in parse_requirements(f)]


setup(
    name='ezhost',
    version='0.0.0-dev',
    py_modules=['ezhost'],
    install_requires=parse_reqs(REQS_TXT_PATH),
    entry_points={
        'console_scripts': [
            'ezhost = ezhost.cli:cli',
        ],
    },
)
