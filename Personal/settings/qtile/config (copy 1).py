# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
# Copyright (c) 2023 c0deWanted
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import hook, bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
mod1 = "mod1"
mod2 = "control"
mod9 = "shift"
home = os.path.expanduser('~')

terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.Popen([home])

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "n", lazy.layout.next()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left(), lazy.layout.shrink().when(layout=["monadtall", "monadwide"])),
    Key([mod, "control"], "l", lazy.layout.grow_right(), lazy.layout.grow().when(layout=["monadtall", "monadwide"])),
    Key([mod, "control"], "j", lazy.layout.grow_down(), lazy.layout.maximize().when(layout=["monadtall", "monadwide"])),
    Key([mod, "control"], "k", lazy.layout.grow_up(), lazy.layout.normalize().when(layout=["monadtall", "monadwide"])),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
    ),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    Key([mod9], "Shift_R",  lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
]

#MOVE WINDOW TO NEXT SCREEN
def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
])

def init_group_names():
    return [("MAIN", {'layout': 'columns'}),
            ("WWW", {'layout': 'max'}),
            ("BUG", {'layout': 'columns'}),
            ("WRK", {'layout': 'columns'}),
            ("OFF", {'layout': 'columns'}),
            ("VMS", {'layout': 'max'}),
            ("MED", {'layout': 'floating'}),
            ("MAIL", {'layout': 'max'}),
            ("MON", {'layout': 'bsp'}),
            ]

    # return [("    ", {'layout': 'columns'}),
    #         ("    ", {'layout': 'max'}),
    #         ("    ", {'layout': 'monadtall'}),
    #         ("    ", {'layout': 'monadtall'}),
    #         ("    ", {'layout': 'monadtall'}),
    #         ("    ", {'layout': 'max'}),
    #         ("    ", {'layout': 'floating'}),
    #         ("    ", {'layout': 'max'}),
    #         ("    ", {'layout': 'bsp'}),
    #         ]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

# COLORS FOR THE BAR
#Theme name : ArcoLinux Nord
def init_colors():
    return [["#3B4252", "#3B4252"], # color 0 blue-grey
            ["#2e3440", "#2e3440"], # color 1 darker-blue grey
            ["#A3BE8C", "#A3BE8C"], # color 2 light green
            ["#EBCB8B", "#EBCB8B"], # color 3 light yellow
            ["#81A1C1", "#81A1C1"], # color 4 light blue
            ["#D8DEE9", "#D8DEE9"], # color 5 very ligth blue-grey
            ["#88C0D0", "#88C0D0"], # color 6 light blue-cyan
            ["#E5E9F0", "#E5E9F0"], # color 7 lmost same as 5
            ["#4C566A", "#4C566A"], # color 8 blue-grey
            ["#BF616A", "#BF616A"], # color 9 red
            ["#282C34", "#282C34"], # color 10 dark grey - doom one
            ["#937752", "#937752"], # color 11 orange
            ["#939aa1", "#939aa1"], # color 12 light blue-grey (border)
            ["#c6def6", "#c6def6"], # color 13 light blue 5a8f5a
            ["#536653", "#536653"]] # color 14 darker green
colors = init_colors()

def init_layout_theme():
    return {"margin":7,
            "border_width":2,
            "border_focus": colors[12],
            "border_normal": colors[1]
            }

layout_theme = init_layout_theme()

layouts = [
    layout.Columns(margin=3, border_width=2, border_focus=colors[12], border_normal=colors[1]),
    #layout.MonadTall(**layout_theme),
    layout.Bsp(margin=0, border_width=0),
    layout.Floating(**layout_theme),
    layout.Max(margin=16, border_width=0),
    #layout.Tile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
]

