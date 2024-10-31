%define _disable_ld_no_undefined 1
%define Werror_cflags %nil

%global optflags %{optflags} -Wno-incompatible-function-pointer-types

%define url_ver		%(echo %{version} | cut -d "." -f -2)

Summary:	A photo organizer designed for GNOME
Name:		shotwell
Version:	0.32.10
Release:	1
License:	LGPLv2+ and CC-BY-SA
Group:		Graphics
Url:		https://www.yorba.org/shotwell/
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		shotwell-0.32.2-no-sqlite3_trace.patch

BuildRequires:  itstool
BuildRequires:	vala
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	meson
BuildRequires:	pkgconfig(atk)
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gexiv2) >= 0.4.90
BuildRequires:	pkgconfig(gee-0.8)
#BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:  pkgconfig(libportal)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:	pkgconfig(rest-0.7)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	pkgconfig(libgdata)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	gomp-devel
BuildRequires:	pkgconfig(sqlite3)

%description
Shotwell is a digital photo organizer designed for the GNOME desktop
environment. It allows you to import photos from disk or camera,
organize them in various ways, view them in full-window or fullscreen
mode, and export them to share with others.

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
# otherwise gettext always returns English text regardless of LANGUAGE asked
export LANG=en_US.utf8
%meson_install || :

# we don't want these
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name 'lib%{name}-plugin-common.so' -delete

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%doc AUTHORS README.md NEWS THANKS
%license COPYING
%{_bindir}/*
%{_libdir}/%{name}/
%{_libexecdir}/%{name}/*
%{_datadir}/applications/org.gnome.Shotwell-Viewer.desktop
%{_datadir}/applications/org.gnome.Shotwell.desktop
%{_datadir}/applications/org.gnome.Shotwell.Auth.desktop
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Shotwell-symbolic.svg
%{_iconsdir}/hicolor/*/*/org.gnome.Shotwell.png
%{_libdir}/libshotwell-plugin*
%{_libdir}/lib%{name}-authenticator*
%{_datadir}/glib-2.0/schemas/org.gnome.shotwell-extras.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shotwell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.yorba.shotwell-extras.gschema.xml
%{_datadir}/glib-2.0/schemas/org.yorba.shotwell.gschema.xml
%{_datadir}/apport/package-hooks/*
%{_datadir}/metainfo/org.gnome.Shotwell.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Shotwell.svg
%{_mandir}/man1/%{name}.1*
