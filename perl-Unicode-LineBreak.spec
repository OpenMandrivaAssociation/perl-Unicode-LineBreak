%define	modname	Unicode-LineBreak
%define	modver	2012.10

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Unicode::LineBreak::Constants\\)'
%endif

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1
Summary:	UAX #14 Unicode Line Breaking Algorithm
License:	GPL+ or Artistic
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
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
