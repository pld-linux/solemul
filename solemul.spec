Summary:	Directory tree required by Solaris emulation module
Summary(pl):	Drzewo katalogów potrzebne w trybie emulacji Solarisa.
Name:		solemul
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	%{name}-%{PACKAGE_VERSION}.tar.gz
ExclusiveOs:	Linux
ExclusiveArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the /usr/gnemul/solaris directory tree required
by the Solaris emulation module.

Note that to use this package, you will also need to install several
libraries from your Solaris OS. See accompanying docs for more info.

%description -l pl
Ten pakiet zawiera drzewo katalogowe /usr/gnemul/solaris potrzebne w
trybie emulacji Solarisa. Aby u¿ywaæ tego pakietu, potrzebujesz
jeszcze niektórych bibliotek z Solarisa - patrz dokumentacja.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

(cd $RPM_BUILD_ROOT
tar xzpSf %{SOURCE0}
mv -f solemul-%{version}%{_prefix} usr
rm -rf solemul-%{version}
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_prefix}/gnemul/solaris
