%define upstream_name    MooseX-Singleton
%define upstream_version 0.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Base class for MooseX::Singleton
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog
%{_mandir}/man3/*
%perl_vendorlib/*

