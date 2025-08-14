#
# Conditional build:
%bcond_with	tests		# build with tests
#
# TODO:
# - runtime Requires if any

%define		qt_ver		6.6
%define		kf_ver		6.1.0
%define		kfname		kirigami-addons
Summary:	Kirigami addons library
Summary(pl.UTF-8):	Biblioteka Kirigami addons
# not strictly part of framework, but closely bound to KF6 (and cmake config is named KF6KirigamiAddons)
Name:		kf6-kirigami-addons
Version:	1.9.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/kirigami-addons/%{kfname}-%{version}.tar.xz
# Source0-md5:	0935e45ed27717cc492f71a643edc78c
URL:		https://kde.org/
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	Qt6Qml-devel >= %{qt_ver}
BuildRequires:	Qt6Quick-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.20
BuildRequires:	kf6-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf6-kconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kglobalaccel-devel >= %{kf_ver}
BuildRequires:	kf6-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf_ver}
BuildRequires:	kf6-kirigami-devel >= %{kf_ver}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6Qml >= %{qt_ver}
Requires:	Qt6Quick >= %{qt_ver}
Requires:	kf6-dirs
Requires:	kf6-kconfig >= %{kf_ver}
Requires:	kf6-kcoreaddons >= %{kf_ver}
Requires:	kf6-kglobalaccel >= %{kf_ver}
Requires:	kf6-kguiaddons >= %{kf_ver}
Requires:	kf6-ki18n >= %{kf_ver}
Requires:	kf6-kirigami >= %{kf_ver}
Obsoletes:	kirigami-addons < 1.4.0-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kirigami Addons is an additional set of visual components that work
well on mobile and desktop and are guaranteed to be cross-platform. It
uses Kirigami under the hood to create its components and should look
native with any QtQuick Controls style.

%description -l pl.UTF-8
Kirigami Addons to dodatkowy zbiór komponentów graficznych dobrze
działających na urządzeniach przenośnych jak i stacjonarnych, z
gwarantowaną przenośnością między platformami. Pod spodem wykorzystuje
Kirigami do tworzenia komponentów i powinien wyglądać zgodnie z
dowolnym stylem kontrolek QtQuick.

%package devel
Summary:	Header files for Kirigami addons development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających Kirigami addons
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qt_ver}
Requires:	Qt6Qml-devel >= %{qt_ver}
Requires:	Qt6Quick-devel >= %{qt_ver}
Requires:	kf6-kconfig-devel >= %{kf_ver}
Requires:	kf6-kcoreaddons-devel >= %{kf_ver}
Requires:	kf6-ki18n-devel >= %{kf_ver}
Obsoletes:	kirigami-addons-devel < 1.4.0-3

%description devel
Header files for Kirigami addons development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających Kirigami addons.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang kirigami-addons6

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f kirigami-addons6.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKirigamiAddonsStatefulApp.so.*.*.*
%ghost %{_libdir}/libKirigamiAddonsStatefulApp.so.6
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/components
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/libcomponentsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/componentsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/private
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/private/ActionMenuItem.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/private/ActionsMenu.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/private/ContextMenuPage.qml
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/private
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/libdateandtimeplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/dateandtimeplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/libdelegatesplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/delegatesplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/private
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/libformcardplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/formcardplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/libcomponentslabsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/componentslabsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/libsettingsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/settingsplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/libsettingsprivateplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/settingsprivateplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/libsoundsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/soundsplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/libKirigamiAddonsStatefulAppplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/KirigamiAddonsStatefulApp.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/libstatefulapplabsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/statefulapplabsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/libstatefulappprivateplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/statefulappprivateplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/private
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/libtableviewplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/tableviewplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/styles
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/libtreeviewplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/*.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/treeviewplugin.qmltypes
%{_datadir}/kdevappwizard/templates/kirigamiaddons6.tar.bz2

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKirigamiAddonsStatefulApp.so
%{_includedir}/KirigamiAddonsStatefulApp
%{_libdir}/cmake/KF6KirigamiAddons
%{_datadir}/kdevappwizard/templates/librarymanager6.tar.bz2
