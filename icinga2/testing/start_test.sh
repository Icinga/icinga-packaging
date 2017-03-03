#!/bin/bash

sudo yum install -y createrepo 

createrepo $WORKSPACE/archive

sudo -E su -c "cat << EOF > /etc/yum.repos.d/local.repo
[local]
name=Nyarlathotep
baseurl=file://$WORKSPACE/archive
enabled=1
gpgcheck=0
EOF"

sudo yum update -y
sudo yum install -y icinga2 mariadb-server icinga2-ido-mysql

sudo icinga2 daemon -C
