# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MooseX
%define		pnam	Has-Sugar
Summary:	MooseX::Has::Sugar - Sugar Syntax for moose 'has' fields
Name:		perl-MooseX-Has-Sugar
Version:	0.05070420
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/K/KE/KENTNL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	566bc8ac848296243d5f09a41c1844d0
URL:		http://search.cpan.org/dist/MooseX-Has-Sugar/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-MooseX-Types
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-namespace-autoclean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sugar Syntax for moose 'has' fields.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/MooseX/Has
%{perl_vendorlib}/MooseX/Has/Sugar.pm
%dir %{perl_vendorlib}/MooseX/Has/Sugar
%{perl_vendorlib}/MooseX/Has/Sugar/Minimal.pm
%{perl_vendorlib}/MooseX/Has/Sugar/Saccharin.pm
%{_mandir}/man3/*
