Name:           ros-indigo-cob-light
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS cob_light package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_light
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-visualization-msgs
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
This package contains scripts to operate the LED lights on Care-O-bot.

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
* Tue Aug 25 2015 Benjamin Maidel <bnm@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Benjamin Maidel <bnm@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Mon Dec 15 2014 Benjamin Maidel <bnm@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Wed Sep 17 2014 Benjamin Maidel <bnm@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Tue Sep 09 2014 Benjamin Maidel <bnm@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Benjamin Maidel <bnm@ipa.fhg.de> - 0.5.7-0
- Autogenerated by Bloom

