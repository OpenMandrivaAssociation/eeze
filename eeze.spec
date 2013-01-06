%define major	1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Eeze is a library for easily manipulating devices
Name:		eeze
Version:	1.7.3
Release:	1
License:	LGPLv2+
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2

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

%package -n	%{devname}
Summary:	Headers and development libraries from %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name} development headers and libraries.

%prep
%setup -q

%build
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

%files -n %{devname}
%{_includedir}/%{name}*
%{_libdir}/libeeze.so
%{_libdir}/pkgconfig/eeze.pc

