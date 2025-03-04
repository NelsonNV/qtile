# Qtile Config File
# http://www.qtile.org/

# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles


from libqtile import hook

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.mouse import mouse
from settings.path import qtile_path

from os import path
import subprocess
from libqtile.log_utils import logger
import asyncio

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

@hook.subscribe.client_managed
async def restack_polkit(client):
    if "polkit-kde-authentication-agent-1" in client.get_wm_class():
        await asyncio.sleep(0.1)
        client.bring_to_front()
    if "xfce-polkit" in client.get_wm_class():
        await asyncio.sleep(0.1)
        client.bring_to_front()
    if "polkit-gnome" in client.get_wm_class():
        await asyncio.sleep(0.1)
        client.bring_to_front()

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True 
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'
