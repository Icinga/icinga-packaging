# Icinga Packaging

## Debian / Ubuntu Packages

In the `deb/*` branches, the Debian packaging is stored.

### Structure

On the first level, each product, or source package, is stored in a separate directory.

* [icinga2](icinga2/)
* [icingaweb2](icingaweb2/)

In this directory multiple versions of the packaging can exist, the names can be referenced in the build system,
to choose the packaging to use.

* icinga2/jessie/
* icinga2/stretch/
* icinga2/ubuntu/
* icingaweb2/trusty/
* icingaweb2/xenial/

Inside each of this directory, should only be the `debian/` directory, with all the necessary contents.

* icinga2/
  * jessie/
    * debian/
      * control
      * changelog
      * rules
      * ...

Some scripts are required, others are helpers for maintaining the data.

* &lt;product&gt;/get_snapshot - REQUIRED: Used to generate a snapshot tarball by the build system
* &lt;product&gt;/testing/start_test.sh - REQUIRED: Used for install tests in the build system
* &lt;product&gt;/diff - Diffing our packaging with the official Debian packaging
* &lt;product&gt;/dch - Helper script to update all changelogs for a new release

All these scripts might differ between packages...

### Notes on changing packaging

* Main target for development or changes of the packaging is `deb/snapshot`
* Feature branches can be used from the buildsystem, and should match a specific upstream branch to be tested:
  * e.g. icinga2 feature branch: `feature/something-cool`
  * can be tested with a packaging branch: `deb/feature/something-cool`
* The branch `deb/release` should only be updated for releases
  * Either by merging or cherry-picking commits from `deb/snapshot`
* Target versions (which upstream version is built for release) is **ONLY** controlled by the `debian/changelog` version!
* Upstream code is pulled by the help of `debian/watch`, see `man uscan`
* Minor packaging changes that should be released **MUST** increment at least the packaging version, e.g. `2.7.0-1` to `2.7.0-2`

### Release workflow

* Make sure the packaging in `deb/snapshot` contains all necessary changes for that release
* Update all `debian/changelog` files with the new version, and a small changelog entry
  * You can use the `dch` script like so: `./dch 2.7.0-1 "Update to 2.7.0"`
  * Note: the script uses your git `user.name` and `user.email` for the Debian changelog
* Make sure the worktree has been updated correctly, and commit it to `deb/snapshot`
* Merge or cherry-pick the needed commits to `deb/release`
* You can now build the respective release jobs in the build system
* The publish part of each release build has to be manually started with `allow_release` set,
  to actually publish the package to the repository.

Notes:

* It's always possible to only update a certain distribution, just update that, and only
  build the respective distribution in the build system.
