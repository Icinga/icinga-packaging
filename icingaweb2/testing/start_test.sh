#!/bin/bash

set -ex

project="icingaweb2"

cd archive

apt-ftparchive packages . > Packages

sudo su -c 'echo "deb file:$(pwd)/ ./" >>  /etc/apt/sources.list'

sudo apt-get update -y

sudo apt-get install -y --force-yes icingaweb2 apache2

sudo apache2ctl start || echo "apache2ctl start failed"


RSTATUS=$(curl -s -w %{http_code} http://localhost/icingaweb2/authentication/login -o /dev/null)
if [ "200" != "$RSTATUS" ]; then 
  echo "Http exit code was not ok!"
  exit 1
else
  echo "All's well"
  exit 0
fi

