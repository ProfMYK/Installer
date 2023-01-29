#!/bin/bash

set +x

cd /tmp
git clone https://github.com/jonaburg/picom
cd picom
meson --buildtype=release . build
sudo ninja -C build
sudo mv build/src/picom /usr/local/bin
mkdir $HOME/.config/picom/
cp picom.sample.conf $HOME/.config/picom/picom.conf
sudo rm -rf /tmp/picom