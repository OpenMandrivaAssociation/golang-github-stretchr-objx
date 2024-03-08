%bcond_with bootstrap2

# Run tests in check section
%bcond_without check

# https://github.com/stretchr/objx
%global goipath		github.com/stretchr/objx
%global forgeurl	https://github.com/stretchr/objx
Version:		0.5.1

%gometa

Summary:	Go package for dealing with maps, slices, JSON and other data
Name:		golang-github-stretchr-objx

Release:	1
Source0:	https://github.com/stretchr/objx/archive/v%{version}/objx-%{version}.tar.gz
%if %{with bootstrap2}
# Generated from Source100
Source3:	vendor.tar.zst
Source100:	golang-package-dependencies.sh
%endif
URL:		https://github.com/stretchr/objx
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
%if ! %{with bootstrap2}
BuildRequires:	golang(github.com/stretchr/testify/assert)
%endif
BuildArch:	noarch

%description
A Go package for dealing with maps, slices, JSON and other data.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n objx-%{version}

rm -rf vendor

%if %{with bootstrap2}
tar xf %{S:3}
%endif

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

