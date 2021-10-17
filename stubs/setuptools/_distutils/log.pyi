from typing import Any

DEBUG: int
INFO: int
WARN: int
ERROR: int
FATAL: int

class Log:
    threshold: Any
    def __init__(self, threshold=...) -> None: ...
    def log(self, level, msg, *args) -> None: ...
    def debug(self, msg, *args) -> None: ...
    def info(self, msg, *args) -> None: ...
    def warn(self, msg, *args) -> None: ...
    def error(self, msg, *args) -> None: ...
    def fatal(self, msg, *args) -> None: ...

log: Any
debug: Any
info: Any
warn: Any
error: Any
fatal: Any

def set_threshold(level): ...
def set_verbosity(v) -> None: ...