%global short_name java

Summary:  SIMP ActiveMQ Puppet Module
Name: pupmod-puppetlabs-java
Version: 1.2.0
Release: 0
License: Apache
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch
Requires: puppet >= 3.4

Prefix: /etc/puppet/environments/simp/modules/%{short_name}

%description
A module to install and configure Java.

%prep
%setup -q

%build

%install

[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}

dirs='manifests'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}
done

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(0640,root,puppet,0750)
%{prefix}

%post
# Post installation stuff

%postun
# Post uninstall stuff

%changelog
* Wed May 21 2014 Nick Markowski <nmarkowski@keywcorp.com> - 1.2.0-0
- Pulled from puppetlabs - https://github.com/puppetlabs/puppetlabs-java
