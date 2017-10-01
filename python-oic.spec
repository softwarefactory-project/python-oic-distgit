%global        srcname pyoidc
%global        uname oic
%global        sum A complete OpenID Connect implementation in Python

Name:          python-%{uname}
Version:       0.9.4
Release:       6%{?dist}
Summary:       %{sum}

URL:           https://github.com/OpenIDC/pyoidc
Source:        https://github.com/OpenIDC/pyoidc/archive/v%{version}.tar.gz
License:       Apache 2.0

BuildArch:      noarch

Buildrequires: python2-devel
BuildRequires: python-setuptools
Buildrequires: python-httpretty
BuildRequires: python2-testfixtures
BuildRequires: python-mock
BuildRequires: python2-jwkest
BuildRequires: pytest
BuildRequires: python2-cryptodomex
BuildRequires: python-future
BuildRequires: python-mako
BuildRequires: python2-responses

%description
%{sum}.

%package -n python2-%{uname}
Summary:        %{sum}

Requires: python-requests
Requires: python2-cryptography
Requires: python-cffi
Requires: python2-jwkest
Requires: python-mako
Requires: python-beaker
Requires: python2-sphinx-theme-alabaster
Requires: pyOpenSSL
Requires: python2-cryptodomex

%description -n python2-%{uname}
%{sum}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
PYTHONPATH=build/lib py.test tests/ -m "not network"

%files -n python2-%{uname}
%{python2_sitelib}/*

%changelog
* Sun Oct 01 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.9.4-6
- Use python2-sphinx-theme-alabaster instead of alabaster

* Wed Apr 19 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.9.4-5
- use python-future instead of python2-future

* Fri Mar 10 2017 Tristan Cacqueray <tdecacqu@redhat.com> 0.9.4.0-4
- use python-cffi instead of python2-cffi to avoid conflict

* Mon Mar 7 2017 Nicolas Hicher <nhicher@redhat.com> 0.9.4.0-3
- move Requires on python2 package instead source

* Thu Mar 2 2017 Nicolas Hicher <nhicher@redhat.com> 0.9.4.0-2
- normalize spec file

* Mon Feb 27 2017 Nicolas Hicher <nhicher@redhat.com> 0.9.4.0-1
- initial package
