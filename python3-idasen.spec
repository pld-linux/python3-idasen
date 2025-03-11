# Conditional build:
%define		module	idasen
Summary:	Python API and CLI for the ikea IDÅSEN standing desk
Name:		python3-%{module}
Version:	0.7.1
Release:	7
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/idasen/%{module}-%{version}.tar.gz
# Source0-md5:	74b7e39d6b1e1c2e05223bccf77955dc
URL:		https://github.com/newAM/idasen
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python API and CLI for the ikea IDÅSEN standing desk.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/%{module}
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
