#!/bin/bash

set -xe

sudo yum clean all

sudo yum install -y yum-plugin-ovl
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
sudo yum install -y icingaweb2

sudo apache2ctl start || echo "apache2ctl start failed"

RSTATUS=$(curl -s -w %{http_code} http://localhost/icingaweb2/authentication/login -o /dev/null)
if [ "200" != "$RSTATUS" ]; then
  echo "Http exit code was not ok!"
  exit 1
else
  echo "All's well!"
  exit 0
fi
