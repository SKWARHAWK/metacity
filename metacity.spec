Summary:	Metacity window manager
Summary(pl):	Zarz�dca okien metacity
Name:		metacity
Version:	2.5.2
Release:	2
License:	GPL
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5: 78a9bc7e61bcfeea3b63460c5628d1f3
Patch0:		%{name}-libtool.patch
URL:		http://people.redhat.com/~hp/metacity/
BuildRequires:	GConf2-devel >= 2.3.0
BuildRequires:	Xft-devel >= 2.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:  fontconfig-devel
BuildRequires:  xft-devel
BuildRequires:	pango-devel >= 1.2.0
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	startup-notification-devel
Requires(post):	/sbin/ldconfig
Requires(post):	GConf2 >= 2.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Metacity is a simple window manager that integrates nicely with
GNOME2.

%description -l pl
Metacity jest prostym zarz�dc� okien �adnie integruj�cym si� z GNOME2.

%package devel
Summary:	metacity - header files
Summary(pl):	metacity - pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains header files for metcity window manager.

%description devel -l pl
Pakiet zawieraj�cy pliki nag��wkowe zarz�dcy okien metacity.

%package static
Summary:	Static metacity library
Summary(pl):	Statyczna biblioteka metacity
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
                                                                                
%description static
Static version of metacity library.
                                                                                
%description static -l pl
Statyczna wersja biblioteki metacity.


# Here go themes:

%package        themes-AgingGorilla
Summary:        AgingGorilla theme for metacity
Summary(pl):    Motyw AgingGorilla dla metacity
Group:          Themes/Gtk
Requires:       %{name} >= %{version}


%description themes-AgingGorilla
AgingGorilla theme for metacity

%description themes-AgingGorilla -l pl
Motyw AgingGorilla dla metacity


%package        themes-Atlanta
Summary:        Atlanta theme for metacity
Summary(pl):    Motyw Atlanta dla metacity
Group:          Themes/Gtk
Requires:       %{name} >= %{version}

%description themes-Atlanta
Atlanta theme for metacity

%description themes-Atlanta -l pl
Motyw Atlanta dla metacity


%package        themes-Bright
Summary:        Bright theme for metacity
Summary(pl):    Motyw Bright dla metacity
Group:          Themes/Gtk
Requires:       %{name} >= %{version}

%description themes-Bright
Bright theme for metacity

%description themes-Bright -l pl
Motyw Bright dla metacity


%package        themes-Crux
Summary:        Crux theme for metacity
Summary(pl):    Motyw Crux dla metacity
Group:          Themes/Gtk
Requires:       %{name} >= %{version}

%description themes-Crux
Crux theme for metacity

%description themes-Crux -l pl
Motyw Crux dla metacity


%package        themes-Esco
Summary:        Esco theme for metacity
Summary(pl):    Motyw Esco dla metacity
Group:          Themes/Gtk
Requires:       %{name} >= %{version}

%description themes-Esco
Esco theme for metacity

%description themes-Esco -l pl
Motyw Esco dla metacity


%package        themes-Metabox
Summary:        Metabox theme for metacity
Summary(pl):    Motyw Metabox dla metacity
Group:          Themes/Gtk
Requires:       %{name} >= %{version}

%description themes-Metabox
Metabox theme for metacity

%description themes-Metabox -l pl
Motyw Metabox dla metacity


%package        themes-Simple
Summary:        Simple theme for metacity
Summary(pl):    Motyw Simple dla metacity
Group:          Themes/Gtk
Requires:       %{name} >= %{version}

%description themes-Simple
Simple theme for metacity

%description themes-Simple -l pl
Motyw Simple dla metacity

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopfilesdir=%{_wmpropsdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

#install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes
install -d $RPM_BUILD_ROOT%{_datadir}/themes/%{name}
for i in `ls -1 $RPM_BUILD_ROOT%{_datadir}/themes/|grep -v metacity`
do
	install -d $RPM_BUILD_ROOT%{_datadir}/themes/%{name}/$i
	cp -fpr $RPM_BUILD_ROOT%{_datadir}/themes/$i/metacity-1/* $RPM_BUILD_ROOT%{_datadir}/themes/%{name}/$i/
	rm -rf $RPM_BUILD_ROOT%{_datadir}/themes/$i
	#ln -s %{_datadir}/themes/$i/metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/%{name}/$i
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/metacity-dialog
%{_datadir}/%{name}
%{_wmpropsdir}/metacity.desktop
%{_sysconfdir}/gconf/schemas/*
%{_pixmapsdir}/*

%files themes-AgingGorilla
%defattr(644,root,root,755)
%{_datadir}/themes/metacity/AgingGorilla/*

%files themes-Atlanta
%defattr(644,root,root,755)
%{_datadir}/themes/metacity/Atlanta/*

%files themes-Bright
%defattr(644,root,root,755)
%{_datadir}/themes/metacity/Bright/*

%files themes-Crux
%defattr(644,root,root,755)
%{_datadir}/themes/metacity/Crux/*

%files themes-Esco
%defattr(644,root,root,755)
%{_datadir}/themes/metacity/Esco/*

%files themes-Metabox
%defattr(644,root,root,755)
%{_datadir}/themes/metacity/Metabox/*

%files themes-Simple
%defattr(644,root,root,755)
%{_datadir}/themes/metacity/Simple/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
