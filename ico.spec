Name: ico
Version: 1.0.4
Release: 1
Summary: Animate an icosahedron or other polyhedron
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
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
%makeinstall_std

%files
%{_bindir}/ico
%{_mandir}/man1/ico.1.*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 665499
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 592505
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdv2010.1
+ Revision: 522918
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-5mdv2010.0
+ Revision: 425200
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-4mdv2009.1
+ Revision: 351247
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2009.0
+ Revision: 221579
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 150281
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 23 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.2-1mdv2008.0
+ Revision: 54776
- new upstream version: 1.0.2
- minor %%build cleanup (remove uneeded configure flags)

* Sat Jul 07 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 49298
- rebuild for 2008


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:27:56 (27463)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

