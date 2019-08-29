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

### Main Products

Package      | RPM | Debian/Ubuntu | Raspbian | Windows
-------------|-----|---------------|----------|--------
[icinga2]    | <!-- PACKAGE BADGES: icinga2 rpm,deb,raspbian,windows --> [![rpm](https://git.icinga.com/packaging/rpm-icinga2/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icinga2) | [![deb](https://git.icinga.com/packaging/deb-icinga2/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icinga2) | [![raspbian](https://git.icinga.com/packaging/raspbian-icinga2/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/raspbian-icinga2) | [![windows](https://git.icinga.com/packaging/windows-icinga2/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/windows-icinga2) | 
[icingaweb2] | <!-- PACKAGE BADGES: icingaweb2 rpm,deb,raspbian --> [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2) | [![raspbian](https://git.icinga.com/packaging/raspbian-icingaweb2/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/raspbian-icingaweb2) | 
[icingaweb2-module-director] | <!-- PACKAGE BADGES: icingaweb2-module-director rpm,deb --> [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-director/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-director) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-director/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-director) | 

### Icinga Web Modules

<!-- PACKAGES: businessprocess cube audit generictts graphite elasticsearch | prefix=icingaweb2-module- -->
Package | RPM | Debian/Ubuntu
--------|-----|--------------
[icingaweb2-module-audit](https://github.com/Icinga/icingaweb2-module-audit) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-audit/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-audit) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-audit/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-audit)
[icingaweb2-module-businessprocess](https://github.com/Icinga/icingaweb2-module-businessprocess) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-businessprocess/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-businessprocess) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-businessprocess/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-businessprocess)
[icingaweb2-module-cube](https://github.com/Icinga/icingaweb2-module-cube) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-cube/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-cube) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-cube/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-cube)
[icingaweb2-module-elasticsearch](https://github.com/Icinga/icingaweb2-module-elasticsearch) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-elasticsearch/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-elasticsearch) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-elasticsearch/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-elasticsearch)
[icingaweb2-module-generictts](https://github.com/Icinga/icingaweb2-module-generictts) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-generictts/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-generictts) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-generictts/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-generictts)
[icingaweb2-module-graphite](https://github.com/Icinga/icingaweb2-module-graphite) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-graphite/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-graphite) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-graphite/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-graphite)
<!-- END PACKAGES -->

These modules are mainly add-ons to Icinga Director:

<!-- PACKAGES: fileshipper | prefix=icingaweb2-module- -->
Package | RPM | Debian/Ubuntu
--------|-----|--------------
[icingaweb2-module-fileshipper](https://github.com/Icinga/icingaweb2-module-fileshipper) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-fileshipper/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-fileshipper) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-fileshipper/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-fileshipper)
<!-- END PACKAGES -->

Some modules provide libraries and no direct functionality:

<!-- PACKAGES: ipl incubator reactbundle | prefix=icingaweb2-module- -->
Package | RPM | Debian/Ubuntu
--------|-----|--------------
[icingaweb2-module-incubator](https://github.com/Icinga/icingaweb2-module-incubator) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-incubator/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-incubator) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-incubator/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-incubator)
[icingaweb2-module-ipl](https://github.com/Icinga/icingaweb2-module-ipl) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-ipl/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-ipl) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-ipl/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-ipl)
[icingaweb2-module-reactbundle](https://github.com/Icinga/icingaweb2-module-reactbundle) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-reactbundle/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-reactbundle) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-reactbundle/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-reactbundle)
<!-- END PACKAGES -->

Upcoming packages for modules:

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
[icingaweb2-module-director]: https://github.com/Icinga/icingaweb2-module-director

[rpm-icinga-rpm-release]: https://git.icinga.com/packaging/rpm-icinga-rpm-release

[raspbian-icinga2]: https://git.icinga.com/packaging/raspbian-icinga2
[raspbian-icingaweb2]: https://git.icinga.com/packaging/raspbian-icingaweb2

[suse-boost]: https://git.icinga.com/packaging/suse-boost
[redhat-boost]: https://git.icinga.com/packaging/redhat-boost
[deb-boost]: https://git.icinga.com/packaging/deb-boost

[rpm-icinga2-templates]: https://git.icinga.com/packaging/rpm-icinga2-templates
[deb-icinga2-templates]: https://git.icinga.com/packaging/deb-icinga2-templates
