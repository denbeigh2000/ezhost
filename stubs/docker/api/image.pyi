from .. import auth as auth, errors as errors, utils as utils
from ..constants import DEFAULT_DATA_CHUNK_SIZE as DEFAULT_DATA_CHUNK_SIZE
from typing import Any

log: Any

class ImageApiMixin:
    def get_image(self, image, chunk_size=...): ...
    def history(self, image): ...
    def images(
        self,
        name: Any | None = ...,
        quiet: bool = ...,
        all: bool = ...,
        filters: Any | None = ...,
    ): ...
    def import_image(
        self,
        src: Any | None = ...,
        repository: Any | None = ...,
        tag: Any | None = ...,
        image: Any | None = ...,
        changes: Any | None = ...,
        stream_src: bool = ...,
    ): ...
    def import_image_from_data(
        self,
        data,
        repository: Any | None = ...,
        tag: Any | None = ...,
        changes: Any | None = ...,
    ): ...
    def import_image_from_file(
        self,
        filename,
        repository: Any | None = ...,
        tag: Any | None = ...,
        changes: Any | None = ...,
    ): ...
    def import_image_from_stream(
        self,
        stream,
        repository: Any | None = ...,
        tag: Any | None = ...,
        changes: Any | None = ...,
    ): ...
    def import_image_from_url(
        self,
        url,
        repository: Any | None = ...,
        tag: Any | None = ...,
        changes: Any | None = ...,
    ): ...
    def import_image_from_image(
        self,
        image,
        repository: Any | None = ...,
        tag: Any | None = ...,
        changes: Any | None = ...,
    ): ...
    def inspect_image(self, image): ...
    def inspect_distribution(self, image, auth_config: Any | None = ...): ...
    def load_image(self, data, quiet: Any | None = ...): ...
    def prune_images(self, filters: Any | None = ...): ...
    def pull(
        self,
        repository,
        tag: Any | None = ...,
        stream: bool = ...,
        auth_config: Any | None = ...,
        decode: bool = ...,
        platform: Any | None = ...,
        all_tags: bool = ...,
    ): ...
    def push(
        self,
        repository,
        tag: Any | None = ...,
        stream: bool = ...,
        auth_config: Any | None = ...,
        decode: bool = ...,
    ): ...
    def remove_image(self, image, force: bool = ..., noprune: bool = ...): ...
    def search(self, term, limit: Any | None = ...): ...
    def tag(self, image, repository, tag: Any | None = ..., force: bool = ...): ...

def is_file(src): ...
