Summary:	Animate an icosahedron or other polyhedron
Name:		ico
Version:	1.0.6
Release:	2
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(x11) >= 1.0.0

%description
Ico displays a wire-frame rotating polyhedron, with hidden lines removed,
or a solid-fill polyhedron with hidden faces removed.  There are a number of
different polyhedra available; adding a new polyhedron to the program is quite
simple.

%prep
%autosetup -p1

%build
%configure

%make_build

%install
%make_install

%files
%{_bindir}/ico
%doc %{_mandir}/man1/ico.1.*
