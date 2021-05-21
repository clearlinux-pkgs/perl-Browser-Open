#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Browser-Open
Version  : 0.04
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/Browser-Open-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/Browser-Open-0.04.tar.gz
Summary  : open a browser in a given URL
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Browser-Open-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Browser-Open, version
0.03:
open a browser in a given URL

%package dev
Summary: dev components for the perl-Browser-Open package.
Group: Development
Provides: perl-Browser-Open-devel = %{version}-%{release}
Requires: perl-Browser-Open = %{version}-%{release}

%description dev
dev components for the perl-Browser-Open package.


%package perl
Summary: perl components for the perl-Browser-Open package.
Group: Default
Requires: perl-Browser-Open = %{version}-%{release}

%description perl
perl components for the perl-Browser-Open package.


%prep
%setup -q -n Browser-Open-0.04
cd %{_builddir}/Browser-Open-0.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Browser::Open.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Browser/Open.pm
