# https://github.com/restic/chunker
%global goipath github.com/restic/chunker
Version:        0.2.0

%global common_description %{expand:
The package chunker implements content-defined-chunking (CDC) based on a 
rolling Rabin Hash. The library is part of the restic backup program.}

%gometa -i

Name:       %{goname}
Release:    1%{?dist}
Summary:    Implementation of Content Defined Chunking (CDC) in Go
License:    BSD
URL:        %{gourl}
Source0:    https://%{goipath}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz



%description
%{common_description}

%package devel
Summary:       %{summary}
BuildArch:     noarch


%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q


%install
%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Thu Jun 14 2018 Steve Miller (copart) <code@rellims.com> - 0.2.0-1
- First package for Fedora

