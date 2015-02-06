Summary:	Displays application menu's on panel
Name:		indicator-application
Version:	12.10.0
Release:	3
License:	GPLv3+
Group:		Graphical desktop/GNOME
Url:		http://launchpad.net/indicator-application
Source0:	%{name}-%{version}.tar.gz
Patch0:		indicator-application-12.10.0-glib-deprecated.patch
BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(json-glib-1.0)

%description
This package provides a library and an indicator to take the menus from
applications and displays them on the panel bar.

%files
%doc AUTHORS COPYING
%{_libexecdir}/indicator-application-service
%{_libdir}/indicators3/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/indicator-application/

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std


