#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : geoclue
Version  : 2.4.12
Release  : 17
URL      : https://www.freedesktop.org/software/geoclue/releases/2.4/geoclue-2.4.12.tar.xz
Source0  : https://www.freedesktop.org/software/geoclue/releases/2.4/geoclue-2.4.12.tar.xz
Summary  : A convenience library to interact with Geoclue service
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: geoclue-data
Requires: geoclue-lib
Requires: geoclue-bin
Requires: geoclue-license
Requires: geoclue-config
BuildRequires : ModemManager-dev
BuildRequires : desktop-file-utils
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd-dev
BuildRequires : vala
Patch1: 0001-Support-a-stateless-configuration.patch

%description
GeoClue: The Geoinformation Service
===================================
GeoClue is a D-Bus geoinformation service. The goal of the Geoclue project is to
make creating location-aware applications as simple as possible.

%package bin
Summary: bin components for the geoclue package.
Group: Binaries
Requires: geoclue-data
Requires: geoclue-config
Requires: geoclue-license

%description bin
bin components for the geoclue package.


%package config
Summary: config components for the geoclue package.
Group: Default

%description config
config components for the geoclue package.


%package data
Summary: data components for the geoclue package.
Group: Data

%description data
data components for the geoclue package.


%package dev
Summary: dev components for the geoclue package.
Group: Development
Requires: geoclue-lib
Requires: geoclue-bin
Requires: geoclue-data
Provides: geoclue-devel

%description dev
dev components for the geoclue package.


%package lib
Summary: lib components for the geoclue package.
Group: Libraries
Requires: geoclue-data
Requires: geoclue-license

%description lib
lib components for the geoclue package.


%package license
Summary: license components for the geoclue package.
Group: Default

%description license
license components for the geoclue package.


%prep
%setup -q -n geoclue-2.4.12
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534258883
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%reconfigure --disable-static --disable-cdma-source --disable-nmea-source --with-dbus-sys-dir=/usr/share/dbus-1/system.d
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534258883
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/geoclue
cp COPYING %{buildroot}/usr/share/doc/geoclue/COPYING
cp COPYING.LIB %{buildroot}/usr/share/doc/geoclue/COPYING.LIB
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/geoclue
/usr/libexec/geoclue-2.0/demos/agent
/usr/libexec/geoclue-2.0/demos/where-am-i

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/geoclue.service

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Geoclue-2.0.typelib
/usr/share/applications/geoclue-demo-agent.desktop
/usr/share/applications/geoclue-where-am-i.desktop
/usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.Agent.xml
/usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.Client.xml
/usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.Location.xml
/usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.Manager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.GeoClue2.xml
/usr/share/dbus-1/system-services/org.freedesktop.GeoClue2.service
/usr/share/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf
/usr/share/dbus-1/system.d/org.freedesktop.GeoClue2.conf
/usr/share/defaults/geoclue/geoclue.conf
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libgeoclue-2.0/gclue-client.h
/usr/include/libgeoclue-2.0/gclue-enum-types.h
/usr/include/libgeoclue-2.0/gclue-enums.h
/usr/include/libgeoclue-2.0/gclue-helpers.h
/usr/include/libgeoclue-2.0/gclue-location.h
/usr/include/libgeoclue-2.0/gclue-manager.h
/usr/include/libgeoclue-2.0/gclue-simple.h
/usr/include/libgeoclue-2.0/geoclue.h
/usr/lib64/libgeoclue-2.so
/usr/lib64/pkgconfig/geoclue-2.0.pc
/usr/lib64/pkgconfig/libgeoclue-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgeoclue-2.so.0
/usr/lib64/libgeoclue-2.so.0.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/geoclue/COPYING
/usr/share/doc/geoclue/COPYING.LIB
