%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Blowfish
Summary:	Crypt::Blowfish perl module
Summary(pl):	Modu³ perla Crypt::Blowfish
Name:		perl-Crypt-Blowfish
Version:	2.09
Release:	2
License:	BSD-like (see COPYRIGHT)
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Blowfish perl module - an implementation of the Blowfish
cryptography algorithm.

%description -l pl
Modu³ perla Crypt::Blowfish - implementacja algorytmu
kryptograficznego Blowfish.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes COPYRIGHT README
%{perl_sitearch}/Crypt/Blowfish.pm
%dir %{perl_sitearch}/auto/Crypt/Blowfish
%{perl_sitearch}/auto/Crypt/Blowfish/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/Blowfish/*.so
%{_mandir}/man3/*
