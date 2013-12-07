%define _disable_ld_no_undefined	1
%define Werror_cflags			%nil

%define url_ver		 %(echo %{version} | cut -d "." -f -2)

Name:		shotwell
Version:	0.14.1
Release:	2
Summary:	A photo organizer designed for GNOME
License:	LGPLv2+ and CC-BY-SA
Group:		Graphics
Url:		http://www.yorba.org/shotwell/
Source0:	http://www.yorba.org/download/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	vala
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gexiv2)
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(webkitgtk-3.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(unique-3.0)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(rest-0.7)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-pbutils-0.10)
BuildRequires:	pkgconfig(json-glib-1.0)

%description
Shotwell is a digital photo organizer designed for the GNOME desktop 
environment. It allows you to import photos from disk or camera, 
organize them in various ways, view them in full-window or fullscreen 
mode, and export them to share with others.

%prep
%setup -q -n %{name}-%{version}

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



%changelog
* Mon Oct 15 2012 Arkady L. Shane <ashejn@rosalab.ru> 0.13.1-1
- update to 0.13.1

* Tue May 29 2012 Guilherme Moro <guilherme@mandriva.com> 0.12.3-1
+ Revision: 801025
- Updated to version 0.12.3

* Tue May 08 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.12.2-1
+ Revision: 797353
- version update 0.12.2
- build fix for vala 0.12.1
- version update to 0.11.6

* Wed Oct 26 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.11.5-2
+ Revision: 707416
- fix file package conflic via shotwell and glib-2

* Wed Oct 26 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.11.5-1
+ Revision: 707299
- updated to upstream release see #64560

* Wed Aug 17 2011 Alexander Barakin <abarakin@mandriva.org> 0.10.1-4
+ Revision: 694875
- increase release number
- correct dependency on yelp

* Fri Aug 12 2011 Alexander Barakin <abarakin@mandriva.org> 0.10.1-3
+ Revision: 694148
- help needs yelp #63897

* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 0.10.1-2
+ Revision: 686118
- rebuild for new webkit

* Sat Jun 04 2011 Funda Wang <fwang@mandriva.org> 0.10.1-1
+ Revision: 682698
- update to new version 0.10.1

* Fri May 27 2011 Funda Wang <fwang@mandriva.org> 0.10-1
+ Revision: 679243
- more linkage fix
- new version 0.10

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.9.3-2
+ Revision: 677833
- rebuild to add gconftool as req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.9.3-1
+ Revision: 657728
- new version 0.9.3

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 0.9.1-1
+ Revision: 650606
- new version 0.9.1

* Fri Feb 04 2011 Funda Wang <fwang@mandriva.org> 0.8.1-1
+ Revision: 635838
- BR libgomp-devel
- new version 0.8.1

* Fri Dec 24 2010 Funda Wang <fwang@mandriva.org> 0.8.0-1mdv2011.0
+ Revision: 624566
- update BR
- new version 0.8.0

  + Götz Waschk <waschk@mandriva.org>
    - bump vala dep

* Sat Sep 11 2010 Funda Wang <fwang@mandriva.org> 0.7.2-1mdv2011.0
+ Revision: 577145
- update to new version 0.7.2

* Sat Aug 28 2010 Funda Wang <fwang@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 573664
- new version 0.7.1

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 571747
- new version 0.7.0

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2011.0
+ Revision: 565620
- add upstream patch to build with vala 0.9.3
- New version 0.6.1

* Fri May 28 2010 Antoine Ginies <aginies@mandriva.com> 0.5.2-1mdv2010.1
+ Revision: 546490
- more languages support (Czech, Finnish, Greek, and Ukrainian), remove patch (integrated upstream)

* Wed Apr 21 2010 Frederik Himpe <fhimpe@mandriva.org> 0.5.0-1mdv2010.1
+ Revision: 537732
- Fix BuildRequires
- Update to new version 0.5.0
- Add patch from Debian to build with vala 0.8
- Don't update icon cache while building package

* Sun Jan 24 2010 Frederik Himpe <fhimpe@mandriva.org> 0.4.3-1mdv2010.1
+ Revision: 495530
- update to new version 0.4.3

* Wed Jan 06 2010 Jérôme Brenier <incubusss@mandriva.org> 0.4.2-1mdv2010.1
+ Revision: 486757
- new version 0.4.2
- add minimal version for some BuildRequires

* Sun Dec 27 2009 Jérôme Brenier <incubusss@mandriva.org> 0.4.1-1mdv2010.1
+ Revision: 482593
- add a buildroot tag
- import shotwell


