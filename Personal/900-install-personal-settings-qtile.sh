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
tput setaf 3
echo "----------------------------------------------------"
echo "Personal settings to reset to default"
echo "----------------------------------------------------"
tput sgr0
# echo
# echo "To default xfce settings"
# echo
# [ -d $HOME"/.config/xfce4/xfconf/xfce-perchannel-xml/" ] || mkdir -p $HOME"/.config/xfce4/xfconf/xfce-perchannel-xml/"
# cp  $installed_dir/settings/xfce/xsettings.xml $HOME/.config/xfce4/xfconf/xfce-perchannel-xml
# sudo cp  $installed_dir/settings/xfce/xsettings.xml /etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml
echo
echo "To default gtk-3.0 config"
echo
[ -d $HOME"/.config/gtk-3.0" ] || mkdir -p $HOME"/.config/gtk-3.0"
cp  $installed_dir/settings/gtk3/settings.ini $HOME/.config/gtk-3.0
sudo cp  $installed_dir/settings/gtk3/settings.ini /etc/skel/.config/gtk-3.0
echo
tput setaf 3
echo "----------------------------------------------------"
echo "Personal settings for any system"
echo "----------------------------------------------------"
tput sgr0
echo
echo "Adding xorg xkill"
echo
[ -d /etc/X11/xorg.conf.d/ ] || mkdir -p /etc/X11/xorg.conf.d/
sudo cp  settings/xorg/* /etc/X11/xorg.conf.d/
echo
tput setaf 2

echo
tput setaf 4
echo "----------------------------------------------------"
echo "Copy configuration files"
echo "----------------------------------------------------"
tput sgr0
echo

cp -rf $installed_dir/settings/qtile* $HOME/.config/
cp -rf $installed_dir/settings/sxhkd* $HOME/.config/

echo
tput setaf 4
echo "----------------------------------------------------"
echo "Copy home files for user oh"
echo "  /arcolinux-mynemesis/Personal/home/oh"
echo "----------------------------------------------------"
tput sgr0
echo

cp -rf $installed_dir/home/oh* /home/

echo
tput setaf 4
echo "----------------------------------------------------"
echo "     Done"
echo "----------------------------------------------------"
tput sgr0
echo
