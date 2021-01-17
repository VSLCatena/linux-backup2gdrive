#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
echo -e "Starting backup\n" > $SCRIPTPATH/backup.log

if test -f $SCRIPTPATH/backup_job.conf ;
   then .  $SCRIPTPATH/backup_job.conf

   tar -zcvpf $BACKUP_DIR/backup.tar.gz $TARGET_DIR >> $SCRIPTPATH/backup.log 2>&1
   sleep 5
   /usr/bin/python3.8 $SCRIPTPATH/backup.py $folderid $BACKUP_DIR/backup.tar.gz >>$SCRIPTPATH/backup.log 2>&1
   sleep 5
   mv $BACKUP_DIR/backup.tar.gz $BACKUP_DIR/backup.tar.gz.old >> $SCRIPTPATH/backup.log 2>&1
   echo -e "Done" >> $SCRIPTPATH/backup.log
fi
