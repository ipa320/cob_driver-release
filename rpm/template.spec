Name:           ros-indigo-cob-sick-lms1xx
Version:        0.6.10
Release:        0%{?dist}
Summary:        ROS cob_sick_lms1xx package

Group:          Development/Libraries
License:        GPL,LGPL
URL:            http://ros.org/wiki/cob_sick_lms1xx
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
This package published a laser scan message out of a Sick LMS1xx laser scanner.
This version is made by fusion of ipa320/RCPRG_laser_drivers and
ipa320/libLMS1xx repository. This package shuld have clearer structure and be
easier to install.

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
* Mon Jul 24 2017 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.8-0
- Autogenerated by Bloom

* Sat Apr 02 2016 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Joshua Hampp <joshua.hampp@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

