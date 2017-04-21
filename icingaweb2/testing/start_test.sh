#!/bin/bash
# this script runs in the rpm_test environment

install_package icingaweb2

if [ -x /usr/sbin/apachectl ]; then
  apache_command="apachectl start"
else
  echo "Can not detect how to start Apache!" >&2
  exit 1
fi

echo "Starting Apache httpd..."
if ! sudo $apache_command; then
    echo "Failed to start httpd..." >&2
    exit 1
fi

sleep 5

output=`mktemp`

if curl -v http://localhost/icingaweb2/authentication/login -o "$output"; then
  if grep -q '<div id="login"' "$output"; then
    echo "Login page available"
    exit 0
  else
    echo "Didn't get a logon page from the webserver!"
    echo
    echo "Output of the page is:"
    echo "====================================="
    cat "$output"
    exit 1
  fi
else
  echo "Request for login page failed!"
  echo
  echo "Output of the page is:"
  echo "====================================="
  cat "$output"
  exit 1
fi
