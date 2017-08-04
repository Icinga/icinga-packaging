Icinga Repository RPM
=====================

This package helps installing Icinga's RPM repository and key to the system.

So you can easily install packages from [packages.icinga.com](https://packages.icinga.com)

    rpm -Uvh icinga-rpm-release-latest-VERSION.noarch.rpm

It will install:

    /etc/yum.repos.d/ICINGA-release.repo
    /etc/yum.repos.d/ICINGA-snapshot.repo

More information can be found inside the [documentation](https://www.icinga.com/docs)
and on [packages.icinga.com](https://packages.icinga.com).
