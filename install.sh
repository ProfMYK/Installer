#!/bin/bash

set +x

wget https://raw.githubusercontent.com/ProfMYK/Installer/main/installer.py
sudo apt install python3 python3-pip
sudo pip3 install colorama typer inquirer
python3 installer.py