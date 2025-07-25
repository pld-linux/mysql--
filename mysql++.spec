Summary:	C++ interface to MySQL Database
Summary(pl.UTF-8):	Interfejs C++ do bazy MySQL
Name:		mysql++
Version:	3.2.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	https://tangentsoft.com/mysqlpp/releases/%{name}-%{version}.tar.gz
# Source0-md5:	5ded941ffeeec895022b97e58b1b204b
Patch0:		%{name}-nolibs.patch
URL:		http://tangentsoft.net/mysql++/
BuildRequires:	autoconf
BuildRequires:	bakefile
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mysql++ is a C++ interface to MySQL API.

%description -l pl.UTF-8
Mysql++ jest interfejsem C++ do API MySQL.

%package devel
Summary:	C++ interface to MySQL Database (headers)
Summary(pl.UTF-8):	Interfejs C++ do bazy MySQL (pliki nagłówkowe)
Group:		Development/Libraries
Requires:	libstdc++-devel
Requires:	mysql-devel
Requires:	%{name} = %{version}-%{release}

%description devel
Mysql++ is a C++ interface to MySQL API. Package contains the
development header files necessary to develop MySQL client
applications using Mysql++.

%description devel -l pl.UTF-8
Mysql++ jest interfejsem C++ do API MySQL. Paczka zawiera nagłówki
potrzebne do rozwoju aplikacji klienckich używających Mysql++.

%package static
Summary:	C++ interface to MySQL Database (static libraries)
Summary(pl.UTF-8):	Interfejs C++ do bazy MySQL (biblioteki statyczne)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Mysql++ is a C++ interface to MySQL API. Package contains the static
libraries.

%description static -l pl.UTF-8
Mysql++ jest interfejsem C++ do API MySQL. Paczka zawiera biblioteki
statyczne.

%prep
%setup -q
%patch -P0 -p1

%build
%{__autoconf}
%configure

%{__make} \
	CXXFLAGS="%{rpmcxxflags} -fPIC"

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
%attr(755,root,root) %ghost %{_libdir}/lib*.so.3

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/lib*.a
