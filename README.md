# Icinga Packaging

## RPM Packages

In the `rpm/*` branches, the RPM spec files, sources and scripts are stored.

### Structure

On the first level, each product, or source package, is stored in a separate directory.

* [icinga2](icinga2/)
* [icingaweb2](icingaweb2/)

Each product directory must contain, a `<product>.spec file` for all target OS and distributions.

Every other file is copied to `SOURCES/` on build, here some examples of other contents:

* icinga2/
  * icinga2.spec
  * icinga2-critical-bug-1234.patch
  * somefile-to-include-as-source.txt

Some scripts are required, others are helpers for maintaining the data.

* &lt;product&gt;/get_snapshot - REQUIRED: Used to generate a snapshot tarball by the build system
* &lt;product&gt;/testing/start_test.sh - REQUIRED: Used for install tests in the build system
* &lt;product&gt;/diff - Diffing our packaging with e.g. upstream (only used for the meantime)

All these scripts might differ between packages...

### Notes on changing packaging

* Main target for development or changes of the packaging is `rpm/snapshot`
* Feature branches can be used from the build system, and should match a specific upstream branch to be tested:
  * e.g. icinga2 feature branch: `feature/something-cool`
  * can be tested with a packaging branch: `rpm/feature/something-cool`
* The branch `rpm/release` should only be updated for releases
  * Either by merging or cherry-picking commits from `rpm/snapshot`
* Target versions (which upstream version is built for release) is **ONLY** controlled by the `Version` and `Revision` of a spec file!
* Upstream code is pulled by the help of `spectool`, with the `Source` URLs inside the spec file
* Minor packaging changes, that should be released, **MUST** increment at least the packaging revision, e.g. `2.7.0-1` to `2.7.0-2`

### Release workflow

* Make sure the packaging in `rpm/snapshot` contains all necessary changes for that release
* Update the spec file with the new version, and make a small changelog entry if it contains interesting information
* Commit the changes to `rpm/snapshot`
* Merge or cherry-pick the needed commits to `rpm/release`
* You can now build the respective release jobs in the build system
* The publish part of each release build has to be manually started with `allow_release` set,
  to actually publish the package to the repository.

Notes:

* It's always possible to only update a certain distribution, just update that, and only
  build the respective distribution in the build system.
