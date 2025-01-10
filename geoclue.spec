#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: f4a13a5a93c1
#
Name     : geoclue
Version  : 2.7.2
Release  : 34
URL      : https://gitlab.freedesktop.org/geoclue/geoclue/-/archive/2.7.2/geoclue-2.7.2.tar.gz
Source0  : https://gitlab.freedesktop.org/geoclue/geoclue/-/archive/2.7.2/geoclue-2.7.2.tar.gz
Source1  : geoclue.tmpfiles
Summary  : A convenience library to interact with Geoclue service
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: geoclue-config = %{version}-%{release}
Requires: geoclue-data = %{version}-%{release}
Requires: geoclue-lib = %{version}-%{release}
Requires: geoclue-libexec = %{version}-%{release}
Requires: geoclue-license = %{version}-%{release}
Requires: geoclue-man = %{version}-%{release}
Requires: geoclue-services = %{version}-%{release}
BuildRequires : ModemManager-dev
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : gobject-introspection-dev
BuildRequires : intltool-dev
BuildRequires : libnotify-dev
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libsoup-3.0)
BuildRequires : pkgconfig(systemd)
BuildRequires : vala
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: backport-Web-Source-Set-User-Agent-on-Soup-Session-Constructi.patch
Patch2: 0001-Redo-stateless-patch.patch

%description
Geoclue: The Geoinformation Service
===================================
Geoclue is a D-Bus geoinformation service. The goal of the Geoclue project
is to make creating location-aware applications as simple as possible.

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
Requires: geoclue-lib = %{version}-%{release}
Requires: geoclue-data = %{version}-%{release}
Provides: geoclue-devel = %{version}-%{release}
Requires: geoclue = %{version}-%{release}

%description dev
dev components for the geoclue package.


%package lib
Summary: lib components for the geoclue package.
Group: Libraries
Requires: geoclue-data = %{version}-%{release}
Requires: geoclue-libexec = %{version}-%{release}
Requires: geoclue-license = %{version}-%{release}

%description lib
lib components for the geoclue package.


%package libexec
Summary: libexec components for the geoclue package.
Group: Default
Requires: geoclue-config = %{version}-%{release}
Requires: geoclue-license = %{version}-%{release}

%description libexec
libexec components for the geoclue package.


%package license
Summary: license components for the geoclue package.
Group: Default

%description license
license components for the geoclue package.


%package man
Summary: man components for the geoclue package.
Group: Default

%description man
man components for the geoclue package.


%package services
Summary: services components for the geoclue package.
Group: Systemd services
Requires: systemd

%description services
services components for the geoclue package.


%prep
%setup -q -n geoclue-2.7.2
cd %{_builddir}/geoclue-2.7.2
%patch -P 1 -p1
%patch -P 2 -p1
pushd ..
cp -a geoclue-2.7.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736532854
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk-doc=false \
-Dcdma-source=false \
-Dnmea-source=false \
-Ddbus-sys-dir=/usr/share/dbus-1/system.d  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgtk-doc=false \
-Dcdma-source=false \
-Dnmea-source=false \
-Ddbus-sys-dir=/usr/share/dbus-1/system.d  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/geoclue
cp %{_builddir}/geoclue-%{version}/COPYING %{buildroot}/usr/share/package-licenses/geoclue/9f36ee7d499d8aacee2830333120c184f7d0cef9 || :
cp %{_builddir}/geoclue-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/geoclue/3ab14ae755fcd87385b7dc685e7e3dfb803b90b4 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/geoclue.conf
## install_append content
mkdir -p %{buildroot}/usr/share/xdg/autostart
mv %{buildroot}/etc/xdg/autostart/* %{buildroot}/usr/share/xdg/autostart/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/geoclue.conf

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
/usr/share/polkit-1/rules.d/org.freedesktop.GeoClue2.rules
/usr/share/vala/vapi/libgeoclue-2.0.deps
/usr/share/vala/vapi/libgeoclue-2.0.vapi
/usr/share/xdg/autostart/geoclue-demo-agent.desktop

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
/V3/usr/lib64/libgeoclue-2.so.0.0.0
/usr/lib64/libgeoclue-2.so.0
/usr/lib64/libgeoclue-2.so.0.0.0

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/geoclue
/V3/usr/libexec/geoclue-2.0/demos/agent
/V3/usr/libexec/geoclue-2.0/demos/where-am-i
/usr/libexec/geoclue
/usr/libexec/geoclue-2.0/demos/agent
/usr/libexec/geoclue-2.0/demos/where-am-i

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/geoclue/3ab14ae755fcd87385b7dc685e7e3dfb803b90b4
/usr/share/package-licenses/geoclue/9f36ee7d499d8aacee2830333120c184f7d0cef9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/geoclue.5

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/geoclue.service
