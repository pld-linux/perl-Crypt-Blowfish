#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Blowfish
Summary:	Crypt::Blowfish - Perl Blowfish encryption module
Summary(pl):	Crypt::Blowfish - modu� Perla dla szyfrowania Blowfish
Name:		perl-Crypt-Blowfish
Version:	2.09
Release:	6
License:	BSD-like (see COPYRIGHT)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bbd037e1eb20778f3d636dff345ed02f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Blowfish Perl module contains an implementation of the Blowfish
cryptography algorithm.

%description -l pl
Modu� Perla Crypt::Blowfish zawiera implementacj� algorytmu
kryptograficznego Blowfish.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
