#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_with	qt5		# build qt5
%bcond_without	qt6		# build qt6
#
# TODO:
# - runtime Requires if any

%define		qtver		5.15.2
%define		kfname		kirigami-addons
Summary:	Kirigami addons library
Name:		kirigami-addons
Version:	1.4.0
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/kirigami-addons/%{name}-%{version}.tar.xz
# Source0-md5:	27d23279ee0ad5252a862c2671bc05ad
URL:		http://www.kde.org/
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Quick-controls2-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	kf5-extra-cmake-modules >= 5.102.0
BuildRequires:	kf5-kirigami2-devel >= 5.102.0
BuildRequires:	qt5-build >= %{qtver}
Requires:	kf5-dirs
%endif
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	kf6-extra-cmake-modules >= 5.102.0
BuildRequires:	kf6-kirigami-devel >= 5.102.0
BuildRequires:	qt6-build >= %{qtver}
Requires:	kf6-dirs
%endif
BuildRequires:	catdoc
BuildRequires:	cmake >= 3.20
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kirigami-addons library.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{name}.

%prep
%setup -q

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

%find_lang %{name}6

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}6.lang
%defattr(644,root,root,755)
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/components
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/Avatar.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/AvatarButton.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/Banner.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/BottomDrawer.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/DialogRoundedBackground.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/DoubleFloatingButton.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/FloatingButton.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/MessageDialog.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/SearchPopupField.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/SegmentedButton.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/componentsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/libcomponentsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/DatePopup.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/TimePicker.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/TimePopup.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/dateandtimeplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/libdateandtimeplugin.so
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/private
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/private/DatePathView.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/private/DatePicker.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/private/DatePickerDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/dateandtime/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/DefaultContentItem.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/IndicatorItemDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/RoundedItemDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/RoundedTreeDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/SubtitleContentItem.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/delegatesplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/libdelegatesplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/delegates/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/AboutKDE.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/AboutPage.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/AbstractFormDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormArrow.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormButtonDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormCard.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormCardPage.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormCheckDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormComboBoxDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormDateTimeDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormDelegateBackground.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormDelegateSeparator.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormGridContainer.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormHeader.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormPasswordFieldDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormRadioDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormSectionText.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormSpinBoxDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormSwitchDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormTextDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormTextFieldDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/formcardplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/libformcardplugin.so
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/private
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/private/ContentItemLoader.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/private/SpinButton.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/AbstractMaximizeComponent.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/AlbumMaximizeComponent.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/AlbumModelItem.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/Avatar.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/Banner.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/DialogRoundedBackground.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/DownloadAction.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/ImageMaximizeDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/SearchPopupField.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/VideoMaximizeDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/componentslabsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/libcomponentslabsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/labs/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/CategorizedSettings.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/SettingAction.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/libsettingsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/settingsplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/SoundsPicker.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/libsoundsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/sounds/soundsplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/TreeViewDecoration.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/libtreeviewplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/styles
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/styles/org.kde.desktop
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/styles/org.kde.desktop/TreeViewDecoration.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/treeview/treeviewplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/components/FloatingToolBar.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormCardDialog.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormColorDelegate.qml
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/HeaderComponent.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/KTableView.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/ListTableView.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/libtableviewplugin.so
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/private
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/private/AbstractHeaderComponent.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/private/AbstractTable.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/private/HeaderDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/private/ListCellDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/private/ListRowDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/private/TableCellDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/tableview/tableviewplugin.qmltypes
%attr(755,root,root) %{_libdir}/libKirigamiAddonsStatefulApp.so.*.*
%ghost %{_libdir}/libKirigamiAddonsStatefulApp.so.?
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/formcard/FormTextAreaDelegate.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/ConfigurationModule.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/ConfigurationView.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/SpellcheckingConfigurationModule.qml
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/ActionIconGroup.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/ConfigMobilePage.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/ConfigWindow.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/SonnetConfigPage.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/libsettingsprivateplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/settings/private/settingsprivateplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/KirigamiAddonsStatefulApp.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/StatefulWindow.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/kde-qmlmodule.version
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/NativeMenuItem.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/libstatefulapplabsplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/labs/statefulapplabsplugin.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/libKirigamiAddonsStatefulAppplugin.so
%dir %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/KQuickCommandBarPage.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/KeySequenceItem.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/ShortcutsEditor.qml
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/libstatefulappprivateplugin.so
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/qmldir
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/private/statefulappprivateplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kirigamiaddons/statefulapp/qmldir
%{_datadir}/kdevappwizard/templates/kirigamiaddons6.tar.bz2

%files devel
%defattr(644,root,root,755)
%{_includedir}/KirigamiAddonsStatefulApp
%{_libdir}/libKirigamiAddonsStatefulApp.so
%{_libdir}/cmake/KF6KirigamiAddons
