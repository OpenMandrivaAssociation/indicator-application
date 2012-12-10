Summary:	Displays application menu's on panel
Name:		indicator-application
Version:	12.10.0
Release:	1
License:	GPLv3
Group:		Graphical desktop/GNOME
Url:		http://launchpad.net/indicator-application
Source0:	%{name}-%{version}.tar.gz
source1:	.abf.yml

BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(json-glib-1.0)
buildrequires:	pkgconfig(dbusmenu-gtk3-0.4)


%description
This package provides a library and an indicator to take the menus from
applications and displays them on the panel bar.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING
%{_libexecdir}/indicator-application-service
%{_libdir}/indicators3/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/indicator-application/



%changelog
* Fri Apr 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.4.0-1
+ Revision: 789550
- imported package indicator-application

