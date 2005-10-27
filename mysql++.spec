Summary:	C++ interface to MySQL Database
Summary(pl):	Interfejs C++ do bazy MySQL
Name:		mysql++
Version:	1.7.26
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://tangentsoft.net/mysql++/releases/%{name}-%{version}.tar.gz
# Source0-md5:	2e425b1a334523723aadd86c9a3185bc
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-libpath.patch
URL:		http://tangentsoft.net/mysql++/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mysql++ is a C++ interface to MySQL API.

%description -l pl
Mysql++ jest interfejsem C++ do API MySQL.

%package devel
Summary:	C++ interface to MySQL Database (headers)
Summary(pl):	Interfejs C++ do bazy MySQL (pliki nag³ówkowe)
Group:		Development/Libraries
Requires:	libstdc++-devel
Requires:	mysql-devel
Requires:	%{name} = %{version}-%{release}

%description devel
Mysql++ is a C++ interface to MySQL API. Package contains the
development header files necessary to develop MySQL client
applications using Mysql++.

%description devel -l pl
Mysql++ jest interfejsem C++ do API MySQL. Paczka zawiera nag³ówki
potrzebne do rozwoju aplikacji klienckich u¿ywaj±cych Mysql++.

%package static
Summary:	C++ interface to MySQL Database (static libraries)
Summary(pl):	Interfejs C++ do bazy MySQL (biblioteki statyczne)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Mysql++ is a C++ interface to MySQL API. Package contains the static
libraries.

%description static -l pl
Mysql++ jest interfejsem C++ do API MySQL. Paczka zawiera biblioteki
statyczne.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-mysql-lib=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
