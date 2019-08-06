Name:           ros-melodic-cob-canopen-motor
Version:        0.7.0
Release:        1%{?dist}
Summary:        ROS cob_canopen_motor package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_canopen_motor
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-cob-generic-can
Requires:       ros-melodic-cob-utilities
Requires:       ros-melodic-roscpp
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cob-generic-can
BuildRequires:  ros-melodic-cob-utilities
BuildRequires:  ros-melodic-roscpp

%description
The package cob_canopen_motor implements a controller-drive component which is
connected to a can-bus and works with a canopen-interface.
&quot;CanDriveItf&quot; provides a - more or less - generic interface to the
controller-drive components. &quot;CanDrvie...&quot; then implements a specific
setup, e.g. an ELMO Harmonica Controller in case of the
&quot;CanDriveHarmonica&quot;.

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

