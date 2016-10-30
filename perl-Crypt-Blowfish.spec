#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Blowfish
Summary:	Crypt::Blowfish - Perl Blowfish encryption module
Summary(pl.UTF-8):	Crypt::Blowfish - moduł Perla dla szyfrowania Blowfish
Name:		perl-Crypt-Blowfish
Version:	2.12
Release:	8
License:	BSD-like (see COPYRIGHT)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a0eca17addc8bdaf38c044c365a8800c
Patch0:		build.patch
URL:		http://search.cpan.org/dist/Crypt-Blowfish/
%{?with_tests:BuildRequires:	perl-Crypt-CBC >= 1.22}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Blowfish Perl module contains an implementation of the Blowfish
cryptography algorithm.

%description -l pl.UTF-8
Moduł Perla Crypt::Blowfish zawiera implementację algorytmu
kryptograficznego Blowfish.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Blowfish/Blowfish.so
%{_mandir}/man3/Crypt::Blowfish.3pm*
