#!/bin/bash
# this script runs in the rpm_test environment

# TODO: database?

install_package icinga2 icinga2-ido-mysql icinga2-ido-pgsql

sudo icinga2 daemon -C
