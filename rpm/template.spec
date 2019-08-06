Name:           ros-melodic-cob-base-drive-chain
Version:        0.7.0
Release:        1%{?dist}
Summary:        ROS cob_base_drive_chain package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_base_drive_chain
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-cob-canopen-motor
Requires:       ros-melodic-cob-generic-can
Requires:       ros-melodic-cob-utilities
Requires:       ros-melodic-control-msgs
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cob-canopen-motor
BuildRequires:  ros-melodic-cob-generic-can
BuildRequires:  ros-melodic-cob-utilities
BuildRequires:  ros-melodic-control-msgs
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs

%description
This package contains classes that are able to control the platform of the
Care-O-Bot. This means to establish a CAN communication to drive and steering
motors of the platform and later send motion commands and receive motor
information.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Aug 06 2019 Matthias Gruhler <mig@ipa.fhg.de> - 0.7.0-1
- Autogenerated by Bloom

