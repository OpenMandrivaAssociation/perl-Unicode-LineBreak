%define	modname	Unicode-LineBreak
%define modver 2014.06

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Unicode::LineBreak::Constants\\)'
%endif

Summary:	UAX #14 Unicode Line Breaking Algorithm
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Encode)
BuildRequires:	perl(MIME::Charset)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Text::LineFold folds or unfolds lines of plain text. As it mainly focuses
on plain text e-mail messages, RFC 3676 flowed format is also supported.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
