Name:           ros-indigo-cob-voltage-control
Version:        0.6.7
Release:        0%{?dist}
Summary:        ROS cob_voltage_control package

Group:          Development/Libraries
License:        LGPL
URL:            None
Source0:        %{name}-%{version}.tar.gz

Requires:       blt
Requires:       ros-indigo-cob-msgs
Requires:       ros-indigo-cob-phidgets
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       tcl
Requires:       tix
Requires:       tk
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-msgs
BuildRequires:  ros-indigo-cob-phidgets
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs

%description
Interface to IO board that manages emergency stop and battery voltage on
rob@work 3

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
* Sat Apr 02 2016 Alexander Bubeck <aub@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Alexander Bubeck <aub@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Alexander Bubeck <aub@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Alexander Bubeck <aub@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Alexander Bubeck <aub@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

