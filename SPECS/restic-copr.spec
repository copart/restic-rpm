# https://github.com/restic/restic
%global goipath         github.com/restic/restic
Version:                0.9.2

#The following is here to allow support of building for Copr EPEL until the
#newer Go Macro support is added to RHEL/EPEL
%if 0%{?fedora:1}
%global UseGoMacros 1
%else
%global UseGoMacros 0
#stops rpmbuild from complaining about empty debug files
%global debug_package %{nil}
%global gometa %{nil}
%endif

%gometa

Name:    restic
Release: 1%{?dist}
Summary: Fast, secure, efficient backup program
URL:     %{gourl}
License: BSD
Source0: https://%{goipath}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExcludeArch: ppc64

%if %{UseGoMacros}
BuildRequires: golang(bazil.org/fuse)
BuildRequires: golang(bazil.org/fuse/fs)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/storage)
BuildRequires: golang(github.com/cenkalti/backoff)
BuildRequires: golang(github.com/elithrar/simple-scrypt)
BuildRequires: golang(github.com/juju/ratelimit)
BuildRequires: golang(github.com/kurin/blazer/b2)
BuildRequires: golang(github.com/mattn/go-isatty)
BuildRequires: golang(github.com/minio/minio-go)
BuildRequires: golang(github.com/minio/minio-go/pkg/credentials)
BuildRequires: golang(github.com/ncw/swift)
BuildRequires: golang(github.com/pkg/errors)
BuildRequires: golang(github.com/pkg/sftp)
BuildRequires: golang(github.com/pkg/xattr)
BuildRequires: golang(github.com/restic/chunker)
BuildRequires: golang(golang.org/x/crypto/poly1305)
BuildRequires: golang(golang.org/x/crypto/scrypt)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sync/errgroup)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(golang.org/x/text/encoding/unicode)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/storage/v1)
BuildRequires: golang(gopkg.in/tomb.v2)
#for check/testing
BuildRequires: golang(github.com/google/go-cmp/cmp)
%else
BuildRequires: golang >= 1.9
%endif
#COMMON
#Soft dependency for mounting , ie: fusemount
#Requires: fuse


%description
restic is a backup program that is easy, fast, verifiable, secure, 
efficient and free.

Backup destinations can be:
*Local
*SFTP
*REST Server
*Amazon S3
*Minio Server
*OpenStack Swift
*Backblaze B2
*Microsoft Azure Blob Storage
*Google Cloud Storage
*Other Services via rclone


%prep
%if %{UseGoMacros}
%gosetup -q
%else
%autosetup
%endif

%build 
%if %{UseGoMacros}
%gobuildroot
%gobuild -o _bin/%{name} %{goipath}/cmd/restic
%else
go run build.go --enable-pie
%endif

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
install -p -m 644 doc/man/* %{buildroot}%{_mandir}/man1/
#zsh completion
install -p -m 644 doc/zsh-completion.zsh %{buildroot}%{_datarootdir}/zsh/site-functions/_restic
#Bash completion
install -p -m 644 doc/bash-completion.sh %{buildroot}%{_datarootdir}/bash-completion/completions/restic
%if %{UseGoMacros}
install -p -m 755 _bin/%{name} %{buildroot}%{_bindir}
%else
install -p -m 755 %{name} %{buildroot}%{_bindir}
%endif

%check
#Skip tests using fuse due to root requirement
export RESTIC_TEST_FUSE=0
%if %{UseGoMacros}
%gochecks cmd internal
%endif

%files 
%license LICENSE
%doc GOVERNANCE.md CONTRIBUTING.md CHANGELOG.md README.rst
%{_bindir}/%{name}
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_restic
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/restic
%{_mandir}/man1/restic*.*

%changelog
* Thu Aug 9 2018 Steve Miller <copart@gmail.com> - 0.9.2-1
- Bumped restic version

* Wed Jun 13 2018 Steve Miller <copart@gmail.com> - 0.9.1-2
- Added ppc64 to ExcludeArch, no go for this architecture
- First package for Fedora
- Rework using More Go packaging

* Sun Jun 10 2018 Steve Miller <copart@gmail.com> - 0.9.1-1
- Bumped restic version

* Sun May 27 2018 Steve Miller <copart@gmail.com> - 0.9.0-1
- Bumped restic version

* Sun Mar 04 2018 Steve Miller <copart@gmail.com> - 0.8.3-1
- Bumped restic version

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
