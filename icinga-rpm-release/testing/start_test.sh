#!/bin/bash
# this script runs in the rpm_test environment

install_package icinga-rpm-release

yum repolist
yum repolist | grep -i icinga
