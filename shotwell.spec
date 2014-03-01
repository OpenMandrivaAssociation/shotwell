%define _disable_ld_no_undefined	1
%define Werror_cflags			%nil

%define url_ver		%(echo %{version} | cut -d "." -f -2)

Summary:	A photo organizer designed for GNOME
Name:		shotwell
Version:	0.15.0
Release:	1
License:	LGPLv2+ and CC-BY-SA
Group:		Graphics
Url:		http://www.yorba.org/shotwell/
Source0:	http://www.yorba.org/download/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	vala
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gexiv2) >= 0.4.90
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-pbutils-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(rest-0.7)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(webkitgtk-3.0)

%description
Shotwell is a digital photo organizer designed for the GNOME desktop
environment. It allows you to import photos from disk or camera,
organize them in various ways, view them in full-window or fullscreen
mode, and export them to share with others.

%prep
%setup -q

%build
%before_configure
./configure \
	--prefix=%{_prefix} \
	--lib=%{_lib} \
	--disable-schemas-compile \
	--disable-desktop-update \
	--disable-icon-update

%make

%install
%makeinstall_std

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS MAINTAINERS README COPYING NEWS THANKS
%{_bindir}/*
%{_libdir}/%{name}
/usr/libexec/%{name}
%{_datadir}/%{name}
%{_datadir}/gnome/help/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/GConf/gsettings/shotwell.convert
%{_datadir}/glib-2.0/schemas/org.yorba.shotwell*.gschema.xml

