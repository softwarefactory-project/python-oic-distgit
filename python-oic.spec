%global        uname oic

Name:          python-oic
Version:       0.9.4.0
Release:       1%{?dist}
Summary:       A complete OpenID Connect implementation in Python

URL:           https://github.com/rohe/pyoidc
Source:        https://pypi.io/packages/source/o/%{uname}/%{uname}-%{version}.tar.gz
License:       Apache 2.0

BuildArch:      noarch

Buildrequires:  python-setuptools
Buildrequires:  python2-devel
Requires: python-requests python-cryptography python-cffi
Requires: python-jwkest python-mako python-beaker
Requires: python-alabaster pyOpenSSL

%description
%{summary}.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n %{name}
%{python2_sitelib}/*

%changelog
* Mon Feb 27 2017 Nicolas Hicher <nhicher@redhat.com> 0.9.4.0-1
- initial package
