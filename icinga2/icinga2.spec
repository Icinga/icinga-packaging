#/******************************************************************************
# * Icinga 2                                                                   *
# * Copyright (C) 2012-2017 Icinga Development Team (https://www.icinga.com/)  *
# *                                                                            *
# * This program is free software; you can redistribute it and/or              *
# * modify it under the terms of the GNU General Public License                *
# * as published by the Free Software Foundation; either version 2             *
# * of the License, or (at your option) any later version.                     *
# *                                                                            *
# * This program is distributed in the hope that it will be useful,            *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of             *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              *
# * GNU General Public License for more details.                               *
# *                                                                            *
# * You should have received a copy of the GNU General Public License          *
# * along with this program; if not, write to the Free Software Foundation     *
# * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.             *
# ******************************************************************************/

%define revision 2

# make sure that _rundir is working on older systems
%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif

%define _libexecdir %{_prefix}/lib/
%define plugindir %{_libdir}/nagios/plugins

%if "%{_vendor}" == "redhat"
%define apachename httpd
%define apacheconfdir %{_sysconfdir}/httpd/conf.d
%define apacheuser apache
%define apachegroup apache

%if 0%{?el5}%{?el6}%{?amzn}
%define use_systemd 0
%define use_selinux 0
%if %(uname -m) != "x86_64"
%define march_flag -march=i686
%endif
%else
# fedora and el>=7
%define use_systemd 1
%define use_selinux 1
%if 0%{?fedora} >= 24
# for installing limits.conf on systemd >= 228
%define configure_systemd_limits 1
%else
%define configure_systemd_limits 0
%endif
%endif
%endif

%if "%{_vendor}" == "suse"
%define plugindir %{_libexecdir}/nagios/plugins
%define apachename apache2
%define apacheconfdir  %{_sysconfdir}/apache2/conf.d
%define apacheuser wwwrun
%define apachegroup www
%if 0%{?suse_version} >= 1310
%define use_systemd 1
%if 0%{?sle_version} >= 120200 || 0%{?suse_version} > 1320
# for installing limits.conf on systemd >= 228
%define configure_systemd_limits 1
%else
%define configure_systemd_limits 0
%endif
%else
%define use_systemd 0
%endif
%endif

%define icinga_user icinga
%define icinga_group icinga
%define icingacmd_group icingacmd

%define logmsg logger -t %{name}/rpm

Summary: Network monitoring application
Name: icinga2
Version: 2.8.0
Release: %{revision}%{?dist}
License: GPLv2+
URL: https://www.icinga.com/
Group: System/Monitoring
Source: https://github.com/Icinga/%{name}/archive/v%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires: %{name}-bin = %{version}-%{release}

%description
Meta package for Icinga 2 Core, DB IDO and Web.

%package bin
Summary:      Icinga 2 binaries and libraries
Group:        System/Monitoring

%if "%{_vendor}" == "suse"
PreReq:        permissions
Provides:      monitoring_daemon
Recommends:    monitoring-plugins
%if 0%{?suse_version} >= 1310
BuildRequires: libyajl-devel
%endif
%endif
BuildRequires: libedit-devel
BuildRequires: ncurses-devel
%if "%{_vendor}" == "suse" && 0%{?suse_version} < 1210
BuildRequires: gcc48-c++
BuildRequires: libstdc++48-devel
BuildRequires: libopenssl1-devel
%else
%if "%{_vendor}" == "redhat" && (0%{?el5} || 0%{?rhel} == 5 || "%{?dist}" == ".el5" || 0%{?el6} || 0%{?rhel} == 6 || "%{?dist}" == ".el6")
# Requires devtoolset-2 scl
BuildRequires: devtoolset-2-gcc-c++
BuildRequires: devtoolset-2-libstdc++-devel
BuildRequires: devtoolset-2-binutils
%define scl_enable scl enable devtoolset-2 --
%else
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
%endif
BuildRequires: openssl-devel
%endif
BuildRequires: cmake
BuildRequires: flex >= 2.5.35
BuildRequires: bison
BuildRequires: make
%if 0%{?fedora}
BuildRequires: wxGTK3-devel
%endif

