from HOMELY import HERE as HERE, HOME as HOME, allowinstallingthings as allowinstallingthings, install_nvim_via_apt as install_nvim_via_apt, jerjerrod_addline as jerjerrod_addline, mypips as mypips, need_installpkg as need_installpkg, wantfull as wantfull, wantjerjerrod as wantjerjerrod, wantnvim as wantnvim, whenmissing as whenmissing

VIM_TAG: str
NVIM_TAG: str

def vim_config() -> None: ...
def vim_install() -> None: ...
def nvim_install() -> None: ...
def nvim_devel() -> None: ...
def neovim_python_devel() -> None: ...
def vim_plugin_update() -> None: ...
