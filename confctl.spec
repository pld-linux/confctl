Summary:	easy access to configuration files
Summary(pl.UTF-8):	łatwy dostęp do plików konfiguracyjnych
Name:		confctl
Version:	1.2
Release:	0.1
License:	BSD
Group:		Applications
Source0:	https://github.com/trasz/confctl/archive/%{version}.tar.gz
# Source0-md5:	b2abc044d2c1feaffea98406d10cae6f
URL:		https://github.com/trasz/confctl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Confctl is a tool designed for easy access to configuration files in
C-like syntax from shell scripts

%description -l pl.UTF-8
Confctl to narzędzie zaprojektowane do łatwego dostępu do plików
konfiguracyjnych z poziomu skryptów shella.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/confctl.1*