%if 0%{?build_icinga_org} && "%{_vendor}" == "redhat" && (0%{?el5} || 0%{?rhel} == 5 || "%{?dist}" == ".el5" || 0%{?el6} || 0%{?rhel} == 6 || "%{?dist}" == ".el6")
# el5 and el6 require packages.icinga.com
BuildRequires: boost153-devel
%else
%if 0%{?build_icinga_org} && "%{_vendor}" == "suse" && 0%{?suse_version} < 1310
# sles 11 sp3 requires packages.icinga.com
BuildRequires: boost153-devel
%else
%if (0%{?el5} || 0%{?rhel} == 5 || "%{?dist}" == ".el5" || 0%{?el6} || 0%{?rhel} == 6 || "%{?dist}" == ".el6")
# Requires EPEL repository
BuildRequires: boost148-devel >= 1.48
%else
BuildRequires: boost-devel >= 1.48
%endif
%endif
%endif

%if 0%{?use_systemd}
BuildRequires: systemd
Requires: systemd
%endif

Requires: %{name}-libs = %{version}-%{release}

%description bin
Icinga 2 is a general-purpose network monitoring application.
This subpackage provides the binaries for Icinga 2 Core.

%package common
Summary:      Common Icinga 2 configuration
Group:        System/Monitoring
%if (0%{?amzn} || 0%{?fedora} || 0%{?rhel})
Requires(pre):  shadow-utils
Requires(post): shadow-utils
%endif
BuildRequires:  logrotate
%if "%{_vendor}" == "suse"
Requires(pre):  shadow
Requires(post): shadow
# Coreutils is added because of autoyast problems reported
Requires(pre):  coreutils
Requires(post): coreutils
%if 0%{?suse_version} >= 1200
BuildRequires:  monitoring-plugins-common
Requires:       monitoring-plugins-common
%else
Recommends:     monitoring-plugins-common
%endif
Recommends:     logrotate
%endif

%description common
This subpackage provides common directories, and the UID and GUID definitions
among Icinga 2 related packages.


%package doc
Summary:      Documentation for Icinga 2
Group:        Documentation/Other

%description doc
This subpackage provides documentation for Icinga 2.


%package libs
Summary:      Libraries for Icinga 2
Group:        System/Libraries
Requires:     %{name}-common = %{version}-%{release}

%description libs
This subpackage provides the internal libraries for the daemon or studio.


%package ido-mysql
Summary:      IDO MySQL database backend for Icinga 2
Group:        System/Monitoring
%if "%{_vendor}" == "suse"
BuildRequires: libmysqlclient-devel
%if 0%{?suse_version} >= 1310
BuildRequires: mysql-devel
%endif

%else
BuildRequires: mysql-devel
%endif #suse

Requires: %{name} = %{version}-%{release}

%description ido-mysql
Icinga 2 IDO mysql database backend. Compatible with Icinga 1.x
IDOUtils schema >= 1.12


%package ido-pgsql
Summary:      IDO PostgreSQL database backend for Icinga 2
Group:        System/Monitoring
%if "%{_vendor}" == "suse" && 0%{?suse_version} < 1210
BuildRequires: postgresql-devel >= 8.4
%else
BuildRequires: postgresql-devel
%endif
Requires: %{name} = %{version}-%{release}

%description ido-pgsql
Icinga 2 IDO PostgreSQL database backend. Compatible with Icinga 1.x
IDOUtils schema >= 1.12

%if 0%{?use_selinux}
%global selinux_variants mls targeted
%global selinux_modulename %{name}

%package selinux
Summary:        SELinux policy module supporting icinga2
Group:          System/Base
BuildRequires:  checkpolicy, selinux-policy-devel, hardlink
Requires:       %{name} = %{version}-%{release}
Requires(post):   policycoreutils-python
Requires(postun): policycoreutils-python

%description selinux
SELinux policy module supporting icinga2
%endif


%if 0%{?fedora}
%package studio
Summary:      Studio for Icinga 2
Group:        System/Monitoring
Requires:     %{name}-libs = %{version}-%{release}
Requires:     wxGTK3

%description studio
Provides a GUI for the Icinga 2 API.
%endif


%package -n vim-icinga2
Summary:      Vim syntax highlighting for icinga2
Group:        Productivity/Text/Editors
%if "%{_vendor}" == "suse"
BuildRequires: vim
Requires:      vim
%else
Requires:      vim-filesystem
%endif

%description -n vim-icinga2
Vim syntax highlighting for icinga2


%package -n nano-icinga2
Summary:       Nano syntax highlighting for icinga2
Group:         Productivity/Text/Editors
Requires:      nano

