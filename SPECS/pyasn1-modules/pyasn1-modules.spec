Summary:        A collection of ASN.1-based protocols modules.
Name:           pyasn1-modules
Version:        0.2.8
Release:        1%{?dist}
License:        BSD
Group:          Development/Languages/Python
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://pypi.python.org/pypi/pyasn1-modules
Source0:        https://github.com/etingof/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is a small but growing collection of ASN.1 data structures expressed in Python terms using pyasn1 data model.

%package -n     python3-%{name}
Summary:        A collection of ASN.1-based protocols modules.
BuildRequires:  python3-devel
%if %{with_check}
BuildRequires:  python3-pyasn1
%endif
Requires:       python3
Requires:       python3-pyasn1

%description -n python3-pyasn1-modules
This is a small but growing collection of ASN.1 data structures expressed in Python terms using pyasn1 data model.
It's thought to be useful to protocol developers and testers.
All modules are py2k/py3k-compliant.

%prep
%autosetup
%py3_shebang_fix .

%build
%py3_build

%install
%py3_install

%check
pushd tools
for file in ../test/*.sh; do
    [ -f "$file" ] && chmod +x "$file" && PYTHONPATH=%{buildroot}%{python3_sitelib} "$file"
done
popd

%files -n python3-pyasn1-modules
%defattr(-,root,root,-)
%license LICENSE.txt
%{python3_sitelib}/*

%changelog
* Fri Jan 04 2022 Thomas Crain <thcrain@microsoft.com> - 0.2.8-1
- Upgrade to latest upstream version
- Use github release tarball instead of pypi source

* Wed Oct 20 2021 Thomas Crain <thcrain@microsoft.com> - 0.2.2-6
- Add license to python3 package
- Remove python2 package
- Lint spec

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 0.2.2-5
- Added %%license line automatically

* Wed Apr 29 2020 Emre Girgin <mrgirgin@microsoft.com> - 0.2.2-4
- Renaming python-pyasn1-modules to pyasn1-modules

* Wed Apr 08 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 0.2.2-3
- Fixed "Source0" tag.
- License verified.

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> - 0.2.2-2
- Initial CBL-Mariner import from Photon (license: Apache2).

* Sun Sep 09 2018 Tapas Kundu <tkundu@vmware.com> - 0.2.2-1
- Update to version 0.2.2

* Mon Aug 14 2017 Xiaolin Li <xiaolinl@vmware.com> - 0.0.8-2
- Fixed make check.

* Mon Mar 13 2017 Xiaolin Li <xiaolinl@vmware.com> - 0.0.8-1
- Initial packaging for Photon
