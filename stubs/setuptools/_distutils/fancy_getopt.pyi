from distutils.errors import *
from typing import Any

longopt_pat: str
longopt_re: Any
neg_alias_re: Any
longopt_xlate: Any

class FancyGetopt:
    option_table: Any
    option_index: Any
    alias: Any
    negative_alias: Any
    short_opts: Any
    long_opts: Any
    short2long: Any
    attr_name: Any
    takes_arg: Any
    option_order: Any
    def __init__(self, option_table: Any | None = ...) -> None: ...
    def set_option_table(self, option_table) -> None: ...
    def add_option(
        self, long_option, short_option: Any | None = ..., help_string: Any | None = ...
    ) -> None: ...
    def has_option(self, long_option): ...
    def get_attr_name(self, long_option): ...
    def set_aliases(self, alias) -> None: ...
    def set_negative_aliases(self, negative_alias) -> None: ...
    def getopt(self, args: Any | None = ..., object: Any | None = ...): ...
    def get_option_order(self): ...
    def generate_help(self, header: Any | None = ...): ...
    def print_help(self, header: Any | None = ..., file: Any | None = ...) -> None: ...

def fancy_getopt(options, negative_opt, object, args): ...

WS_TRANS: Any

def wrap_text(text, width): ...
def translate_longopt(opt): ...

class OptionDummy:
    def __init__(self, options=...) -> None: ...
