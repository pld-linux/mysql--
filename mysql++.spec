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
Mysql++ is a C++ interface to MySQL API. Package contains a development header
files and libraries necessary to develop MySQL client applications in C++.

%description -l pl
Mysql++ jest interfejsem C++ do API MySQL. Paczka zawiera nag³ówki 
oraz biblioteki potrzebne do rozwoju aplikacji klienckich w jêzyku C++.

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

%files
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*
%doc README doc/*
