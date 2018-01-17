# Icinga Packaging

This repository holds the required build scripts to create packages for packages.icinga.com

## Documentation

Documentation for release packages and more can be found in the [doc](doc/) directory.

* [Introduction into RPM/Deb packages](doc/01-Introduction.md)
* [Build release packages](doc/02-Release-Packages.md)

## Branches

### Snapshot Packages

* Debian/Ubuntu: [deb/snapshot](https://github.com/Icinga/icinga-packaging/tree/deb/snapshot)
* RedHat/Fedora/SUSE: [rpm/snapshot](https://github.com/Icinga/icinga-packaging/tree/rpm/snapshot)

### Release Packages

* Debian/Ubuntu: [deb/release](https://github.com/Icinga/icinga-packaging/tree/deb/release)
* RedHat/Fedora/SUSE: [rpm/release](https://github.com/Icinga/icinga-packaging/tree/rpm/release)


## Contributing

Fork this repository on GitHub. Checkout the snapshot branches and build your PR based on that.

Example for RPM packages:

```
git checkout rpm/snapshot
git checkout -b fix/rpm-lint

Do your work, test, commit

git commit -av -m "Fix RPMlint errors"
git push -u origin fix/rpm-lint

hub pull-request -b rpm/snapshot
```

Issues and problems should be discussed in new issues.

## License

Please see the respective `*.spec` file, or the contents of `debian/copyright` for
author and license information about every package contained here.

    All additional scripts are licensed under GPL-2.0+ and

    Copyright (c) 2018 Icinga Development Team <info@icinga.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
