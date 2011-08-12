Name:			shotwell
Version:		0.10.1
Release:		%mkrel 3
Summary:		A photo organizer designed for GNOME
License:		LGPLv2+ and CC-BY-SA
Group:			Graphics
Url:			http://www.yorba.org/shotwell/
Source0:		http://www.yorba.org/download/shotwell/0.10/shotwell-%{version}.tar.bz2
Patch0:			shotwell-0.10-link.patch
Requires:		yelp >= 2.30.2-6
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:		vala >= 0.12.0
BuildRequires:		gettext
BuildRequires:		gtk+2-devel >= 2.14.4
BuildRequires:		libgee-devel >= 0.5.0
BuildRequires:		webkitgtk-devel >= 1.1.5
BuildRequires:		sqlite-devel >= 3.5.9
BuildRequires:		gphoto2-devel >= 2.4.2
BuildRequires:		libgexiv2-devel >= 0.1.0
BuildRequires:		unique-devel >= 1.0.0
BuildRequires:		libsoup-devel
BuildRequires:		dbus-glib-devel
BuildRequires:		libGConf2-devel
BuildRequires:		libgudev-devel
BuildRequires:		libraw-devel
BuildRequires:		libjson-glib-devel
BuildRequires:		libgomp-devel
BuildRequires:		gnome-vfs2-devel

%description
Shotwell is a digital photo organizer designed for the GNOME desktop 
environment. It allows you to import photos from disk or camera, 
organize them in various ways, view them in full-window or fullscreen 
mode, and export them to share with others.

%prep
%setup -q
%patch0 -p0

%build
%define _disable_ld_no_undefined 1
./configure --lib=%{_lib} --prefix=/usr --disable-schemas-install --assume-pkgs --disable-icon-update --disable-desktop-update
sed -i -e 's/\\n/\n/g' configure.mk
sed -i -e 's/^CFLAGS = .*$/CFLAGS = %{optflags} %{ldflags}/' Makefile
%make LDFLAGS="%ldflags"

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} --all-name

%clean
rm -rf %{buildroot}

%preun
%preun_uninstall_gconf_schemas %name

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS MAINTAINERS README COPYING NEWS THANKS
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/gnome/help/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
