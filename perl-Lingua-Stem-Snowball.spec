%define upstream_name    Lingua-Stem-Snowball
%define upstream_version 0.952

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

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




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.952.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.952.0-2mdv2011.0
+ Revision: 555995
- rebuild for perl 5.12

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.952.0-1mdv2010.1
+ Revision: 471172
- import perl-Lingua-Stem-Snowball


* Sun Nov 29 2009 cpan2dist 0.952-1mdv
- initial mdv release, generated with cpan2dist
