import distutils.command.install_lib as orig

class install_lib(orig.install_lib):
    def run(self) -> None: ...
    def get_exclusions(self): ...
    def copy_tree(
        self,
        infile,
        outfile,
        preserve_mode: int = ...,
        preserve_times: int = ...,
        preserve_symlinks: int = ...,
        level: int = ...,
    ): ...
    def get_outputs(self): ...