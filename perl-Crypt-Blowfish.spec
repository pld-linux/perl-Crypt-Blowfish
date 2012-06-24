%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Blowfish
Summary:	Crypt::Blowfish Perl module
Summary(cs):	Modul Crypt::Blowfish pro Perl
Summary(da):	Perlmodul Crypt::Blowfish
Summary(de):	Crypt::Blowfish Perl Modul
Summary(es):	M�dulo de Perl Crypt::Blowfish
Summary(fr):	Module Perl Crypt::Blowfish
Summary(it):	Modulo di Perl Crypt::Blowfish
Summary(ja):	Crypt::Blowfish Perl �⥸�塼��
Summary(ko):	Crypt::Blowfish �� ����
Summary(nb):	Perlmodul Crypt::Blowfish
Summary(pl):	Modu� Perla Crypt::Blowfish
Summary(pt):	M�dulo de Perl Crypt::Blowfish
Summary(pt_BR):	M�dulo Perl Crypt::Blowfish
Summary(ru):	������ ��� Perl Crypt::Blowfish
Summary(sv):	Crypt::Blowfish Perlmodul
Summary(uk):	������ ��� Perl Crypt::Blowfish
Summary(zh_CN):	Crypt::Blowfish Perl ģ��
Name:		perl-Crypt-Blowfish
Version:	2.09
Release:	4
License:	BSD-like (see COPYRIGHT)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bbd037e1eb20778f3d636dff345ed02f
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Blowfish perl module - an implementation of the Blowfish
cryptography algorithm.

%description -l pl
Modu� perla Crypt::Blowfish - implementacja algorytmu
kryptograficznego Blowfish.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes COPYRIGHT README
%{perl_vendorarch}/Crypt/Blowfish.pm
%dir %{perl_vendorarch}/auto/Crypt/Blowfish
%{perl_vendorarch}/auto/Crypt/Blowfish/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Blowfish/*.so
%{_mandir}/man3/*
