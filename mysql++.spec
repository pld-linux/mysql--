Summary:	C++ interface to MySQL Database
Summary(pl):	Interfejs C++ do bazy MySQL
Name:		mysql++
Version:	1.7.9
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	ftp://sunsite.icm.edu.pl/pub/unix/mysql/Downloads/mysql++/%{name}-%{version}.tar.gz
URL:		http://www.mysql.com/downloads/api-mysql++.html
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mysql++ is a C++ interface to MySQL API.
%description -l pl
Mysql++ jest interfejsem C++ do API MySQL.

%package devel
Summary:	C++ interface to MySQL Database (headers and libraries)
Summary(pl):	Interfejs C++ do bazy MySQL (pliki nag³ówkowe i biblioteki)
Group:		Development/Libraries

%description devel
Mysql++ is a C++ interface to MySQL API. Package contains a development header
files and libraries necessary to develop MySQL client applications in C++.

%description devel -l pl
Mysql++ jest interfejsem C++ do API MySQL. Paczka zawiera nag³ówki 
oraz biblioteki potrzebne do rozwoju aplikacji klienckich w jêzyku C++.

%package static
Summary:	C++ interface to MySQL Database (static libraries)
Summary(pl):	Interfejs C++ do bazy MySQL (biblioteki statyczne)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Mysql++ is a C++ interface to MySQL API. Package contains a static libraries.

%description static -l pl
Mysql++ jest interfejsem C++ do API MySQL. Paczka zawiera biblioteki statyczne.

%prep
%setup -q

%build
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so*
%doc README doc/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_libdir}/*.a
