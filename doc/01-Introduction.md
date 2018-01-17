# Introduction <a id="introduction"></a>

## RPM Packages <a id="introduction-packages-rpm"></a>

The `rpm/*` branches provide the scripts and sources to build RPM packages.

### Structure <a id="introduction-packages-rpm-structure"></a>

Each project is located in a separate directory.

* icinga2
* icingaweb2
* icinga-rpm-release

Each directory requires a spec file with their name. In addition to that optional patch and
source files can be added here.

Everything except the spec file is copied to the `SOURCES/` directory during the RPM package
build jobs.

Example tree:

* icinga2/
  * icinga2.spec
  * icinga2-critical-bug-1234.patch
  * file-to-include-as-source.txt

These scripts are used by the build infrastructure and help during package development too:

Script                                | Description
--------------------------------------|--------------------------------------
&lt;product&gt;/get_snapshot          | **Required.** Used to generate a snapshot tarball by the build system
&lt;product&gt;/testing/start_test.sh | **Required.** Used for install tests in the build system
&lt;product&gt;/diff                  | **Optional.** Allows to diff the repository contents with e.g. upstream.

These scripts may differ in specific branches.

### Package Development <a id="introduction-packages-rpm-development"></a>

* The `rpm/snapshot` branch is the main development target.
* The `rpm/release` branch is updated for releases
  * Cherry-pick the release commit from `rpm/snapshot` if this is a minor release.
  * Merge `rpm/snapshot` into `rpm/release` if this is a major release.
* Upstream sources are pulled with `spectool`. This uses the `Source` URLs specified in the spec file.

> **Note**
>
> The package version is controlled by the `Version` and `Revision` entries in the spec file.

#### Minor Package Only Releases <a id="introduction-packages-rpm-development-minor"></a>

* Ensure that the **package revision** is incremented in the spec file

### Test Feature Branches <a id="introduction-packages-rpm-branches"></a>

The build system allows to build feature branches based on upstream feature branches.

The Icinga 2 feature branch called `feature/api-pretty` can be built with the
corresponding `rpm/` prefix to the branch name in this repository, e.g. `rpm/feature/api-pretty`.


## Debian/Ubuntu Packages <a id="introduction-packages-deb"></a>

The `deb/*` branches provide the scripts and sources to build Debian/Ubuntu packages.

### Structure <a id="introduction-packages-deb-structure"></a>

Each project is located in a separate directory.

* icinga2
* icingaweb2

Each project has sub directories for the specific distribution they are built on.
This also allows for virtual directory names exposed to the build system.

* icinga2/jessie/
* icinga2/stretch/
* icinga2/ubuntu/
* icingaweb2/trusty/
* icingaweb2/xenial/

Each distribution directory provides the `debian/` directory where the package build
sources and control files are located.

* icinga2/
  * jessie/
    * debian/
      * control
      * changelog
      * rules
      * ...

> **Tip**
>
> You can only update a specific distribution and release minor package updates.

Script                                | Description
--------------------------------------|--------------------------------------
&lt;product&gt;/get_snapshot          | **Required.** Used to generate a snapshot tarball by the build system
&lt;product&gt;/testing/start_test.sh | **Required.** Used for install tests in the build system
&lt;product&gt;/diff                  | **Optional.** Allows to diff the repository contents with e.g. upstream.
&lt;product&gt;/dch                   | **Optional.** Helper script to update all changelog entries for a new release.

### Package Development <a id="introduction-packages-deb-development"></a>

* The `deb/snapshot` branch is the main development target.
* The `deb/release` branch is updated for releases
  * Cherry-pick the release commit from `deb/snapshot` if this is a minor release.
  * Merge `deb/snapshot` into `deb/release` if this is a major release.
* The `dch` helper script requires the Git configuration entries for `user.name` and `user.email`.

> **Note**
>
> The package version is controlled by `debian/changelog` version entry.


#### Minor Package Only Releases <a id="introduction-packages-deb-development-minor"></a>

* Ensure that the **package revision** is correctly set inside the `debian/changelog` file. This
must be passed to the `dch` helper script too.

```
./dch 2.8.1-2 "Update to 2.8.1-2"
```

### Test Feature Branches <a id="introduction-packages-deb-branches"></a>

The build system allows to build feature branches based on upstream feature branches.

The Icinga 2 feature branch called `feature/api-pretty` can be built with the
corresponding `deb/` prefix to the branch name in this repository, e.g. `deb/feature/api-pretty`.
