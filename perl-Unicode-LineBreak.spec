%define	modname	Unicode-LineBreak

%define __requires_exclude perl\\(Unicode::LineBreak::Constants\\)

Summary:	UAX #14 Unicode Line Breaking Algorithm
Name:		perl-%{modname}
Version:	2019.001
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Unicode::LineBreak
Source0:	https://www.cpan.org/modules/by-module/Unicode/%{modname}-%{version}.tar.gz
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(MIME::Charset)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(sombok)
# Ease version scheme switching without an Epoch
Obsoletes:	%{name} = 2019.1.0-2

%description
Text::LineFold folds or unfolds lines of plain text. As it mainly focuses
on plain text e-mail messages, RFC 3676 flowed format is also supported.

%prep
%autosetup -n %{modname}-%{version}
# remove bundled library
rm -rf sombok
sed -i -e '/^sombok/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
%make_install

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*

