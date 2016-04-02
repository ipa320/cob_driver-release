Name:           ros-indigo-cob-generic-can
Version:        0.6.7
Release:        0%{?dist}
Summary:        ROS cob_generic_can package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_generic_can
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-utilities
Requires:       ros-indigo-libntcan
Requires:       ros-indigo-libpcan
Requires:       ros-indigo-socketcan-interface
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-utilities
BuildRequires:  ros-indigo-libntcan
BuildRequires:  ros-indigo-libpcan
BuildRequires:  ros-indigo-socketcan-interface

%description
The package cob_generic_can provides an interface for nodes on a can-bus and
examplary wrappers for two PeakSys-can-libs. When a can-bus-device is generated
(for an example see base_dirve_chain) you can use generic_can to create as many
itfs as there will be components communicating via this can-bus. Assign type of
the can communication device (e.g. usb-to-can or can-card of a specific vendor)
and can-address of the target device. This package comes with wrappers for
PeakSys and PeakSysUSB adapters.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Apr 02 2016 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Matthias Gruhler <mig@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

