# alerta_client

## Invoke Alerta Server
```
docker-compose -f alerta.yml up -d
```


## Setup Backup cronjob and upload to ftp.
0. mkdir -p /ssd/backup_file

1. Fill in the id/pw in backup_mongo.sh
 
2. Install the backup cronjob
```
0 */6 * * *  cd $INSTALL_DIR && backup_mongo.sh
```

## Restore
Put the mongo db files in /ssd/restore directory.

`ls -l /ssd/restore` will get

```
total 8
drwxr-xr-x 2 root root 4096 Feb 24 17:47 admin
drwxr-xr-x 2 root root 4096 Feb 24 17:47 monitoring
```

Execute 
```
docker-compose -f restore.yml up -d
```
