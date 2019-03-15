Icinga Packaging
================

![Icinga Logo](https://www.icinga.com/wp-content/uploads/2014/06/icinga_logo.png)


##### Contents

<!-- TOC -->

- [About](#about)
- [Packages and Sources](#packages-and-sources)
  - [Libraries](#libraries)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

<!-- /TOC -->
## About

This repository is the main issue tracker and support channel for [packages.icinga.com].

All packages build for the Icinga repository have their own packaging repository for RPM and Debian/Ubuntu builds.

Most sources are available public:

* [Icinga on GitHub](https://github.com/Icinga) (search for rpm or deb)
* [packaging on Icinga GitLab](https://git.icinga.com/packaging)

This repository is the place to file issues and requests, please [open an issue](https://github.com/Icinga/icinga-packaging/issues/new).

## Packages and Sources

Package sources are split into several repositories, based on OS, support or update behavior.

Package            | Repositories
-------------------|--------------------------------------------------------
icinga2            | [rpm-icinga2] [deb-icinga2] [raspbian-icinga2]
icingaweb2         | [rpm-icingaweb2] [deb-icingaweb2] [raspbian-icingaweb2]
icinga-rpm-release | [rpm-icinga-rpm-release]

### Libraries

Also some libraries are built a fulfill requirements, especially on older OS releases.

Package | Description                  | Repositories
--------|------------------------------|----------------------------------------
boost   | Icinga 2 needs boost >= 1.66 | [redhat-boost] [suse-boost] [deb-boost]

## Documentation

Documentation for release packages and more can be found in the [doc](doc/) directory.

* [Introduction into RPM/Deb packages](doc/01-Introduction.md)
* [Build release packages](doc/02-Release-Packages.md)
* [Dependencies by OS](doc/03-Dependencies.md)
* [OS EOL dates](doc/04-OS-EOL.md)

## Contributing

Feel free to contribute to our packaging work, see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

Icinga software and the Icinga documentation are licensed under the terms of the GNU
General Public License Version 2, you will find a copy of this license in the
COPYING file included in the source package.

[packages.icinga.com]: https://packages.icinga.com
[rpm-icinga2]: https://github.com/Icinga/rpm-icinga2
[deb-icinga2]: https://github.com/Icinga/deb-icinga2
[rpm-icinga2-templates]: https://github.com/Icinga/rpm-icinga2-templates
[deb-icinga2-templates]: https://github.com/Icinga/deb-icinga2-templates
[rpm-icingaweb2]: https://github.com/Icinga/rpm-icingaweb2
[deb-icingaweb2]: https://github.com/Icinga/deb-icingaweb2
[rpm-icinga-rpm-release]: https://github.com/Icinga/rpm-icinga-rpm-release
[raspbian-icinga2]: https://git.icinga.com/packaging/raspbian-icinga2
[raspbian-icingaweb2]: https://git.icinga.com/packaging/raspbian-icingaweb2
[suse-boost]: https://git.icinga.com/packaging/suse-boost
[redhat-boost]: https://git.icinga.com/packaging/redhat-boost
[deb-boost]: https://git.icinga.com/packaging/deb-boost