%description -n nano-icinga2
Nano syntax highlighting for icinga2

%prep
%setup -q -n %{name}-%{version}

%build
CMAKE_OPTS="-DCMAKE_INSTALL_PREFIX=/usr \
         -DCMAKE_INSTALL_SYSCONFDIR=/etc \
         -DCMAKE_INSTALL_LOCALSTATEDIR=/var \
         -DCMAKE_BUILD_TYPE=RelWithDebInfo \
         -DICINGA2_LTO_BUILD=ON \
         -DCMAKE_VERBOSE_MAKEFILE=ON \
         -DBoost_NO_BOOST_CMAKE=ON \
         -DICINGA2_PLUGINDIR=%{plugindir} \
         -DICINGA2_RUNDIR=%{_rundir} \
         -DICINGA2_USER=%{icinga_user} \
         -DICINGA2_GROUP=%{icinga_group} \
         -DICINGA2_COMMAND_GROUP=%{icingacmd_group}"
%if 0%{?fedora}
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_STUDIO=true"
%endif
%if "%{_vendor}" == "redhat"
%if 0%{?el5} || 0%{?rhel} == 5 || "%{?dist}" == ".el5" || 0%{?el6} || 0%{?rhel} == 6 || "%{?dist}" == ".el6"
%if 0%{?build_icinga_org}
# Boost_VERSION 1.41.0 vs 101400 - disable build tests
# details in https://dev.icinga.com/issues/5033
CMAKE_OPTS="$CMAKE_OPTS -DBOOST_LIBRARYDIR=%{_libdir}/boost153 \
 -DBOOST_INCLUDEDIR=/usr/include/boost153 \
 -DBoost_ADDITIONAL_VERSIONS='1.53;1.53.0'"
%else
CMAKE_OPTS="$CMAKE_OPTS -DBOOST_LIBRARYDIR=%{_libdir}/boost148 \
 -DBOOST_INCLUDEDIR=/usr/include/boost148 \
 -DBoost_ADDITIONAL_VERSIONS='1.48;1.48.0'"
%endif
CMAKE_OPTS="$CMAKE_OPTS \
 -DBoost_NO_SYSTEM_PATHS=TRUE \
 -DBUILD_TESTING=FALSE \
 -DBoost_NO_BOOST_CMAKE=TRUE"
%endif
%endif

%if "%{_vendor}" == "suse" && 0%{?suse_version} < 1310
CMAKE_OPTS="$CMAKE_OPTS -DBOOST_LIBRARYDIR=%{_libdir}/boost153 \
 -DBOOST_INCLUDEDIR=/usr/include/boost153 \
 -DBoost_ADDITIONAL_VERSIONS='1.53;1.53.0' \
 -DBoost_NO_SYSTEM_PATHS=TRUE \
 -DBUILD_TESTING=FALSE \
 -DBoost_NO_BOOST_CMAKE=TRUE"
%endif

%if 0%{?use_systemd}
CMAKE_OPTS="$CMAKE_OPTS -DUSE_SYSTEMD=ON"
%endif

%if "%{_vendor}" == "suse" && 0%{?suse_version} < 1210
# from package gcc48-c++
export CC=gcc-4.8
export CXX=g++-4.8
%endif

%{?scl_enable} cmake $CMAKE_OPTS -DCMAKE_C_FLAGS:STRING="%{optflags} %{?march_flag}" -DCMAKE_CXX_FLAGS:STRING="%{optflags} %{?march_flag}" .

make %{?_smp_mflags}

%if 0%{?use_selinux}
cd tools/selinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv %{selinux_modulename}.pp %{selinux_modulename}.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -
%endif

%install
make install \
        DESTDIR="%{buildroot}"

# install custom limits.conf for systemd
%if 0%{?configure_systemd_limits}
# for > 2.8 or > 2.7.2
install -D -m 0644 etc/initsystem/icinga2.service.limits.conf %{buildroot}/etc/systemd/system/%{name}.service.d/limits.conf
%endif

