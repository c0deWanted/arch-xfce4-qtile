#!/bin/bash
#set -e
##################################################################################################################
# Author    : Erik Dubois
# Website   : https://www.erikdubois.be
# Website   : https://www.arcolinux.com
# Website   : https://www.arcolinuxforum.com
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################
#tput setaf 0 = black
#tput setaf 1 = red
#tput setaf 2 = green
#tput setaf 3 = yellow
#tput setaf 4 = dark blue
#tput setaf 5 = purple
#tput setaf 6 = cyan
#tput setaf 7 = gray
##################################################################################################################

installed_dir=$(dirname $(readlink -f $(basename `pwd`)))

##################################################################################################################

echo
tput setaf 4
echo "----------------------------------------------------"
echo "Copy configuration files"
echo "----------------------------------------------------"
tput sgr0
echo

cp -rf $installed_dir/settings/alacritty* $HOME/.config/
cp -rf $installed_dir/settings/archlinux-logout* $HOME/.config/
cp -rf $installed_dir/settings/dconf* $HOME/.config/
cp -rf $installed_dir/settings/deadbeef* $HOME/.config/
cp -rf $installed_dir/settings/flameshot* $HOME/.config/
cp -rf $installed_dir/settings/gtk-3.0* $HOME/.config/
cp -rf $installed_dir/settings/htop* $HOME/.config/
#cp -rf $installed_dir/settings/Kvantum* $HOME/.config/
cp -rf $installed_dir/settings/mpv* $HOME/.config/
cp -rf $installed_dir/settings/neofetch* $HOME/.config/
cp -rf $installed_dir/settings/paru* $HOME/.config/
cp -rf $installed_dir/settings/polybar* $HOME/.config/
cp -rf $installed_dir/settings/pulse* $HOME/.config/
cp -rf $installed_dir/settings/qt5ct* $HOME/.config/
cp -rf $installed_dir/settings/rofi* $HOME/.config/
cp -rf $installed_dir/settings/solaar* $HOME/.config/
cp -rf $installed_dir/settings/Thunar* $HOME/.config/
cp -rf $installed_dir/settings/volumeicon* $HOME/.config/

####################################################

# Copy doom config and sync
#cp -rf $installed_dir/settings/.doom.d* $HOME/

####################################################

echo
tput setaf 4
echo "----------------------------------------------------"
echo "     Done"
echo "----------------------------------------------------"
tput sgr0
echo
