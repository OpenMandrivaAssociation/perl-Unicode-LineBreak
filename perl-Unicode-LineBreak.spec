%define	modname	Unicode-LineBreak
%define modver 2019.001
%ifarch %{x86_64}
# FIXME workaround for debuginfo bug
%global _debugsource_template %{nil}
%endif

%define __requires_exclude perl\\(Unicode::LineBreak::Constants\\)

Summary:	UAX #14 Unicode Line Breaking Algorithm
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Unicode::LineBreak
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{modname}-%{modver}.tar.gz
BuildRequires:	perl(Encode)
BuildRequires:	perl(MIME::Charset)
BuildRequires:	perl(Test)
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
%{perl_vendorarch}/*
%{_mandir}/man3/*