# remove features-enabled symlinks
rm -f %{buildroot}/%{_sysconfdir}/%{name}/features-enabled/*.conf

# enable suse rc links
%if "%{_vendor}" == "suse"
%if 0%{?use_systemd}
  ln -sf /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}
%else
  ln -sf ../../%{_initrddir}/%{name} "%{buildroot}%{_sbindir}/rc%{name}"
%endif
mkdir -p "%{buildroot}%{_localstatedir}/adm/fillup-templates/"
mv "%{buildroot}%{_sysconfdir}/sysconfig/%{name}" "%{buildroot}%{_localstatedir}/adm/fillup-templates/sysconfig.%{name}"
%endif

%if 0%{?use_selinux}
cd tools/selinux
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 %{selinux_modulename}.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{selinux_modulename}.pp
done
cd -

# TODO: Fix build problems on Icinga, see https://github.com/Icinga/puppet-icinga_build/issues/11
#/usr/sbin/hardlink -cv %%{buildroot}%%{_datadir}/selinux
%endif

%if 0%{?fedora}
mkdir -p "%{buildroot}%{_datadir}/icinga2-studio"
install -p -m 644 icinga-studio/icinga.ico %{buildroot}%{_datadir}/icinga2-studio

mkdir -p "%{buildroot}%{_datadir}/applications"
echo "[Desktop Entry]
Name=Icinga 2 Studio
Comment=API viewer for Icinga 2
TryExec=icinga-studio
Exec=icinga-studio
Icon=/usr/share/icinga2-studio/icinga.ico
StartupNotify=true
Terminal=false
Type=Application
Categories=GTK;Utility;
Keywords=Monitoring;" > %{buildroot}%{_datadir}/applications/icinga2-studio.desktop
%endif

%if "%{_vendor}" == "suse"
install -D -m 0644 tools/syntax/vim/syntax/%{name}.vim %{buildroot}%{_datadir}/vim/site/syntax/%{name}.vim
install -D -m 0644 tools/syntax/vim/ftdetect/%{name}.vim %{buildroot}%{_datadir}/vim/site/ftdetect/%{name}.vim
%else
install -D -m 0644 tools/syntax/vim/syntax/%{name}.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{name}.vim
install -D -m 0644 tools/syntax/vim/ftdetect/%{name}.vim %{buildroot}%{_datadir}/vim/vimfiles/ftdetect/%{name}.vim
%endif

install -D -m 0644 tools/syntax/nano/%{name}.nanorc %{buildroot}%{_datadir}/nano/%{name}.nanorc

%pre common
getent group %{icinga_group} >/dev/null || %{_sbindir}/groupadd -r %{icinga_group}
getent group %{icingacmd_group} >/dev/null || %{_sbindir}/groupadd -r %{icingacmd_group}
getent passwd %{icinga_user} >/dev/null || %{_sbindir}/useradd -c "icinga" -s /sbin/nologin -r -d %{_localstatedir}/spool/%{name} -G %{icingacmd_group} -g %{icinga_group} %{icinga_user}

%if "%{_vendor}" == "suse"
%if 0%{?use_systemd}
  %service_add_pre %{name}.service
%endif
%endif

%if "%{_vendor}" == "suse"
%verifyscript bin
%verify_permissions -e %{_rundir}/%{name}/cmd
%endif

%post bin

# suse
%if "%{_vendor}" == "suse"

%if 0%{?suse_version} >= 1310
%set_permissions %{_rundir}/%{name}/cmd
%endif

%endif #suse/rhel

%post common
# suse
%if "%{_vendor}" == "suse"
%if 0%{?use_systemd}
%fillup_only  %{name}
%service_add_post %{name}.service
%else
%fillup_and_insserv %{name}
%endif

if [ ${1:-0} -eq 1 ]
then
        # initial installation, enable default features
        for feature in checker notification mainlog; do
                ln -sf ../features-available/${feature}.conf %{_sysconfdir}/%{name}/features-enabled/${feature}.conf
        done
fi

exit 0

%else
# rhel

%if 0%{?use_systemd}
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name}
%endif

if [ ${1:-0} -eq 1 ]
then
        # initial installation, enable default features
        for feature in checker notification mainlog; do
                ln -sf ../features-available/${feature}.conf %{_sysconfdir}/%{name}/features-enabled/${feature}.conf
        done
fi

exit 0

%endif
# suse/rhel

%postun common
# suse
%if "%{_vendor}" == "suse"
%if 0%{?use_systemd}
  %service_del_postun %{name}.service
%else
  %restart_on_update %{name}
  %insserv_cleanup
%endif

%else
# rhel

%if 0%{?use_systemd}
%systemd_postun_with_restart %{name}.service
%else
if [ "$1" -ge  "1" ]; then
        /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi
%endif

%endif
# suse / rhel

if [ "$1" = "0" ]; then
        # deinstallation of the package - remove enabled features
        rm -rf %{_sysconfdir}/%{name}/features-enabled
fi

exit 0

%preun common
# suse
%if "%{_vendor}" == "suse"

%if 0%{?use_systemd}
  %service_del_preun %{name}.service
%else
  %stop_on_removal %{name}
%endif

exit 0

%else
# rhel

%if 0%{?use_systemd}
%systemd_preun %{name}.service
%else
if [ "$1" = "0" ]; then
        /sbin/service %{name} stop > /dev/null 2>&1 || :
        /sbin/chkconfig --del %{name} || :
fi
%endif

exit 0

%endif
# suse / rhel

%post ido-mysql
if [ ${1:-0} -eq 1 ]
then
        # initial installation, enable ido-mysql feature
        ln -sf ../features-available/ido-mysql.conf %{_sysconfdir}/%{name}/features-enabled/ido-mysql.conf
fi

exit 0

%postun ido-mysql
if [ "$1" = "0" ]; then
        # deinstallation of the package - remove feature
        rm -f %{_sysconfdir}/%{name}/features-enabled/ido-mysql.conf
fi

exit 0

%post ido-pgsql
if [ ${1:-0} -eq 1 ]
then
        # initial installation, enable ido-pgsql feature
        ln -sf ../features-available/ido-pgsql.conf %{_sysconfdir}/%{name}/features-enabled/ido-pgsql.conf
fi

exit 0

%postun ido-pgsql
if [ "$1" = "0" ]; then
        # deinstallation of the package - remove feature
        rm -f %{_sysconfdir}/%{name}/features-enabled/ido-pgsql.conf
fi

exit 0

%if 0%{?use_selinux}
%post selinux
for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/%{selinux_modulename}.pp &> /dev/null || :
done
/sbin/fixfiles -R icinga2-bin restore &> /dev/null || :
/sbin/fixfiles -R icinga2-common restore &> /dev/null || :
/sbin/semanage port -a -t icinga2_port_t -p tcp 5665 &> /dev/null || :

%postun selinux
if [ $1 -eq 0 ] ; then
  /sbin/semanage port -d -t icinga2_port_t -p tcp 5665 &> /dev/null || :
  for selinuxvariant in %{selinux_variants}
  do
     /usr/sbin/semodule -s ${selinuxvariant} -r %{selinux_modulename} &> /dev/null || :
  done
  /sbin/fixfiles -R icinga2-bin restore &> /dev/null || :
  /sbin/fixfiles -R icinga2-common restore &> /dev/null || :
fi
%endif


%files
%defattr(-,root,root,-)
%doc COPYING

%files bin
%defattr(-,root,root,-)
%doc COPYING COPYING.Exceptions README.md NEWS AUTHORS CHANGELOG.md
%{_sbindir}/%{name}
%dir %{_libdir}/%{name}/sbin
%{_libdir}/%{name}/sbin/%{name}
%{plugindir}/check_nscp_api
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/include
%{_mandir}/man8/%{name}.8.gz

%files libs
%defattr(-,root,root,-)
%doc COPYING COPYING.Exceptions README.md NEWS AUTHORS CHANGELOG.md
%exclude %{_libdir}/%{name}/libdb_ido_mysql*
%exclude %{_libdir}/%{name}/libdb_ido_pgsql*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so*

%files common
%defattr(-,root,root,-)
%doc COPYING COPYING.Exceptions README.md NEWS AUTHORS CHANGELOG.md tools/syntax
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sysconfdir}/bash_completion.d/%{name}
%if 0%{?use_systemd}
%attr(644,root,root) %{_unitdir}/%{name}.service
%if 0%{?configure_systemd_limits}
%dir /etc/systemd/system/%{name}.service.d
%attr(644,root,root) %config(noreplace) /etc/systemd/system/%{name}.service.d/limits.conf
%endif
%else
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/init.d/%{name}
%endif
%if "%{_vendor}" == "suse"
%{_sbindir}/rc%{name}
%{_localstatedir}/adm/fillup-templates/sysconfig.%{name}
%else
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%endif
%attr(0750,root,%{icinga_group}) %dir %{_sysconfdir}/%{name}
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/conf.d
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/features-available
%exclude %{_sysconfdir}/%{name}/features-available/ido-*.conf
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/features-enabled
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/scripts
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/zones.d
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %attr(0640,root,%{icinga_group}) %{_sysconfdir}/%{name}/init.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/constants.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/zones.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/conf.d/*.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/features-available/*.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/zones.d/*
%config(noreplace) %{_sysconfdir}/%{name}/scripts/*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/prepare-dirs
%{_libexecdir}/%{name}/safe-reload
%attr(0750,%{icinga_user},%{icingacmd_group}) %{_localstatedir}/cache/%{name}
%attr(0750,%{icinga_user},%{icingacmd_group}) %dir %{_localstatedir}/log/%{name}
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/log/%{name}/crash
%attr(0750,%{icinga_user},%{icingacmd_group}) %dir %{_localstatedir}/log/%{name}/compat
%attr(0750,%{icinga_user},%{icingacmd_group}) %dir %{_localstatedir}/log/%{name}/compat/archives
%attr(0750,%{icinga_user},%{icinga_group}) %{_localstatedir}/lib/%{name}
%attr(0750,%{icinga_user},%{icingacmd_group}) %ghost %{_rundir}/%{name}
%attr(2750,%{icinga_user},%{icingacmd_group}) %ghost %{_rundir}/%{name}/cmd
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/spool/%{name}
%attr(0770,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/spool/%{name}/perfdata
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/spool/%{name}/tmp
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_datadir}/%{name}/include
%{_datadir}/%{name}/include

%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/%{name}
%docdir %{_datadir}/doc/%{name}

%files ido-mysql
%defattr(-,root,root,-)
%doc COPYING COPYING.Exceptions README.md NEWS AUTHORS CHANGELOG.md
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/features-available/ido-mysql.conf
%{_libdir}/%{name}/libdb_ido_mysql*
%{_datadir}/icinga2-ido-mysql

%files ido-pgsql
%defattr(-,root,root,-)
%doc COPYING COPYING.Exceptions README.md NEWS AUTHORS CHANGELOG.md
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/features-available/ido-pgsql.conf
%{_libdir}/%{name}/libdb_ido_pgsql*
%{_datadir}/icinga2-ido-pgsql

%if 0%{?use_selinux}
%files selinux
%defattr(-,root,root,0755)
%doc tools/selinux/*
%{_datadir}/selinux/*/%{selinux_modulename}.pp
%endif

