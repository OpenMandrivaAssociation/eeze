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

%if %snapshot
%define	svndate	20120103
%define	svnrev	66151
%endif

%define	major	1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Eeze is a library for easily manipulating devices
Name:		eeze
%if %snapshot
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.2
%else
Version:	1.2.0
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
BuildRequires:	pkgconfig(ecore) >= 1.2.1
BuildRequires:	pkgconfig(edje) >= 1.2.1
BuildRequires:	pkgconfig(libudev)

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
%if %snapshot
NOCONFIGURE=yes ./autogen.sh
%endif

%configure2_5x \
	--disable-static \
	--with-mount \
	--with-umount 
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libeeze.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}*
%{_libdir}/libeeze.so
%{_libdir}/pkgconfig/eeze.pc

