# https://github.com/kurin/blazer
%global goipath github.com/kurin/blazer


%global common_description %{expand:
Blazer is a Golang client library for Backblaze's B2 object storage service. It is designed for simple integration with existing applications that may already be using S3 and Google Cloud Storage, by exporting only a few standard Go types.

It implements and satisfies the B2 integration checklist, automatically handling error recovery, reauthentication, and other low-level aspects, making it suitable to upload very large files, or over multi-day time scales.}

%gometa -i

Name:           %{goname}
Version:        0.4.4
Release:        1%{?dist}
Summary:        A Go library for Backblaze's B2. 
License:        ASL 2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
%{summary}

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
%doc CONTRIBUTING.md README.md

%changelog
* Thu Jun 14 2018 Steve Miller (copart) <code@rellims.com> <copart@gmail.com> - 0.4.4-1
- First package for Fedora
