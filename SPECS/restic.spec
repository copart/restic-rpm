Name:    restic
Version: 0.8.2
Release: 1%{?dist}
Summary: Backup program
URL:     https://restic.net
License: BSD

BuildRequires: golang
Source0: https://github.com/restic/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%define debug_package %{nil}

%description
restic is a backup program that is fast, efficient and secure.

%prep
%autosetup

%build
#Gzip man pages
/usr/bin/gzip %{_builddir}/%{name}-%{version}/doc/man/*
#build binary
go run build.go

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
mkdir -p %{buildroot}%{_datarootdir}/doc/restic
install -p -m 755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}%{_bindir}
install -p -m 644 %{_builddir}/%{name}-%{version}/doc/man/* %{buildroot}%{_mandir}/man1/
#zsh completion
install -p -m 644 %{_builddir}/%{name}-%{version}/doc/zsh-completion.zsh %{buildroot}%{_datarootdir}/zsh/site-functions/_restic
#Bash completion
install -p -m 644 %{_builddir}/%{name}-%{version}/doc/bash-completion.sh %{buildroot}%{_datarootdir}/bash-completion/completions/restic
#Doc
install -p -m 644 %{_builddir}/%{name}-%{version}/README.rst %{buildroot}%{_datarootdir}/doc/restic/
install -p -m 644 %{_builddir}/%{name}-%{version}/CHANGELOG.md %{buildroot}%{_datarootdir}/doc/restic/

%files
%{_bindir}/%{name}
%{_datarootdir}/zsh/site-functions/_restic
%{_datarootdir}/bash-completion/completions/restic
%doc %{_mandir}/man1/restic*.gz
%doc %{_datarootdir}/doc/restic

%license LICENSE

%changelog
* Tue Feb 20 2018 Steve Miller <copart@gmail.com> - 0.8.2-1
- Bumped restic version
* Fri Jan 12 2018 Steve Miller <copart@gmail.com> - 0.8.1-2
- Added man pages
- Added bash completion
- Added zsh completion
* Sun Jan 07 2018 Steve Miller <copart@gmail.com> - 0.8.1-1
- New Version
* Sat Sep 16 2017 Philipp Baum <phil@phib.io> - 0.7.2-1
- New Version
* Sun Aug 27 2017 Philipp Baum <phil@phib.io> - 0.7.1-1
- New Version
* Wed Mar 15 2017 Philipp Baum <phil@phib.io> - 0.5.0-1
- Initial package build
