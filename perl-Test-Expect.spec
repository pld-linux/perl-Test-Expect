#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Expect
Summary:	Test::Expect - Automated driving and testing of terminal-based programs
#Summary(pl.UTF-8):	
Name:		perl-Test-Expect
Version:	0.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b22cb4575d910bb2d36e506a958da300
URL:		http://search.cpan.org/dist/Test-Expect/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Expect-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Expect is a module for automated driving and testing of
terminal-based programs.  It is handy for testing interactive programs
which have a prompt, and is based on the same concepts as the Tcl
Expect tool.  As in Expect::Simple, the Expect object is made
available for tweaking.

Test::Expect is intended for use in a test script.

# %description -l pl.UTF-8
# TODO

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
%doc CHANGES README
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
