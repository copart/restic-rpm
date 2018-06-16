# https://github.com/minio/minio-go
%global goipath         github.com/minio/minio-go

%global common_description %{expand:
The Minio Go Client SDK provides simple APIs to access any Amazon S3 compatible
object storage.

This quickstart guide will show you how to install the Minio client SDK, 
connect to Minio, and provide a walkthrough for a simple file uploader. 
For a complete list of APIs and examples, please take a look at the Go 
Client API Reference.}

%gometa -i

Name:		%{goname}
Version:	6.0.2
Release:	1%{?dist}
Summary:	Minio Client SDK for Go
License:	ASL 2.0
URL:		%{gourl}
Source0:	https://%{goipath}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#patch0 reverts minio to use former name of httpguts lib, 
# keep until dependancy is upgraded
Patch0:		minio-undo981.patch

%description
%{common_description}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/go-ini/ini)
BuildRequires: golang(github.com/mitchellh/go-homedir)
BuildRequires: golang(golang.org/x/crypto/argon2)
BuildRequires: golang(golang.org/x/net/lex/httplex)
#BuildRequires: golang(golang.org/x/net/http/httpguts)

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup
%patch0 -p1

%install
%goinstall

%check
#tests are disabled since they require Internet access

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README_zh_CN.md CONTRIBUTING.md MAINTAINERS.md README.md

%changelog
* Thu Jun 14 2018 Steve Miller (copart) <code@rellims.com> - 6.0.2-1
- First package for Fedora
