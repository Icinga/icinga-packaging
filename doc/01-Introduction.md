# Introduction <a id="introduction"></a>

Each package repository should contain at least two branches:

* `master` which contains the current developed state
* `release` which is the current released version

We are not using tags as of now, but plan to do so.

## RPM Packages <a id="introduction-rpm-packages"></a>

Each project requires a spec file with the same name as the project. In addition to that optional patch and
source files can be added here.

Everything except the spec file is copied to the `SOURCES/` directory during the RPM package
build jobs.

Example contents:

* icinga2.spec
* icinga2-critical-bug-1234.patch
* file-to-include-as-source.txt

Some scripts are used by the build infrastructure and help during package development too:

Script                | Description
----------------------|------------
get_snapshot          | **Required.** Used to generate a snapshot tarball by the build system
testing/start_test.sh | **Required.** Used for install tests in the build system
diff                  | Allows to diff the repository contents with e.g. upstream.

These scripts may differ in the individual projects.

## Debian/Ubuntu Packages <a id="introduction-deb-packages"></a>

Each project has sub directories for the specific distribution they are built on.
This also allows for virtual directory names exposed to the build system.

* jessie/
* stretch/
* ubuntu/

Each distribution directory provides the `debian/` directory where the package build
sources and control files are located.

* jessie/
  * debian/
    * control
    * changelog
    * rules
    * ...

> **Tip**
>
> You can only update a specific distribution and release minor package updates.

Script                | Description
----------------------|------------
get_snapshot          | **Required.** Used to generate a snapshot tarball by the build system
testing/start_test.sh | **Required.** Used for install tests in the build system
diff                  | Allows to diff the repository contents with e.g. upstream.
dch                   | Helper script to update all changelog entries for a new release.



## Package Development <a id="introduction-package-development"></a>

* The `master` branch is the main development target.
* The `release` branch is updated for releases, usually by merging `master` into it

**RPM:**

* Upstream sources are pulled with `spectool`. This uses the `Source` URLs specified in the spec file.
* The package version is controlled by the `Version` and `Revision` entries in the spec file.
* For minor releases, make sure to increment the revision!

**Debian/Ubuntu:**

* The `dch` helper script requires the Git configuration entries for `user.name` and `user.email`.
* The package version is controlled by `debian/changelog` version entry.
* Ensure that the **package revision** is correctly set inside the `debian/changelog` file.
  This must be passed to the `dch` helper script too.

```
./dch 2.8.1-2 "Update to 2.8.1-2"
```

## Test Feature Branches <a id="introduction-packages-rpm-branches"></a>

The build system allows to build feature branches based on upstream feature branches.

The Icinga 2 feature branch called `feature/api-pretty` can be built with the
corresponding `rpm/` prefix to the branch name in this repository, e.g. `rpm/feature/api-pretty`.
