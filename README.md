Icinga Packaging
================

![Icinga Logo](https://www.icinga.com/wp-content/uploads/2014/06/icinga_logo.png)

##### Contents

<!-- TOC -->

- [About](#about)
- [Packages and Sources](#packages-and-sources)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

<!-- /TOC -->
## About

This repository is the main issue tracker and support channel for [packages.icinga.com].

All packages build for the Icinga repository have their own packaging repository for RPM and Debian/Ubuntu builds. Though there are no longer on GitHub since we are using GitLab CI for building.

This repository is the place to file issues and requests, please [open an issue](https://github.com/Icinga/icinga-packaging/issues/new).

If you have general questions you can also join the [Icinga Community](https://community.icinga.com).

## Build System

The packages are built and tested using GitLab CI, with Docker images and scripts from the [Icinga Docker Build System](https://git.icinga.com/build-docker/docs).

## Packages and Sources

All public packages are built from GIT repositories in our [Icinga GitLab packaging group](https://git.icinga.com/packaging).

Package sources are split into several repositories, based on OS, support or update behavior.

### Products

Package      | Repositories
-------------|--------------------------------------------------------
[icinga2]    | [RPM][rpm-icinga2] [Debian/Ubuntu][deb-icinga2] [Raspbian][raspbian-icinga2] [Windows][windows-icinga2]
[icingaweb2] | [RPM][rpm-icingaweb2] [Debian/Ubuntu][deb-icingaweb2] [Raspbian][raspbian-icingaweb2]

### Icinga Web Modules

Package       | Repositories
--------------|--------------------------------------------------------------------------------------------
[director]    | [RPM][rpm-icingaweb2-module-director] [Debian/Ubuntu][deb-icingaweb2-module-director]
[ipl]         | [RPM][rpm-icingaweb2-module-ipl] [Debian/Ubuntu][deb-icingaweb2-module-ipl]
[incubator]   | [RPM][rpm-icingaweb2-module-incubator] [Debian/Ubuntu][deb-icingaweb2-module-incubator]
[reactbundle] | [RPM][rpm-icingaweb2-module-reactbundle] [Debian/Ubuntu][deb-icingaweb2-module-reactbundle]

Upcoming packages for modules:

* audit
* businessprocess
* cube
* elasticsearch
* fileshipper
* generictts
* graphite
* nagvis
* pnp
* reporting
  - pdfexport
  - idoreports
* vspheredb
* x509
* (for director)
  - aws
  - puppetdb
  - vsphere

### Other

Also some libraries are built a fulfill requirements, especially on older OS releases:

Package            | Repositories
-------------------|-------------------------
icinga-rpm-release | [RPM][rpm-icinga-rpm-release]
boost  | see [separate documentation](doc/packages-boost.md)

## Documentation

Other documentation can be found in the [doc](doc/) directory.

* [Dependencies by OS](doc/03-Dependencies.md)
* [OS EOL dates](doc/04-OS-EOL.md)

## License

Icinga software and the Icinga documentation are licensed under the terms of the GNU
General Public License Version 2, you will find a copy of this license in the
COPYING file included in the source package.

[packages.icinga.com]: https://packages.icinga.com

[icinga2]: https://github.com/Icinga/icinga2
[icingaweb2]: https://github.com/Icinga/icingaweb2

[rpm-icinga2]: https://git.icinga.com/packaging/rpm-icinga2
[deb-icinga2]: https://git.icinga.com/packaging/deb-icinga2
[windows-icinga2]: https://git.icinga.com/packaging/windows-icinga2
[rpm-icingaweb2]: https://git.icinga.com/packaging/rpm-icingaweb2
[deb-icingaweb2]: https://git.icinga.com/packaging/deb-icingaweb2

[director]: https://github.com/Icinga/icingaweb2-module-director
[deb-icingaweb2-module-director]: https://git.icinga.com/packaging/deb-icingaweb2-module-director
[rpm-icingaweb2-module-director]: https://git.icinga.com/packaging/rpm-icingaweb2-module-director

[ipl]: https://github.com/Icinga/icingaweb2-module-ipl
[deb-icingaweb2-module-ipl]: https://git.icinga.com/packaging/deb-icingaweb2-module-ipl
[rpm-icingaweb2-module-ipl]: https://git.icinga.com/packaging/rpm-icingaweb2-module-ipl

[incubator]: https://github.com/Icinga/icingaweb2-module-incubator
[deb-icingaweb2-module-incubator]: https://git.icinga.com/packaging/deb-icingaweb2-module-incubator
[rpm-icingaweb2-module-incubator]: https://git.icinga.com/packaging/rpm-icingaweb2-module-incubator

[reactbundle]: https://github.com/Icinga/icingaweb2-module-reactbundle
[deb-icingaweb2-module-reactbundle]: https://git.icinga.com/packaging/deb-icingaweb2-module-reactbundle
[rpm-icingaweb2-module-reactbundle]: https://git.icinga.com/packaging/rpm-icingaweb2-module-reactbundle

[rpm-icinga-rpm-release]: https://git.icinga.com/packaging/rpm-icinga-rpm-release

[raspbian-icinga2]: https://git.icinga.com/packaging/raspbian-icinga2
[raspbian-icingaweb2]: https://git.icinga.com/packaging/raspbian-icingaweb2

[suse-boost]: https://git.icinga.com/packaging/suse-boost
[redhat-boost]: https://git.icinga.com/packaging/redhat-boost
[deb-boost]: https://git.icinga.com/packaging/deb-boost

[rpm-icinga2-templates]: https://git.icinga.com/packaging/rpm-icinga2-templates
[deb-icinga2-templates]: https://git.icinga.com/packaging/deb-icinga2-templates
