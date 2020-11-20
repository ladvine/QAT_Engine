# SPDX-License-Identifier: MIT

%global githubname QAT_Engine
%global soversion 0
%global enginesdir %(pkg-config --variable=enginesdir libcrypto)

Name:           qatengine
Version:        0.6.2
Release:        1%{?dist}
Summary:        Intel QuickAssist Technology (QAT) OpenSSL Engine
License:        BSD
URL:            https://github.com/intel/%{githubname}
Source0:        https://github.com/intel/%{githubname}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc make pkg-config
BuildRequires:  autoconf automake libtool
BuildRequires:  openssl-devel >= 1.1.1
BuildRequires:  qatlib-devel >= 20.10.0
# Exclude arm, aarch64, power64 and s390x due to broken build
ExcludeArch:    %{arm} aarch64 %{power64} s390x

%description
This package provides the Intel QuickAssist Technology OpenSSL Engine
(an OpenSSL Plug-In Engine) which provides cryptographic acceleration
for both hardware and optimized software using Intel QuickAssist Technology
enabled Intel platforms.

%prep
%autosetup -n %{githubname}-%{version}

%build
autoreconf -ivf
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libqatengine.so.%{soversion}*
%{enginesdir}/qatengine.so
%exclude %{_libdir}/libqatengine.la
%exclude %{_libdir}/libqatengine.so

%changelog
* Wed Nov 18 2020 Dinesh Balakrishnan <dineshx.balakrishnan@intel.com> 0.6.2-1
- Update to qatengine v0.6.2
- Address review comments
* Tue Sep 08 2020 Dinesh Balakrishnan <dineshx.balakrishnan@intel.com> 0.6.1-1
- Initial version of rpm package
