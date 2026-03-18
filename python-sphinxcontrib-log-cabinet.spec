%define module sphinxcontrib-log-cabinet
%define oname sphinxcontrib_log_cabinet

Name:		python-sphinxcontrib-log-cabinet
Version:	1.0.1
Release:	1
Summary:	Organize changelog directives in Sphinx docs
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/davidism/sphinxcontrib-log-cabinet
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)

%description
Organize changelog directives in Sphinx docs.

%prep -a
# Remove bundled egg-info
rm -rf src/%{oname}.egg-info

%files
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/sphinxcontrib
%{python_sitelib}/%{oname}-%{version}-py%{pyver}.egg-info
%{python_sitelib}/%{oname}-%{version}-py%{pyver}-nspkg.pth
