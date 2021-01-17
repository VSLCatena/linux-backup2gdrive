#!/bin/sh
#https://developers.google.com/drive/api/v3/quickstart/python

sudo apt update && apt upgrade -y
curl https://bootstrap.pypa.io/get-pip.py -o ./get-pip.py
chmod +x ./get-pip.py
/usr/bin/python3.8 get-pip.py
pip install -r requirements.txt
rm ./get-pip.py
