Summary:	C++ interface to MySQL Database
Summary(pl):	Interfejs C++ do bazy MySQL
Name:		mysql++
Version:	1.7.9
Release:	2
License:	LGPL
Group:		Development/Libraries
Source0:	ftp://sunsite.icm.edu.pl/pub/unix/mysql/Downloads/mysql++/%{name}-%{version}.tar.gz
# Source0-md5:	1312fb4e33dcce07fac5fa9c2ac801f7
Patch0:		%{name}-gcc3.patch
URL:		http://www.mysql.com/downloads/api-mysql++.html
BuildRequires:	autoconf
BuildRequires:	automake
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
Requires:	%{name} = %{version}

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
Requires:	%{name}-devel = %{version}

%description static
Mysql++ is a C++ interface to MySQL API. Package contains the static
libraries.

%description static -l pl
Mysql++ jest interfejsem C++ do API MySQL. Paczka zawiera biblioteki
statyczne.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README doc/*
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
