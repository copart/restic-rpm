# https://github.com/pkg/xattr
%global goipath github.com/pkg/xattr
Version:        0.3.0

%gometa -i

Name:           %{goname}
Release:        1%{?dist}
Summary:        Extended attribute support library for Go
License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz


%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/sys/unix)

%description devel
%{summary}

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
* Thu Jun 14 2018 Steve Miller (copart) <code@rellims.com> - 0.3.0-1
- First package for Fedora