%if 0%{?fedora}
%files studio
%defattr(-,root,root,-)
%{_bindir}/icinga-studio
%{_datadir}/icinga2-studio
%{_datadir}/applications/icinga2-studio.desktop
%endif

%files -n vim-icinga2
%defattr(-,root,root,-)
%if "%{_vendor}" == "suse"
%{_datadir}/vim/site/syntax/%{name}.vim
%{_datadir}/vim/site/ftdetect/%{name}.vim
%else
%{_datadir}/vim/vimfiles/syntax/%{name}.vim
%{_datadir}/vim/vimfiles/ftdetect/%{name}.vim
%endif

%files -n nano-icinga2
%defattr(-,root,root,-)
%if "%{_vendor}" == "suse"
%dir %{_datadir}/nano
%endif
%{_datadir}/nano/%{name}.nanorc

%changelog
* Fri Nov 24 2017 Markus Frosch <markus.frosch@icinga.com> 2.8.0-2
- [SLES] Add systemd limits file
- Add config(noreplace) for the systemd limits file
  (no need to release every OS immediately)
- Update SELinux handling to be compatible to Fedora 27
  (only affecting f27 builds)

* Thu Nov 16 2017 Jean Flach <jean-marcel.flach@icinga.com> 2.8.0-1
- Update to 2.8.0

* Thu Nov 09 2017 Gunnar Beutner <gunnar.beutner@icinga.com> 2.7.2-1
- Update to 2.7.2

* Mon Oct 02 2017 Markus Frosch <markus.frosch@icinga.com> 2.7.1-2
- Fixing systemd limit issues on openSUSE > 42.1

* Thu Sep 21 2017 Michael Friedrich <michael.friedrich@icinga.com> 2.7.1-1
- Update to 2.7.1

* Tue Jun 20 2017 Markus Frosch <markus.frosch@icinga.com> 2.7.0-1
- Update to 2.7.0
