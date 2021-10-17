import packaging
from pkgutil import get_importer as get_importer
from typing import Any, NamedTuple

FileExistsError = OSError
require: Any
working_set: Any
add_activation_listener: Any
cleanup_resources: Any
resource_stream: Any
set_extraction_path: Any
resource_isdir: Any
resource_string: Any
iter_entry_points: Any
resource_listdir: Any
resource_filename: Any
resource_exists: Any

class PEP440Warning(RuntimeWarning): ...

def parse_version(v): ...

class ResolutionError(Exception): ...

class VersionConflict(ResolutionError):
    @property
    def dist(self): ...
    @property
    def req(self): ...
    def report(self): ...
    def with_context(self, required_by): ...

class ContextualVersionConflict(VersionConflict):
    @property
    def required_by(self): ...

class DistributionNotFound(ResolutionError):
    @property
    def req(self): ...
    @property
    def requirers(self): ...
    @property
    def requirers_str(self): ...
    def report(self): ...

class UnknownExtra(ResolutionError): ...

EGG_DIST: int
BINARY_DIST: int
SOURCE_DIST: int
CHECKOUT_DIST: int
DEVELOP_DIST: int

def register_loader_type(loader_type, provider_factory) -> None: ...
def get_provider(moduleOrReq): ...

get_platform = get_build_platform

def compatible_platforms(provided, required): ...
def run_script(dist_spec, script_name) -> None: ...

run_main = run_script

def get_distribution(dist): ...
def load_entry_point(dist, group, name): ...
def get_entry_map(dist, group: Any | None = ...): ...
def get_entry_info(dist, group, name): ...

class IMetadataProvider:
    def has_metadata(name) -> None: ...
    def get_metadata(name) -> None: ...
    def get_metadata_lines(name) -> None: ...
    def metadata_isdir(name) -> None: ...
    def metadata_listdir(name) -> None: ...
    def run_script(script_name, namespace) -> None: ...

class IResourceProvider(IMetadataProvider):
    def get_resource_filename(manager, resource_name) -> None: ...
    def get_resource_stream(manager, resource_name) -> None: ...
    def get_resource_string(manager, resource_name) -> None: ...
    def has_resource(resource_name) -> None: ...
    def resource_isdir(resource_name) -> None: ...
    def resource_listdir(resource_name) -> None: ...

class WorkingSet:
    entries: Any
    entry_keys: Any
    by_key: Any
    callbacks: Any
    def __init__(self, entries: Any | None = ...) -> None: ...
    def add_entry(self, entry) -> None: ...
    def __contains__(self, dist): ...
    def find(self, req): ...
    def iter_entry_points(self, group, name: Any | None = ...): ...
    def run_script(self, requires, script_name) -> None: ...
    def __iter__(self): ...
    def add(
        self, dist, entry: Any | None = ..., insert: bool = ..., replace: bool = ...
    ) -> None: ...
    def resolve(
        self,
        requirements,
        env: Any | None = ...,
        installer: Any | None = ...,
        replace_conflicting: bool = ...,
        extras: Any | None = ...,
    ): ...
    def find_plugins(
        self,
        plugin_env,
        full_env: Any | None = ...,
        installer: Any | None = ...,
        fallback: bool = ...,
    ): ...
    def require(self, *requirements): ...
    def subscribe(self, callback, existing: bool = ...) -> None: ...

class _ReqExtras(dict):
    def markers_pass(self, req, extras: Any | None = ...): ...

class Environment:
    platform: Any
    python: Any
    def __init__(
        self, search_path: Any | None = ..., platform=..., python=...
    ) -> None: ...
    def can_add(self, dist): ...
    def remove(self, dist) -> None: ...
    def scan(self, search_path: Any | None = ...) -> None: ...
    def __getitem__(self, project_name): ...
    def add(self, dist) -> None: ...
    def best_match(
        self,
        req,
        working_set,
        installer: Any | None = ...,
        replace_conflicting: bool = ...,
    ): ...
    def obtain(self, requirement, installer: Any | None = ...): ...
    def __iter__(self): ...
    def __iadd__(self, other): ...
    def __add__(self, other): ...

AvailableDistributions = Environment

class ExtractionError(RuntimeError): ...

class ResourceManager:
    extraction_path: Any
    cached_files: Any
    def __init__(self) -> None: ...
    def resource_exists(self, package_or_requirement, resource_name): ...
    def resource_isdir(self, package_or_requirement, resource_name): ...
    def resource_filename(self, package_or_requirement, resource_name): ...
    def resource_stream(self, package_or_requirement, resource_name): ...
    def resource_string(self, package_or_requirement, resource_name): ...
    def resource_listdir(self, package_or_requirement, resource_name): ...
    def extraction_error(self) -> None: ...
    def get_cache_path(self, archive_name, names=...): ...
    def postprocess(self, tempname, filename) -> None: ...
    def set_extraction_path(self, path) -> None: ...
    def cleanup_resources(self, force: bool = ...) -> None: ...

def get_default_cache(): ...
def safe_name(name): ...
def safe_version(version): ...
def safe_extra(extra): ...
def to_filename(name): ...
def invalid_marker(text): ...
def evaluate_marker(text, extra: Any | None = ...): ...

