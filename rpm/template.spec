Name:           ros-kinetic-cob-mimic
Version:        0.6.11
Release:        0%{?dist}
Summary:        ROS cob_mimic package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_mimic
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       libvlc-devel
Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       vlc
BuildRequires:  boost-devel
BuildRequires:  libvlc-devel
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslib
BuildRequires:  vlc

%description
This package implements the Care-O-bot mimic

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Jan 07 2018 Benjamin Maidel <benjamin.maidel@ipa.fraunhofer.de> - 0.6.11-0
- Autogenerated by Bloom

* Mon Jul 24 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.10-0
- Autogenerated by Bloom

