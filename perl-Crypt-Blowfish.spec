%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Blowfish
Summary:	Crypt::Blowfish Perl module
Summary(cs):	Modul Crypt::Blowfish pro Perl
Summary(da):	Perlmodul Crypt::Blowfish
Summary(de):	Crypt::Blowfish Perl Modul
Summary(es):	Módulo de Perl Crypt::Blowfish
Summary(fr):	Module Perl Crypt::Blowfish
Summary(it):	Modulo di Perl Crypt::Blowfish
Summary(ja):	Crypt::Blowfish Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Crypt::Blowfish ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Crypt::Blowfish
Summary(pl):	Modu³ Perla Crypt::Blowfish
Summary(pt):	Módulo de Perl Crypt::Blowfish
Summary(pt_BR):	Módulo Perl Crypt::Blowfish
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Crypt::Blowfish
Summary(sv):	Crypt::Blowfish Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Crypt::Blowfish
Summary(zh_CN):	Crypt::Blowfish Perl Ä£¿é
Name:		perl-Crypt-Blowfish
Version:	2.09
Release:	3
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
