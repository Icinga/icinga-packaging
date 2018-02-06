# Icinga Packaging

![Icinga Logo](https://www.icinga.com/wp-content/uploads/2014/06/icinga_logo.png)

#### Table of Contents

1. [About](#about)
2. [Packages](#packages)
3. [Documentation](#documentation)
4. [Contributing](#contributing)
5. [License](#license)

## About

This repository is the main issue tracker and support channel for [packages.icinga.com].

All packages build for the Icinga repository have their own packaging repository for RPM and Debian/Ubuntu builds.

If you are uncertain where your issue/request belongs to, [open an issue here](https://github.com/Icinga/icinga-packaging/issues/new).

> **Note:**
> Previously this repository contained all packaging within branches.
> This has been discontinued as of 2018-02-06. Please see the individual
> repositories below.

## Packages

Package            | RPM           | Debian/Ubuntu
-------------------|---------------|--------------
icinga2            | [rpm-icinga2] | [deb-icinga2]
icinga2-templates  | [rpm-icinga2-templates] | [deb-icinga2-templates]
icingaweb2         | [rpm-icingaweb2] | [deb-icingaweb2]
icinga-rpm-release | [rpm-icinga-rpm-release] | -

## Documentation

Documentation for release packages and more can be found in the [doc](doc/) directory.

* [Introduction into RPM/Deb packages](doc/01-Introduction.md)
* [Build release packages](doc/02-Release-Packages.md)

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
