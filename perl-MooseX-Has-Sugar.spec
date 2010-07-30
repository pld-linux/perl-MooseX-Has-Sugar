#
# TODO:	- pl
#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MooseX
%define		pnam	Has-Sugar
Summary:	MooseX::Has-Sugar - Sugar Syntax for moose 'has' fields
Name:		perl-MooseX-Has-Sugar
Version:	0.05044303
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/K/KE/KENTNL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3504c457cee4a337fbded2af327b9f9b
URL:		http://search.cpan.org/dist/MooseX-Has-Sugar/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Find-Lib
BuildRequires:	perl-MooseX-Types
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-use-ok
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
	--prefix="%{_prefix}" \
	--installdirs="vendor"

%{__perl} Build

%{?with_tests:%{__perl} Build test}

%install
rm -rf $RPM_BUILD_ROOT

%{__perl} Build install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_mandir}/man3/*
%dir %{perl_vendorlib}/MooseX/Has
%{perl_vendorlib}/MooseX/Has/Sugar.pm
%dir %{perl_vendorlib}/MooseX/Has/Sugar
%{perl_vendorlib}/MooseX/Has/Sugar/Minimal.pm
%{perl_vendorlib}/MooseX/Has/Sugar/Saccharin.pm