widget_defaults = dict(
    font="Noto Sans",
    fontsize=20,
    padding=3,
    background=colors[10]
)
extension_defaults = widget_defaults.copy()
powerline = {
    "decorations": [
        PowerLineDecoration(
            path = 'arrow_right')
    ]
}
screens = [
# Primary screen
    Screen(
         top=bar.Bar(
            [
                widget.GroupBox(font="Noto Sans bold",
                        fontsize = 13,
                        padding = 4,
                        borderwidth = 2,
                        disable_drag = True,
                        active = colors[13],
                        inactive = colors[8],
                        rounded = False,
                        highlight_method = "line",
                        this_current_screen_border = colors[4],
                        other_current_screen_border = colors[2],
                        other_screen_border = colors [14],
                        background = colors[10],
                        ),
                widget.Sep(
                        linewidth = 2,
                        padding = 60,
                        foreground = colors[0],
                        background = colors[10]
                        ),
                widget.Systray(padding = 10),
                widget.Sep(
                        linewidth = 2,
                        padding = 60,
                        foreground = colors[0],
                        background = colors[10]
                        ),
                widget.WindowName(font="Mononoki Nerd Font Mono bold",
                        fontsize = 16,
                        foreground = colors[7],
                        background = colors[10],
                        ),
                widget.CurrentLayout(
                        font = "Mononoki Nerd Font Mono bold",
                        fontsize = 16,
                        foreground = colors[12],
                        background = colors[10]
                        ),
                widget.KeyboardLayout(
                    font = "Noto Sans bold",
                    fontsize = 14,
                    foreground = colors[3],
                    configured_keyboards = ['de', 'ru'],
                    padding = 10,
                ),
                widget.TextBox(
                        font="FontAwesome",
                        text="        ",
                        foreground=colors[11],
                        background=colors[10],
                        padding = 0,
                        fontsize=14
                        ),
                widget.Clock(font = "Noto Sans bold",
                        foreground = colors[5],
                        background = colors[10],
                        fontsize = 16,
                        format=" %Y.%m.%d  "
                        ),
                widget.TextBox(
                        font="FontAwesome",
                        text="    ",
                        foreground=colors[11],
                        background=colors[10],
                        padding = 0,
                        fontsize=18
                        ),
                widget.Clock(font = "Noto Sans bold",
                        foreground = colors[5],
                        background = colors[10],
                        fontsize = 20,
                        format=" %H:%M:%S   "
                        ),
            ],
            size = 24,
            opacity = 0.8
        ),
    ),
# Secondary screen
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(font="Noto Sans bold",
                        fontsize = 18,
                        padding = 4,
                        borderwidth = 2,
                        disable_drag = True,
                        active = colors[13],
                        inactive = colors[8],
                        rounded = False,
                        highlight_method = "line",
                        this_current_screen_border = colors[4],
                        other_current_screen_border = colors[2],
                        other_screen_border = colors [14],
                        background = colors[10],
                        **powerline,
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 1,
                        foreground = colors[0],
                        background = colors[12],
                        **powerline,
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 1,
                        foreground = colors[0],
                        background = colors[0],
                        **powerline,
                        ),
                widget.WindowName(
                        font="Mononoki Nerd Font Mono bold",
                        fontsize = 22,
                        padding = 20,
                        foreground = colors[7],
                        background = colors[10],
                        **powerline,
                        ),
               widget.CurrentLayout(
                        font = "Mononoki Nerd Font Mono bold",
                        fontsize = 26,
                        foreground = colors[10],
                        background = colors[13],
                        **powerline,
                        padding = 20
                        ),
                widget.NvidiaSensors(
                       font = "Mononoki Nerd Font Mono bold",
                       fontsize = 22,
                       foreground = colors[10],
                       foreground_alert = colors[9],
                       background = colors[3],
                       **powerline,
                       padding = 20,
                       format = 'GPU:{temp}°C'
                       ),
                widget.Clock( font = "Noto Sans bold",
                        foreground = colors[5],
                        background = colors[10],
                        **powerline,
                        fontsize = 24,
                        format=" %H:%M:%S   ",
                       ),
            ],
            size = 28,
            opacity = 0.8
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
