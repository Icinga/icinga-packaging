Boost Packages
==============

## Icinga 2 Requirements

Version | Minimum Boost
--------|--------------
2.11    | >= 1.66
2.9     | >= 1.53
2.8     | >= 1.48

## Repositories

Packages provided from Icinga are built with the following sources:

* [suse-boost](https://git.icinga.com/packaging/suse-boost) for SLES and openSUSE
* [redhat-boost](https://git.icinga.com/packaging/redhat-boost) for RHEL and compatible
* [deb-boost](https://git.icinga.com/packaging/deb-boost) for Debian and Ubuntu

## Boost Package Distribution

This list where the required Boost version is not available in the base Operating System, and has to be acquired
from additional repositories.

Usually we only reference semi-official repositories or the Icinga official releases.

### Icinga 2.11

OS            | Release | Package                       | Version | Distribution
--------------|---------|-------------------------------|---------|-------------------
RHEL / CentOS | 6       | icinga-boost169               | 1.69.0  | [Icinga EPEL]
RHEL / CentOS | 7       | [boost169][epel-boost169]     | 1.69.0  | [Fedora EPEL]
SLES          | 12.3    | icinga-boost169               | 1.69.0  | [Icinga SUSE]
SLES          | 12.4    | icinga-boost169               | 1.69.0  | [Icinga SUSE]
openSUSE      | 42.3    | icinga-boost169               | 1.69.0  | [Icinga openSUSE]
Debian        | jessie  | icinga-boost1.67              | 1.67.0  | [Icinga Debian]
Debian        | stretch | [boost1.67][debian-boost1.67] | 1.67.0  | [Debian Backports]
Ubuntu        | trusty  | icinga-boost1.67              | 1.67.0  | [Icinga Ubuntu]
Ubuntu        | xenial  | icinga-boost1.67              | 1.67.0  | [Icinga Ubuntu]
Ubuntu        | bionic  | icinga-boost1.67              | 1.67.0  | [Icinga Ubuntu]

> Note: Raspbian jessie and stretch will be added in the future

### Icinga 2.8

> Note: These are legacy builds after the release of Icinga 2.11

* SLES 11.4
* RHEL 5
* RHEL 6

You can find the old sources under [rpm-boost-old](https://git.icinga.com/packaging/rpm-boost-old).

[Icinga EPEL]: https://packages.icinga.com/epel
[Icinga SUSE]: https://packages.icinga.com/SUSE
[Icinga openSUSE]: https://packages.icinga.com/openSUSE
[Icinga Debian]: https://packages.icinga.com/debian
[Icinga Ubuntu]: https://packages.icinga.com/ubuntu
[Fedora EPEL]: https://fedoraproject.org/wiki/EPEL
[Debian Backports]: https://backports.debian.org
[debian-boost1.67]: https://tracker.debian.org/pkg/boost1.67
[epel-boost169]: https://apps.fedoraproject.org/packages/boost
<!-- currently only listed at https://bodhi.fedoraproject.org/updates/FEDORA-EPEL-2019-853e06b03c -->
