Name:			shotwell
Version:		0.5.2
Release:		%mkrel 1
Summary:		A photo organizer designed for GNOME
License:		LGPLv2+ and CC-BY-SA
Group:			Graphics
Url:			http://www.yorba.org/shotwell/
Source0:		http://www.yorba.org/download/shotwell/0.5/shotwell-%{version}.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:		vala >= 0.7.9
BuildRequires:		gettext
BuildRequires:		gtk+2-devel >= 2.14.4
BuildRequires:		hal-devel >= 0.5.11
BuildRequires:		libgee-devel >= 0.5.0
BuildRequires:		webkitgtk-devel >= 1.1.5
BuildRequires:		sqlite-devel >= 3.5.9
BuildRequires:		gphoto2-devel >= 2.4.2
BuildRequires:		libexif-devel >= 0.6.16
BuildRequires:		unique-devel >= 1.0.0
BuildRequires:		libgudev-devel

%description
Shotwell is a digital photo organizer designed for the GNOME desktop 
environment. It allows you to import photos from disk or camera, 
organize them in various ways, view them in full-window or fullscreen 
mode, and export them to share with others.

%prep
%setup -q

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DISABLE_ICON_UPDATE=1 %makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS MAINTAINERS README COPYING NEWS THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_sysconfdir}/gconf/schemas/%{name}.schemas
