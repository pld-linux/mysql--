Summary:	C++ interface to MySQL Database
Summary(pl):	Interfejs C++ do bazy MySQL
Name:		mysql++
Version:	1.7.9
Release:	5
License:	LGPL
Group:		Libraries
Source0:	ftp://sunsite.icm.edu.pl/pub/unix/mysql/Downloads/mysql++/%{name}-%{version}.tar.gz
# Source0-md5:	1312fb4e33dcce07fac5fa9c2ac801f7
Patch0:		ftp://sunsite.icm.edu.pl/pub/unix/mysql/Downloads/mysql++/mysql++-gcc-3.0.patch.gz
Patch1:		ftp://sunsite.icm.edu.pl/pub/unix/mysql/Downloads/mysql++/mysql++-gcc-3.2.patch.gz
Patch2:		ftp://sunsite.icm.edu.pl/pub/unix/mysql/Downloads/mysql++/mysql++-gcc-3.2.2.patch.gz
# fixed from ftp://sunsite.icm.edu.pl/pub/unix/mysql/Downloads/mysql++/mysqlplus-gcc-3.4.patch.gz
Patch3:		%{name}-gcc-3.4.patch
Patch4:		%{name}-examples-gcc3.patch
Patch5:		%{name}-nolibs.patch
Patch6:		%{name}-libpath.patch
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

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
%doc README doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
