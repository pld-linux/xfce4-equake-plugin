Summary:	Earthquake monitor plugin for the Xfce panel
Name:		xfce4-equake-plugin
Version:	1.3.8.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-equake-plugin/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	07d42b8a3d440d6f1861048a6cc3a15a
URL:		http://www.e-quake.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	xfce4-dev-tools >= 4.11.0
BuildRequires:	xfce4-panel-devel >= 4.11.0
Requires:	xfce4-panel >= 4.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Equake monitors earthquakes and will display an update each time a new
earthquake occurs.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-equake-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-equake-plugin.desktop
%{_iconsdir}/hicolor/*x*/apps/xfce4-equake-plugin-icon.*
