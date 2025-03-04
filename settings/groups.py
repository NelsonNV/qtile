# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-dev-terminal, 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-fa-code, 
# nf-md-image, 
# nf-custom-folder_config,
# nf-md-git, 
# nf-fae-telegram
# nf-md-layers

groups = [Group(i) for i in [
    "   ", "  ", "   ", "   ", " 󰋩 ", "   ", " 󰊢  ", "   ", " 󰌨  ",
   
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
