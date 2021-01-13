#!/bin/bash
folderid='DITGETAL' # https://drive.google.com/drive/folders/DITGETAL

BACKUP_DIR="/opt/data/" #zet hier backup neer
TARGET_DIR="/opt/data/minecraft/" #maakt hier backup van
tar -zcvpf $BACKUP_DIR/backup.tar.gz $TARGET_DIR # Create archive.tar from files foo and bar.

/usr/bin/python3.8 backup.py $folderid /opt/data/backup.tar.gz #upload backup.tar.gz naar Gdrive
