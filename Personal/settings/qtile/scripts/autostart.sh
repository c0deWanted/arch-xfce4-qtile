#!/bin/bash
#
#
picom --config $HOME/.config/qtile/scripts/picom.conf &
#Set your native resolution IF it does not exist in xrandr
#More info in the script
#run $HOME/.config/qtile/scripts/set-screen-resolution-in-virtualbox.sh

#The following will set you screen resolution to full HD at qtile start
#Find out your monitor name with xrandr or arandr and replace it.
#There are a few examples btw
#xrandr -s 1920x1080
# vbox vm
#xrandr --output Virtual-1 --primary --mode 2560x1440 --rate 60.00 &
xrandr --output LVDS1 --mode 1366x768 --rate 60.00 &
#xrandr --output VGA-1 --primary --mode 1360x768 --pos 0x0 --rotate normal
#xrandr --output DP2 --primary --mode 1920x1080 --rate 60.00 --output LVDS1 --off &
#xrandr --output LVDS1 --mode 1366x768 --output DP3 --mode 1920x1080 --right-of LVDS1
#xrandr --output HDMI2 --mode 1920x1080 --pos 1920x0 --rotate normal --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output VIRTUAL1 --off
#
#xrandr --output DP-4 --gamma 0.9 --brightness 0.6
#
#Set your wallpaper
feh --bg-fill /home/oh/Pictures/Backgrounds/hugin.png &
#
#start sxhkd to replace Qtile native key-bindings
#run sxhkd -c ~/.config/sxhkd/sxhkdrc &
volumeicon &
sxhkd &
#emacs --daemon &
#solaar --window hide --battery-icons regular &
nm-applet &
#pamac-tray &
xfce4-power-manager &
#numlockx on &
blueberry-tray &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#thunderbird
