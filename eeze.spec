#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/eeze eeze; \
#cd eeze; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf eeze-$PKG_VERSION.tar.xz eeze/ --exclude .svn --exclude .*ignore

%define snapshot 0

%if %{snapshot}
%define	svndate	20120103
%define	svnrev	66151
%endif

%define major	1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Eeze is a library for easily manipulating devices
Name:		eeze
%if %snapshot
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.2
%else
Version:	1.7.3
Release:	1
%endif
License: LGPLv2+
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
%if %snapshot
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
%endif

BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ecore) >= 1.7.0
BuildRequires:	pkgconfig(ecore-con) >= 1.7.0
BuildRequires:	pkgconfig(ecore-file) >= 1.7.0
BuildRequires:	pkgconfig(edje) >= 1.7.0
BuildRequires:	pkgconfig(eet) >= 1.7.0
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(mount)

%description
Eeze is a library for manipulating devices through udev with a simple and fast
api. It interfaces directly with libudev, avoiding such middleman daemons as
udisks/upower or hal, to immediately gather device information the instant it
becomes known to the system.  This can be used to determine such things as:
  * If a cdrom has a disk inserted
  * The temperature of a cpu core
  * The remaining power left in a battery
  * The current power consumption of various parts
  * Monitor in realtime the status of peripheral devices
  
Each of the above examples can be performed by using only a single eeze
function, as one of the primary focuses of the library is to reduce the
complexity of managing devices.

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries
%rename	%{name}

%description -n %{libname}
Eeze libraries

Eeze is a library for manipulating devices through udev with a simple and fast
api. It interfaces directly with libudev, avoiding such middleman daemons as
udisks/upower or hal, to immediately gather device information the instant it
becomes known to the system.  This can be used to determine such things as:
  * If a cdrom has a disk inserted
  * The temperature of a cpu core
  * The remaining power left in a battery
  * The current power consumption of various parts
  * Monitor in realtime the status of peripheral devices
  
Each of the above examples can be performed by using only a single eeze
function, as one of the primary focuses of the library is to reduce the
complexity of managing devices.

%package -n	%{develname}
Summary:	Headers and development libraries from %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%prep
%if %snapshot
%setup -qn %{name}
%else
%setup -q
%endif

%build
%if %{snapshot}
NOCONFIGURE=yes ./autogen.sh
%endif

%configure2_5x \
	--disable-static \
	--with-mount \
	--with-umount \
	--with-eject
%make

%install
%makeinstall_std

%files
%{_bindir}/eeze*

%files -n %{libname}
%{_libdir}/libeeze.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}*
%{_libdir}/libeeze.so
%{_libdir}/pkgconfig/eeze.pc



%changelog
* Wed Jan 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.99.66151-0.20120103.2
+ Revision: 759676
- build with mount umount

* Thu Jan 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.99.66151-0.20120103.1
+ Revision: 757949
- fixed group
- removed . from end of summary
- new version/snapshot 1.1.99.66151
- merge spec with UnityLinux
- cleaned up spec
- disabled static build
- no more binary

* Fri Apr 29 2011 Crispin Boylan <crisb@mandriva.org> 1.0.1-1
+ Revision: 660721
- New release

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 1.0.0-1
+ Revision: 633927
- 1.0.0 final

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta3.1mdv2011.0
+ Revision: 622799
- 1.0 beta3

* Tue Nov 16 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta2.1mdv2011.0
+ Revision: 597953
- 1.0.0 beta2

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta.1mdv2011.0
+ Revision: 585315
- fix requires
- import eeze

