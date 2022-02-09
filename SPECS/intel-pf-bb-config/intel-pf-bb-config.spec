Name:          intel-pf-bb-config
Version:       21.11
Release:       1%{?dist}
Summary:       A tool for configuring certain Intel baseband devices
Group:         System/Tools
Vendor:        Microsoft
Distribution:  Mariner
License:       Apache 2.0
URL:           https://github.com/intel/pf-bb-config
Source0:       https://github.com/benhoyt/inih/archive/r44.tar.gz
Source1:       https://github.com/intel/pf-bb-config/archive/v%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

%description
This application provides a means to configure certain Intel baseband devices by
accessing their configuration space and setting parameters via MMIO.

%prep
%setup -n inih-r44
%setup -T -D -b 1 -n pf-bb-config-21.11

%build
# Build the INI parser library
pushd ../inih-r44/extra
make -f Makefile.static
cp libinih.a ..
popd

cd ..
export INIH_PATH=$PWD/inih-r44

# Build the baseband tool
pushd pf-bb-config-21.11
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 pf_bb_config %{buildroot}%{_bindir}/pf_bb_config

%files
%license LICENSE
%{_bindir}/pf_bb_config

%changelog
* Wed Dec 22 2021 Xenofon Foukas <xefouk@microsoft.com> - 21.11-1
- Moved tool to latest version
* Tue Mar 16 2021 Hernan Gatta <hegatta@microsoft.com> - 21.3-1
- Initial SPEC for ECF Mariner.
