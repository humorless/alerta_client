#!/bin/bash
ID=ooooooo
PW=xxxxxxx

function backup_upload() {
  echo "execute backup "
  DATE=$(date +"%Y%m%d_%H%M%S")
  tar zcf /ssd/backup_file/alerta_backup_"$DATE".tar.gz /ssd/backup 
  echo "execute upload "
  curl -v -F "file=@/ssd/backup_file/alerta_backup_$DATE.tar.gz" -u $ID:$PW "http://ftp.owl.fastweb.com.cn/OWL-backup/mongo/?upload"
  rm /ssd/backup_file/alerta_backup_"$DATE".tar.gz
}

YAML=./backup.yml
# backup command
docker-compose -f $YAML up -d backup-db

RESULT=$(docker-compose -f $YAML ps | awk '/backup/{print $7$8}')
if [ $RESULT == "Exit0" ]; then
   # execute upload
   backup_upload 
   exit 0
fi

sleep 600

RESULT=$(docker-compose -f $YAML ps | awk '/backup/{print $7$8}')
if [ $RESULT == "Exit0" ]; then
   # execute upload
   backup_upload 
   exit 0
fi

exit 1
