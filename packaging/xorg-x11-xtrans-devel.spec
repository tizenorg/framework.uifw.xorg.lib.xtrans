
Name:       xorg-x11-xtrans-devel
Summary:    X.Org X11 developmental X transport library
Version:    1.2.6
Release:    1
Group:      Graphics/X Window System
License:    MIT/X11
URL:        http://www.x.org
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/xorg-x11-xtrans-devel.manifest 
BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --disable-shared
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%manifest xorg-x11-xtrans-devel.manifest
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
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
%{_libdir}/pkgconfig/xtrans.pc
%{_datadir}/aclocal/xtrans.m4
%{_docdir}/xtrans/xtrans.xml


