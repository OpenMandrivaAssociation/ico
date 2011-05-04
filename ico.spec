Name: ico
Version: 1.0.3
Release: %mkrel 2
Summary: Animate an icosahedron or other polyhedron
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Ico displays a wire-frame rotating polyhedron, with hidden lines removed,
or a solid-fill polyhedron with hidden faces removed.  There are a number of
different polyhedra available; adding a new polyhedron to the program is quite
simple.

%prep
%setup -q -n %{name}-%{version}

%build
%configure

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/ico
%{_mandir}/man1/ico.1.*


