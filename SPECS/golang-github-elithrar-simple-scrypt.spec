# https://github.com/elithrar/simple-scrypt
%global goipath         github.com/elithrar/simple-scrypt


%global common_description %{expand:
simple-scrypt provides a convenience wrapper around Go's existing scrypt package that makes it easier to securely derive strong keys ("hash user passwords"). This library allows you to:

*Generate a scrypt derived key with a crytographically secure salt and sane default parameters for N, r and p.
*Upgrade the parameters used to generate keys as hardware improves by storing them with the derived key (the scrypt spec. doesn't allow for this by default).
*Provide your own parameters (if you wish to).

The API closely mirrors Go's bcrypt library in an effort to make it easy to migrate—and because it's an easy to grok API.}

%gometa -i

Name:           %{goname}
Version:        1.3.0
Release: 		1%{?dist}
Summary:        A convenience library for generating, comparing and inspecting password hashes using the scrypt KDF in Go. 
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
%{common_description}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/crypto/scrypt)

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
* Wed Jun 13 2018 Steve Miller (copart) <code@rellims.com> - 1.3.0-1
- First package for Fedora
