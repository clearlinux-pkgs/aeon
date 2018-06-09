#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aeon
Version  : 0.2.7
Release  : 8
URL      : https://github.com/NervanaSystems/aeon/archive/v0.2.7.tar.gz
Source0  : https://github.com/NervanaSystems/aeon/archive/v0.2.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: aeon-python3
Requires: aeon-python
Requires: numpy
BuildRequires : curl-dev
BuildRequires : llvm
BuildRequires : numpy
BuildRequires : opencv-dev
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : sox-dev
Patch1: build.patch

%description
# Getting Started
## Installation
First grab aeon's dependencies:
### Ubuntu:
sudo apt-get install libcurl4-openssl-dev clang libopencv-dev libsox-dev

%package python
Summary: python components for the aeon package.
Group: Default
Requires: aeon-python3

%description python
python components for the aeon package.


%package python3
Summary: python3 components for the aeon package.
Group: Default
Requires: python3-core

%description python3
python3 components for the aeon package.


%prep
%setup -q -n aeon-0.2.7
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528566761
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
