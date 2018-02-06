# Release Packages <a id="release-package"></a>

## Requirements <a id="release-package-requirements"></a>

* Upstream project has a Git tag and GitHub release
* build.icinga.com jobs are ready and working
* Snapshot package builds are not failing

## Preparations <a id="release-package-preparations"></a>

### Debian Builds on macOS <a id="release-package-preparations-macos"></a>

> **Note**
>
> This release package type requires the `dch` script which only is available on Debian/Ubuntu.

Instructions for macOS:

```
docker run -v $HOME/coding/icinga/rpm-icinga2:/mnt/packaging -ti ubuntu:xenial bash

apt-get update
apt-get install git dev-tools vim
cd /mnt/packaging

git config --global user.name "Michael Friedrich"
git config --global user.email "michael.friedrich@icinga.com"
```

### Checklist <a id="release-package-checklist"></a>

```markdown
* [ ] Upstream version files are uptodate
* [ ] RPM and Deb specific version bumps
* [ ] Changelog entries: Spec file (RPM) and control file (Debian)
* [ ] Only commit release specific changes, separate additional fixes into commits
* [ ] Snapshot builds on build.icinga.com are ok
```

#### Icinga 2 <a id="release-package-checklist-icinga2"></a>

```markdown
## Test Systems: icinga2

* [ ] Test system is running the latest snapshot packages.
* [ ] Icinga 2 is running (monitoring state ok).
* [ ] Cluster health check is ok.
* [ ] No late checks, or any other breaking changes.
```

#### Icinga Web 2 <a id="release-package-checklist-icingaweb2"></a>

```markdown
## Test Systems: icingaweb2

* [ ] Test system is running the latest snapshot packages.
* [ ] Icinga Web 2 is accessible and the monitoring health is ok.
* [ ] Dashboards and listings present current monitoring data.
```

## RPM Release <a id="release-package-rpm"></a>

Update required files. Ensure that the release commit only affects
release specific files. If you need to add for example specific
patches, commit them separately.

```
git checkout master && git pull

vim icinga2.spec
```

- Edit `Version` and `Revision`
- Add a changelog entry

```
git commit -av -m "Release 2.8.1-1"
git push origin master

git checkout release && git pull
git merge master
git push origin release
```

For minor releases just update `release`, and merge it back to `master`.

## DEB Release <a id="release-package-deb"></a>

Update required files. Ensure that the release commit only affects
release specific files. If you need to add for example specific
patches, commit them separately.

```
git checkout master && git pull

./dch 2.8.1-1 "Update to 2.8.1"

git commit -av -m "Release 2.8.1-1"
git push origin master

git checkout release && git pull
git merge master
git push origin release
```

For minor releases just update `release`, and merge it back to `master`.

## Build Release Package <a id="release-package-build"></a>

Once the release commit is pushed to `release` branch, you can start with building the released packages.

Go to [build.icinga.com](https://build.icinga.com) and log in. Navigate into the
project's release tree.

Each distribution needs to be started manually by kicking off the `-0source` build job.

For example open the [icinga2-release](https://build.icinga.com/job/icinga2-release/) tab
and start each `*-0source` job.

The build pipeline triggers additional jobs:

- Source package generation (started by you)
- (Binary) package builds
- Specific tests for this project

It then stops for review. This allows to inspect possible build failures prior to releasing
a broken package to users.

### Publish Release Package <a id="release-package-build-publish"></a>

In order to publish the built release packages, start the `-3-publish` jobs for each
distribution manually.

> **Tip**
>
> Start with RPM package jobs and kick off the Debian package jobs once succeeded.

Steps:

* Click the `Build with parameters` button on a `*-3-publish` job.
* Check the checkbox `allow_release` to actually publish the release.
* Click the `Build` button.


### Windows Release Package <a id="release-package-build-windows"></a>

> **Note**
>
> This builds the Icinga 2 Windows client package only.

Navigate to the [icinga2-windoows-package](https://build.icinga.com/view/Icinga%202/job/icinga2-windows-package/) job
and click on the `Build with Parameters` entry.

- branch: `tags/v2.8.1`
- pkgname: `v2.8.1`
- Click the `Build` button

This job publishes the binary package directly onto [packages.icinga.com](https://packages.icinga.com).

Upload the package to [chocolatey](https://chocolatey.org/packages/upload).
