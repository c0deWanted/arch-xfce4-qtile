#!/bin/bash
#set -e
##################################################################################################################
# Author    : Erik Dubois
# Website   : https://www.erikdubois.be
# Website   : https://www.alci.online
# Website   : https://www.ariser.eu
# Website   : https://www.arcolinux.info
# Website   : https://www.arcolinux.com
# Website   : https://www.arcolinuxd.com
# Website   : https://www.arcolinuxb.com
# Website   : https://www.arcolinuxiso.com
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
#tput setaf 8 = light blue
##################################################################################################################

echo
tput setaf 3
echo "################################################################"
echo "################### Remove software for all"
echo "################################################################"
tput sgr0
echo

sudo pacman -R --noconfirm adobe-source-han-sans-cn-fonts
sudo pacman -R --noconfirm adobe-source-han-sans-jp-fonts
sudo pacman -R --noconfirm adobe-source-han-sans-kr-fonts
sudo pacman -R --noconfirm archinstall

# remove where ever we are

sudo pacman -R --noconfirm ristretto parole xfburn xfce4-artwork xfce4-screensaver

sudo rm -rf /usr/share/backgrounds/xfce

sudo pacman -Rs broadcom-wl-dkms --noconfirm
sudo pacman -Rs xf86-video-amdgpu --noconfirm
sudo pacman -Rs xf86-video-fbdev --noconfirm
sudo pacman -Rs xf86-video-openchrome --noconfirm
if pacman -Qi xf86-video-vmware &> /dev/null; then
  sudo pacman -Rs xf86-video-vmware --noconfirm
fi
sudo pacman -Rs xf86-video-ati --noconfirm
sudo pacman -Rs xf86-video-nouveau --noconfirm
sudo pacman -Rs xf86-video-vesa --noconfirm

# always put the current .bashrc .zshrc away
if [ -f /etc/skel/.bashrc ]; then
  sudo mv /etc/skel/.bashrc /etc/skel/.bashrc-old
fi

if [ -f /etc/skel/.zshrc ]; then
  sudo mv /etc/skel/.zshrc /etc/skel/.zshrc-old
fi

# when on Arch Linux - remove conflicting files
if grep -q "archlinux" /etc/os-release; then

  echo
  tput setaf 2
  echo "################################################################"
  echo "############### Removing software for Arch"
  echo "################################################################"
  tput sgr0
  echo

  echo "Nothing to remove"

  echo
  tput setaf 2
  echo "################################################################"
  echo "################### Software removed"
  echo "################################################################"
  tput sgr0
  echo

fi

# when on ARCOLINUX - remove conflicting files

if grep -q "ArcoLinux" /etc/os-release; then
  echo
  tput setaf 2
  echo "################################################################"
  echo "####### Removing software for ArcoLinux"
  echo "################################################################"
  tput sgr0
  echo

  echo "Nothing to do"

  echo
  tput setaf 2
  echo "################################################################"
  echo "################### Software removed"
  echo "################################################################"
  tput sgr0
  echo

fi
