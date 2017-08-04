%if 0%{?fedora}
%define pkgversion %{fedora}
%define pkgrepository fedora
%else
%if 0%{?rhel}
%define pkgversion %{rhel}
%define pkgrepository epel
%endif
%endif

Name:		icinga-rpm-release
Version:	%{pkgversion}
Release:	3%{?dist}
Summary:	Icinga Package Repository
Group:		System Environment/Base
License:	GPLv2
URL:		https://packages.icinga.com
Source1:	icinga.key
Source2:	ICINGA-release.repo
Source3:	ICINGA-snapshot.repo
Source4:	README.md

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch

%if 0%{?fedora}
Requires:	fedora-release >= %{version}
%else
%if 0%{?rhel}
Requires:	redhat-release >= %{version}
%endif
%endif

%description
This package contains the Icinga package repository GPG key
as well as configuration for yum.

%prep
%setup -q -c -T

%build
sed 's/@@repo@@/%{pkgrepository}/' %{SOURCE2} >ICINGA-release.repo
sed 's/@@repo@@/%{pkgrepository}/' %{SOURCE3} >ICINGA-snapshot.repo

%install
rm -rf $RPM_BUILD_ROOT

# GPG key
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ICINGA

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 ICINGA-release.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
install -pm 644 ICINGA-snapshot.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}
install -pm 644 %{SOURCE4} $RPM_BUILD_ROOT%{_docdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/*
%{_docdir}/%{name}

%changelog
* Fri Aug 4 2017 Markus Frosch <markus.frosch@icinga.com> %{version}-3
- Update specfile to a general version for all RedHat based dists
