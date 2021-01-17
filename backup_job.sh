#!/bin/bash

if test -f $PWD/backup_job.conf ;
   then .  $PWD/backup_job.conf

   mv $BACKUP_DIR/backup.tar.gz $BACKUP_DIR/backup.tar.gz.old
   tar -zcvpf $BACKUP_DIR/backup.tar.gz $TARGET_DIR 
   /usr/bin/python3.8 $PWD/linux-backup2gdrive/backup.py $folderid $BACKUP_DIR/backup.tar.gz

fi
