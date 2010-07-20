%define upstream_name    Lingua-Stem-Snowball
%define upstream_version 0.952

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perl interface to Snowball stemmers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::ParseXS)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Stemming reduces related words to a common root form -- for instance,
"horse", "horses", and "horsing" all become "hors". Most commonly, stemming
is deployed as part of a search application, allowing searches for a given
term to match documents which contain other forms of that term.

This module is very similar to the Lingua::Stem manpage -- however,
Lingua::Stem is pure Perl, while Lingua::Stem::Snowball is an XS module
which provides a Perl interface to the C version of the Snowball stemmers.
(the http://snowball.tartarus.org manpage).

Supported Languages
    The following stemmers are available (as of Lingua::Stem::Snowball
    0.95):

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


