#!/bin/bash
# this script runs in the rpm_test environment

install_package icingaweb2

# set timezone for PHP
if [ -d /etc/php.d ]; then
  php_d=/etc/php.d
elif [ -d /etc/php5/conf.d ]; then
  php_d=/etc/php5/conf.d
else
  echo "Can not set PHP timezone!" >&2
  exit 1
fi
sudo sh -c "echo 'date.timezone = UTC' >${php_d}/timezone.ini"

# Start apache in background
if [ -e /usr/sbin/start_apache2 ]; then
  # newer SUSE
  sudo a2enmod rewrite
  sudo a2enmod php5

  sudo /usr/sbin/start_apache2 -t
  sudo /usr/sbin/start_apache2 -k start
elif [ -x /usr/share/apache2/get_module_list ]; then
  # older SUSE
  sudo a2enmod rewrite
  sudo a2enmod php5

  # update apache config
  sudo /usr/share/apache2/get_includes
  sudo /usr/share/apache2/get_module_list

  sudo /usr/sbin/apache2ctl -k start
elif [ -x /usr/sbin/httpd ]; then
  # Disable mod_lua - it sometimes crashes on Fedora 25 with:
  # mod_lua: Failed to create shared memory segment on file /tmp/httpd_lua_shm.187
  sudo sh -ex <<<"test -e /etc/httpd/conf.modules.d/00-lua.conf && mv /etc/httpd/conf.modules.d/00-lua.conf{,.off} || true"
  sudo httpd -t
  sudo httpd -k start
else
  echo "Can not detect how to start Apache!" >&2
  exit 1
fi

sleep 10

output=`mktemp`

if curl -v http://127.0.0.1/icingaweb2/authentication/login -o "$output"; then
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
  echo "====================================="
  sudo sh -ex <<<'cat /var/log/httpd/*error* /var/log/apache2/*error*'
  exit 1
fi
