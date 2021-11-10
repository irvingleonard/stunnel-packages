%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:		stunnel
Version:	5.60
Release:	1%{?dist}
Summary:	TLS enabling proxy

License:	GNU GPL version 2 with OpenSSL exception
URL:		https://www.stunnel.org/index.html
Source0:	https://www.stunnel.org/downloads/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
BuildRequires:  tcp_wrappers-devel

%description
Stunnel is a proxy designed to add TLS encryption functionality to existing clients and servers without any changes in the programs' code.

%prep
%setup

%build
./configure
make

%install
make install DESTDIR=%{buildroot}
%{__gzip} --name --best %{buildroot}/usr/local/share/man/man8/stunnel.8
%{__gzip} --name --best %{buildroot}/usr/local/share/man/man8/stunnel.pl.8
 
%files
/usr/local/bin/stunnel*
/usr/local/etc/stunnel
/usr/local/lib/stunnel
/usr/local/share/doc/stunnel
%doc /usr/local/share/man/man8/stunnel*

%changelog
* Wed Nov 10 2021 Irving Leonard <irvingleonard@github.com> 5.60-1
- Upgraded to version 5.60
* Mon Mar 8 2021 Irving Leonard <mm-irvingleonard@github.com> 5.58-1
- Upgraded to version 5.58
* Thu Oct 15 2020 Irving Leonard <mm-irvingleonard@github.com> 5.57-1
- Initial RPM release
