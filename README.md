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

<!-- PACKAGES:
  audit businessprocess cube generictts graphite elasticsearch nagvis pnp x509 vspheredb
  reporting idoreports pdfexport
| prefix=icingaweb2-module- -->
Package | RPM | Debian/Ubuntu
--------|-----|--------------
[icingaweb2-module-audit](https://github.com/Icinga/icingaweb2-module-audit) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-audit/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-audit) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-audit/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-audit)
[icingaweb2-module-businessprocess](https://github.com/Icinga/icingaweb2-module-businessprocess) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-businessprocess/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-businessprocess) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-businessprocess/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-businessprocess)
[icingaweb2-module-cube](https://github.com/Icinga/icingaweb2-module-cube) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-cube/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-cube) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-cube/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-cube)
[icingaweb2-module-elasticsearch](https://github.com/Icinga/icingaweb2-module-elasticsearch) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-elasticsearch/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-elasticsearch) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-elasticsearch/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-elasticsearch)
[icingaweb2-module-generictts](https://github.com/Icinga/icingaweb2-module-generictts) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-generictts/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-generictts) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-generictts/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-generictts)
[icingaweb2-module-graphite](https://github.com/Icinga/icingaweb2-module-graphite) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-graphite/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-graphite) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-graphite/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-graphite)
[icingaweb2-module-idoreports](https://github.com/Icinga/icingaweb2-module-idoreports) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-idoreports/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-idoreports) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-idoreports/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-idoreports)
[icingaweb2-module-nagvis](https://github.com/Icinga/icingaweb2-module-nagvis) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-nagvis/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-nagvis) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-nagvis/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-nagvis)
[icingaweb2-module-pdfexport](https://github.com/Icinga/icingaweb2-module-pdfexport) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-pdfexport/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-pdfexport) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-pdfexport/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-pdfexport)
[icingaweb2-module-pnp](https://github.com/Icinga/icingaweb2-module-pnp) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-pnp/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-pnp) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-pnp/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-pnp)
[icingaweb2-module-reporting](https://github.com/Icinga/icingaweb2-module-reporting) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-reporting/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-reporting) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-reporting/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-reporting)
[icingaweb2-module-vspheredb](https://github.com/Icinga/icingaweb2-module-vspheredb) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-vspheredb/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-vspheredb) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-vspheredb/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-vspheredb)
[icingaweb2-module-x509](https://github.com/Icinga/icingaweb2-module-x509) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-x509/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-x509) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-x509/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-x509)
<!-- END PACKAGES -->

These modules are mainly add-ons to Icinga Director:

<!-- PACKAGES: aws fileshipper vsphere puppetdb | prefix=icingaweb2-module- -->
Package | RPM | Debian/Ubuntu
--------|-----|--------------
[icingaweb2-module-aws](https://github.com/Icinga/icingaweb2-module-aws) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-aws/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-aws) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-aws/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-aws)
[icingaweb2-module-fileshipper](https://github.com/Icinga/icingaweb2-module-fileshipper) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-fileshipper/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-fileshipper) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-fileshipper/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-fileshipper)
[icingaweb2-module-puppetdb](https://github.com/Icinga/icingaweb2-module-puppetdb) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-puppetdb/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-puppetdb) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-puppetdb/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-puppetdb)
[icingaweb2-module-vsphere](https://github.com/Icinga/icingaweb2-module-vsphere) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-vsphere/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-vsphere) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-vsphere/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-vsphere)
<!-- END PACKAGES -->

Some modules provide libraries and no direct functionality:

<!-- PACKAGES: ipl incubator reactbundle | prefix=icingaweb2-module- -->
Package | RPM | Debian/Ubuntu
--------|-----|--------------
[icingaweb2-module-incubator](https://github.com/Icinga/icingaweb2-module-incubator) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-incubator/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-incubator) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-incubator/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-incubator)
[icingaweb2-module-ipl](https://github.com/Icinga/icingaweb2-module-ipl) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-ipl/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-ipl) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-ipl/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-ipl)
[icingaweb2-module-reactbundle](https://github.com/Icinga/icingaweb2-module-reactbundle) | [![rpm](https://git.icinga.com/packaging/rpm-icingaweb2-module-reactbundle/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/rpm-icingaweb2-module-reactbundle) | [![deb](https://git.icinga.com/packaging/deb-icingaweb2-module-reactbundle/badges/master/pipeline.svg?style=flat-square)](https://git.icinga.com/packaging/deb-icingaweb2-module-reactbundle)
<!-- END PACKAGES -->

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
