Name:			shotwell
Version:		0.4.1
Release:		%mkrel 1
Summary:		A photo organizer designed for GNOME
License:		LGPLv2+ and CC-BY-SA
Group:			Graphics
Url:			http://www.yorba.org/shotwell/
Source0:		http://www.yorba.org/download/shotwell/0.4/shotwell-%{version}.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:		vala >= 0.7.9
BuildRequires:		gettext
BuildRequires:		gtk+2-devel
BuildRequires:		hal-devel
BuildRequires:		libgee-devel
BuildRequires:		webkitgtk-devel
BuildRequires:		sqlite-devel
BuildRequires:		gphoto2-devel
BuildRequires:		libexif-devel
BuildRequires:		unique-devel

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
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

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
