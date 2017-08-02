Releasing a package
===================

**Note:** This is basically the same workflow for a full release, as well as a single release update to a distribution. It depends what you: change, build and publish

All required changed should have been pushed to the `*/snapshot` branch

Now we need to update the `*/release` branches with the new changes, either:

* Make a PR merging `*/snapshot` -> `*/release`
* **or:** Merge a specific branch of cherry picked commits from `*/snapshot` (In case we have mixed changes between packages)

## The pull-request

The PR should have the labels: `releases` and `<package>`

Subject:

    rpm: Release icinga2 2.7.0
    deb: Release icinga2 2.7.0

Here is a checklist for the PRs description, it should be followed!

```markdown
Checklist for releases:

* [ ] All spec or changelog have the correct version?
* [ ] Commit list only contains stuff related to the release? (or maybe doc changes)
* [ ] Are all snapshots built recently / with this state of the repository?
* [ ] Are all snapshot builds ok?
```

In case of Icinga 2 or Icingaweb 2 there are additions to the checklist regarding the test systems:

## Icinga 2 checklist

Please add this for icinga2, so we have the test systems in mind!

```markdown
## Test Systems: icinga2

We currently have: CentOS 7 & Debian 8

* [ ] Test System is up2date
* [ ] Icinga 2 is running (monitoring state ok)
* [ ] All cluster connections are fine
* [ ] No late checks, or problems we have to care about
```

**TODO:** Extend list ;-)

## Icingaweb2 checklist

```markdown
## Test Systems: icingaweb2

We currently have: CentOS 7 & Debian 8

* [ ] Test System is up2date
* [ ] Icingaweb2 and interaction with it is working
* [ ] Monitoring data can be displayed and accessed
```

**TODO:** Extend list ;-)

## Building releases

When the PR is merged, you can start triggering the release builds.

There is no button `build all`, please trigger all the builds, that should be build.

E.g. go to [icinga2-release](https://build.icinga.com/job/icinga2-release/) and start each `*-0source` job.

This will build the package and test its install locally. It is normal, that the publish job fails at first!

## Actually pushing packages to release

The publish job of release builds is set up, so it fails when started in the build chain.

This is meant to be triggered manually.

So the general release procedure is:

* Prepare release (PR and merging changes)
* Triggering build jobs
* Reviewing build state
* Triggering all the publish jobs when done

To actually release the package:

* Click `Build with parameters` on a `*-publish` job
* Check the checkbox at `allow_release`
* Click `Build`

## Selective merging

To merge certain changes here a few git CLI shorthands:

```
git branch -D rpm/release-icinga2-2.7.0
git checkout -b rpm/release-icinga2-2.7.0 rpm/release

git log --format="%h" rpm/release..rpm/snapshot icinga2/ | cut -d" " -f2 | tac | xargs git cherry-pick

git branch -D deb/release-icinga2-2.7.0
git checkout -b deb/release-icinga2-2.7.0 deb/release

git log --format="%h" deb/release..deb/snapshot icinga2/ | cut -d" " -f2 | tac | xargs git cherry-pick
```
