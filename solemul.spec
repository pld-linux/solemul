Summary: Directory tree required by Solaris emulation module.
Name: solemul
Version: 1.1
Release: 1
Copyright: GPL
Group: Applications/Emulators
Source: solemul-%{PACKAGE_VERSION}.tar.gz
ExclusiveOs: Linux
ExclusiveArch: sparc sparc64
BuildRoot: /var/tmp/%{name}-root

%description
This package contains the /usr/gnemul/solaris directory tree required
by the Solaris emulation module.

Note that to use this package, you will also need to install several
libraries from your Solaris OS. See accompanying docs for more info.

%prep
%setup -q

%install
mkdir -p $RPM_BUILD_ROOT/
cd $RPM_BUILD_ROOT
tar xzpSf $RPM_SOURCE_DIR/solemul-%{PACKAGE_VERSION}.tar.gz
mv -f solemul-%{PACKAGE_VERSION}/usr usr
rm -rf solemul-%{PACKAGE_VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
/usr/gnemul/solaris
