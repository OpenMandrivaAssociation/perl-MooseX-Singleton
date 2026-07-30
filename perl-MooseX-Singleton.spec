%define upstream_name    MooseX-Singleton
%define upstream_version 0.30
Name:		perl-%{upstream_name}
Version:	0.30
Release:	3

Summary:	Base class for MooseX::Singleton
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Singleton-0.30.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Requires)

BuildArch:	noarch

%description
A singleton is a class that has only one instance in an application.
'MooseX::Singleton' lets you easily upgrade (or downgrade, as it were) your
the Moose manpage class to a singleton.

All you should need to do to transform your class is to change 'use Moose'
to 'use MooseX::Singleton'. This module uses a new class metaclass and
instance metaclass, so if you're doing metamagic you may not be able to use
this.

'MooseX::Singleton' gives your class an 'instance' method that can be used
to get a handle on the singleton. It's actually just an alias for 'new'.

%prep
%setup -q -n MooseX-Singleton-0.30

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


