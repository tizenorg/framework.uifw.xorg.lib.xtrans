# NOTE: This package contains only C source and header files and pkg-config
# *.pc files, and does not contain any ELF binaries or DSOs, so we disable
# debuginfo generation.
%define debug_package %{nil}

Summary: X.Org X11 developmental X transport library
Name: xorg-x11-xtrans-devel
Version: 1.2.7
Release: 2
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org
BuildArch: noarch

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires: xorg-x11-xutils-dev

%description
X.Org X11 developmental X transport library

%prep
%setup -q

%build

# yes, this looks horrible, but it's to get the .pc file in datadir
%reconfigure --libdir=%{_datadir} \
	   --docdir=%{_docdir}/%{name}-%{version}-%{release}
# Running 'make' not needed.

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%remove_docs

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%dir %{_includedir}/X11
%dir %{_includedir}/X11/Xtrans
%{_includedir}/X11/Xtrans/Xtrans.c
%{_includedir}/X11/Xtrans/Xtrans.h
%{_includedir}/X11/Xtrans/Xtransint.h
%{_includedir}/X11/Xtrans/Xtranslcl.c
%{_includedir}/X11/Xtrans/Xtranssock.c
%{_includedir}/X11/Xtrans/Xtranstli.c
%{_includedir}/X11/Xtrans/Xtransutil.c
%{_includedir}/X11/Xtrans/transport.c
%{_datadir}/aclocal/xtrans.m4
%{_datadir}/pkgconfig/xtrans.pc
#%dir %{_docdir}/%{name}-%{version}-%{release}
#%{_docdir}/%{name}-%{version}-%{release}/xtrans.xml
