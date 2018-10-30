Summary:	Animate an icosahedron or other polyhedron
Name:		ico
Version:	1.0.5
Release:	3
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(x11) >= 1.0.0

%description
Ico displays a wire-frame rotating polyhedron, with hidden lines removed,
or a solid-fill polyhedron with hidden faces removed.  There are a number of
different polyhedra available; adding a new polyhedron to the program is quite
simple.

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall_std

%files
%{_bindir}/ico
%{_mandir}/man1/ico.1.*

