%define upstream_name    MooseX-Singleton
%define upstream_version 0.29

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Base class for MooseX::Singleton
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.250.0-2mdv2011.0
+ Revision: 653604
- rebuild for updated spec-helper

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2011.0
+ Revision: 573857
- adding missing buildrequires:
- update to 0.25

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 553966
- update to 0.24

* Mon Dec 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.1
+ Revision: 483041
- update to 0.22

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 442944
- update to 0.21

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.0
+ Revision: 394971
- forgot to commit new tarball
- update to 0.19

* Thu Jun 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.0
+ Revision: 389123
- update to 0.18

* Sat Jun 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 383359
- adding missing buildrequires
- import perl-MooseX-Singleton


* Sat Jun 06 2009 cpan2dist 0.17-1mdv
- initial mdv release, generated with cpan2dist

