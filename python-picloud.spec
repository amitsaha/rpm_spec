Name:           python-picloud
Version:        2.5.6
Release:        1%{?dist}
Summary:        PiCloud client-side Library
Group:          Development/Languages
#All files within the PiCloud cloud client package distribution are subject to the 
#GNU Lesser General Public License v 2.1,described within COPYING.LESSER, 
#save for the following which are covered under licenses described within 
#their respective files/directories:
# serialization/xmlhandlers.py: Private copyright
# util/urllib2_file.py: GNU LGPL 2.1 and others
# util/cloghandler/*: Apache License Version 2.0
# util/cronexpr.py: Non-standard, please see the file for the license 
License:       LGPLv2+ and ASL 2.0
URL:           http://www.picloud.com
# Patch p1 patches the setup.py so that it doesn't attempt to copy the
# man page and bash configuration files on its own and hence prevent warnings
# Upstream uses this so that they are copied on $python setup.py install
# we don't need that here and we can do it in the RPM itself
Source:        http://pypi.python.org/packages/source/c/cloud/cloud-%{version}.tar.gz
#Patch1:        cloud-%{version}.setup.patch 
BuildArch:     noarch
BuildRequires: python2-devel
BuildRequires: python-setuptools


%description
PiCloud is a cloud-computing platform that integrates into 
the Python Programming Language. This package installs the 
PiCloud client library.

%prep
%setup -q -n cloud-%version
#%patch1 -p1

%install

mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d

%{__python} setup.py install --root $RPM_BUILD_ROOT

#manually copy the manual page and the bash completion files
#cp -p doc/picloud.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
#cp -p bash_completion.d/picloud $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/


%files
%doc doc README.txt CHANGELOG
%{_mandir}/man1/*
%{python_sitelib}/*
%{_bindir}/*
%{_sysconfdir}/bash_completion.d/*

%changelog

* Wed Aug 22 2012 Amit Saha <amitksaha@fedoraproject.org> 2.5.6-1
- New upstream release, changed patch file.

* Mon Mar 24 2012 Amit Saha <amitksaha@fedoraproject.org> 2.4.4-1
- New upstream release, changed patch file.

* Mon Mar 13 2012 Amit Saha <amitksaha@fedoraproject.org> 2.4.2-3
- Added python-setuptools in the Buld-requires, Patch for the setup.py source and misc changes

* Fri Mar 9 2012 Amit Saha <amitksaha@fedoraproject.org> 2.4.2-2
- SPEC file changed to incorporate the comments of reviewers

* Fri Mar 4 2012 Amit Saha <amitksaha@fedoraproject.org> 2.4.2
- Initial package
