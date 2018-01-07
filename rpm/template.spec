Name:           ros-indigo-cob-elmo-homing
Version:        0.6.11
Release:        0%{?dist}
Summary:        ROS cob_elmo_homing package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-canopen-402
Requires:       ros-indigo-class-loader
BuildRequires:  ros-indigo-canopen-402
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-class-loader

%description
This packagae implements the special homing procedure that is needed for old
cob4/raw bases

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
* Sun Jan 07 2018 Florian Weisshardt <florian.weisshardt@ipa.fraunhofer.de> - 0.6.11-0
- Autogenerated by Bloom

* Mon Jul 24 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.6.10-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.6.8-0
- Autogenerated by Bloom

* Sat Apr 02 2016 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.6.7-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.6.6-0
- Autogenerated by Bloom

