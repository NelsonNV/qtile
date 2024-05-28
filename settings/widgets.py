import os
from libqtile import widget
from .theme import colors
home = os.path.expanduser("~")
# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-fa-caret_left 
        fontsize=37,
        padding=-3.5
    )


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=15,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=0,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        distro ='Arch',
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=60,
    ),

    powerline('color3', 'color4'),

    icon(bg="color3", text=' '),  # Icon: nf-fa-feed

    widget.Net(**base(bg='color3')),

    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text='󰃰 '), # Icon: nf-md-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('color3', 'color1'),

    widget.Systray(background=colors['color3'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

   widget.CPU(format="  {freq_current}GHz {load_percent}%",**base(bg='color4')),#icon: nf-oct-cpu
   
    powerline('color3', 'color4'),

    widget.Memory( measure_mem='G',format="  {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm} " , **base(bg='color3')), # icon:nf-fa-memory

    powerline('color1', 'color3' ),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),
    
    widget.NvidiaSensors(**base(bg='color2'),format=' {temp} '),
 
    powerline('color1', 'color2'),
    widget.Volume(**base(bg='color1'),emoji=False,fmt=' {}',
                emoji_list=[' ',' ',' ',' ']), #nf-fa-volume_xmark,nf-fa-volume_off,nf-fa-volume_down, nf-fa-volume_up

    powerline('grey', 'color1'),
    widget.Net(**base( fg='light' ,bg='grey')),
    
    #powerline('light', 'grey'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14.0,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