class NullProvider:
    egg_name: Any
    egg_info: Any
    loader: Any
    module_path: Any
    def __init__(self, module) -> None: ...
    def get_resource_filename(self, manager, resource_name): ...
    def get_resource_stream(self, manager, resource_name): ...
    def get_resource_string(self, manager, resource_name): ...
    def has_resource(self, resource_name): ...
    def has_metadata(self, name): ...
    def get_metadata(self, name): ...
    def get_metadata_lines(self, name): ...
    def resource_isdir(self, resource_name): ...
    def metadata_isdir(self, name): ...
    def resource_listdir(self, resource_name): ...
    def metadata_listdir(self, name): ...
    def run_script(self, script_name, namespace) -> None: ...

class EggProvider(NullProvider):
    def __init__(self, module) -> None: ...

class DefaultProvider(EggProvider):
    def get_resource_stream(self, manager, resource_name): ...

class EmptyProvider(NullProvider):
    module_path: Any
    def __init__(self) -> None: ...

empty_provider: Any

class ZipManifests(dict):
    @classmethod
    def build(cls, path): ...
    load: Any

class MemoizedZipManifests(ZipManifests):
    class manifest_mod(NamedTuple):
        manifest: Any
        mtime: Any
    def load(self, path): ...

class ZipProvider(EggProvider):
    eagers: Any
    zip_pre: Any
    def __init__(self, module) -> None: ...
    @property
    def zipinfo(self): ...
    def get_resource_filename(self, manager, resource_name): ...

class FileMetadata(EmptyProvider):
    path: Any
    def __init__(self, path) -> None: ...
    def has_metadata(self, name): ...
    def get_metadata(self, name): ...
    def get_metadata_lines(self, name): ...

class PathMetadata(DefaultProvider):
    module_path: Any
    egg_info: Any
    def __init__(self, path, egg_info) -> None: ...

class EggMetadata(ZipProvider):
    zip_pre: Any
    loader: Any
    module_path: Any
    def __init__(self, importer) -> None: ...

def register_finder(importer_type, distribution_finder) -> None: ...
def find_distributions(path_item, only: bool = ...): ...

class NoDists:
    def __bool__(self): ...
    def __call__(self, fullpath): ...

def register_namespace_handler(importer_type, namespace_handler) -> None: ...
def declare_namespace(packageName) -> None: ...
def fixup_namespace_packages(path_item, parent: Any | None = ...) -> None: ...
def normalize_path(filename): ...
def yield_lines(strs) -> None: ...

class EntryPoint:
    name: Any
    module_name: Any
    attrs: Any
    extras: Any
    dist: Any
    def __init__(
        self, name, module_name, attrs=..., extras=..., dist: Any | None = ...
    ) -> None: ...
    def load(self, require: bool = ..., *args, **kwargs): ...
    def resolve(self): ...
    def require(self, env: Any | None = ..., installer: Any | None = ...) -> None: ...
    pattern: Any
    @classmethod
    def parse(cls, src, dist: Any | None = ...): ...
    @classmethod
    def parse_group(cls, group, lines, dist: Any | None = ...): ...
    @classmethod
    def parse_map(cls, data, dist: Any | None = ...): ...

class Distribution:
    PKG_INFO: str
    project_name: Any
    py_version: Any
    platform: Any
    location: Any
    precedence: Any
    def __init__(
        self,
        location: Any | None = ...,
        metadata: Any | None = ...,
        project_name: Any | None = ...,
        version: Any | None = ...,
        py_version=...,
        platform: Any | None = ...,
        precedence=...,
    ) -> None: ...
    @classmethod
    def from_location(cls, location, basename, metadata: Any | None = ..., **kw): ...
    @property
    def hashcmp(self): ...
    def __hash__(self): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @property
    def key(self): ...
    @property
    def parsed_version(self): ...
    @property
    def version(self): ...
    def requires(self, extras=...): ...
    def activate(self, path: Any | None = ..., replace: bool = ...) -> None: ...
    def egg_name(self): ...
    def __getattr__(self, attr): ...
    def __dir__(self): ...
    @classmethod
    def from_filename(cls, filename, metadata: Any | None = ..., **kw): ...
    def as_requirement(self): ...
    def load_entry_point(self, group, name): ...
    def get_entry_map(self, group: Any | None = ...): ...
    def get_entry_info(self, group, name): ...
    def insert_on(self, path, loc: Any | None = ..., replace: bool = ...) -> None: ...
    def check_version_conflict(self) -> None: ...
    def has_version(self): ...
    def clone(self, **kw): ...
    @property
    def extras(self): ...

class EggInfoDistribution(Distribution): ...

class DistInfoDistribution(Distribution):
    PKG_INFO: str
    EQEQ: Any

def parse_requirements(strs) -> None: ...

class RequirementParseError(packaging.requirements.InvalidRequirement): ...

class Requirement(packaging.requirements.Requirement):
    unsafe_name: Any
    specs: Any
    extras: Any
    hashCmp: Any
    def __init__(self, requirement_string) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __contains__(self, item): ...
    def __hash__(self): ...
    @staticmethod
    def parse(s): ...

def ensure_directory(path) -> None: ...
def split_sections(s) -> None: ...

class PkgResourcesDeprecationWarning(Warning): ...