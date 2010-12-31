%define upstream_name    Unicode-LineBreak
%define upstream_version 1.010

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
Summary:    UAX #14 Unicode Line Breaking Algorithm
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Unicode/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl(MIME::Charset)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Text::LineFold folds or unfolds lines of plain text. As it mainly focuses
on plain text e-mail messages, RFC 3676 flowed format is also supported.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
cd linebreak-c
autoreconf -fi

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


