from . import credentials as credentials, errors as errors
from .utils import config as config
from typing import Any

INDEX_NAME: str
INDEX_URL: Any
TOKEN_USERNAME: str
log: Any

def resolve_repository_name(repo_name): ...
def resolve_index_name(index_name): ...
def get_config_header(client, registry): ...
def split_repo_name(repo_name): ...
def get_credential_store(authconfig, registry): ...

class AuthConfig(dict):
    def __init__(self, dct, credstore_env: Any | None = ...) -> None: ...
    @classmethod
    def parse_auth(cls, entries, raise_on_error: bool = ...): ...
    @classmethod
    def load_config(cls, config_path, config_dict, credstore_env: Any | None = ...): ...
    @property
    def auths(self): ...
    @property
    def creds_store(self): ...
    @property
    def cred_helpers(self): ...
    @property
    def is_empty(self): ...
    def resolve_authconfig(self, registry: Any | None = ...): ...
    def get_credential_store(self, registry): ...
    def get_all_credentials(self): ...
    def add_auth(self, reg, data) -> None: ...

def resolve_authconfig(
    authconfig, registry: Any | None = ..., credstore_env: Any | None = ...
): ...
def convert_to_hostname(url): ...
def decode_auth(auth): ...
def encode_header(auth): ...
def parse_auth(entries, raise_on_error: bool = ...): ...
def load_config(
    config_path: Any | None = ...,
    config_dict: Any | None = ...,
    credstore_env: Any | None = ...,
): ...
