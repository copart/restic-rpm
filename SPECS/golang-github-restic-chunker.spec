# https://github.com/restic/chunker
%global goipath github.com/restic/chunker
Version:        0.2.0

%global common_description %{expand:
The Minio Go Client SDK provides simple APIs to access any Amazon S3 compatible
object storage.

This quickstart guide will show you how to install the Minio client SDK, 
connect to Minio, and provide a walkthrough for a simple file uploader. 
For a complete list of APIs and examples, please take a look at the Go 
Client API Reference.}

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

