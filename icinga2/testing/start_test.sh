#!/bin/bash

set -ex

#This should work for any .deb Package

cd archive

apt-ftparchive packages . > Packages

sudo su -c 'echo "deb file:$(pwd)/ ./" >>  /etc/apt/sources.list'

sudo apt-get update

sudo DEBIAN_FRONTEND=noninteractive apt-get install --allow-unauthenticated -y icinga2 icinga2-ido-mysql mysql-server

sudo icinga2 feature list

sudo icinga2 deamon -C
