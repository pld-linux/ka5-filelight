%define		kdeappsver	20.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		filelight
Summary:	Filelight
Name:		ka5-%{kaname}
Version:	20.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3ea8f25f27a30b95e92136e4ba5735a3
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filelight allows you to understand exactly where your diskspace is
being used by graphically representating your filesystem as a set of
concentric segmented-rings.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/filelightrc
%attr(755,root,root) %{_bindir}/filelight
%{_desktopdir}/org.kde.filelight.desktop
%{_iconsdir}/hicolor/16x16/apps/filelight.png
%{_iconsdir}/hicolor/22x22/apps/filelight.png
#%%{_iconsdir}/hicolor/32x32/actions/views_filelight.png
%{_iconsdir}/hicolor/32x32/apps/filelight.png
%{_iconsdir}/hicolor/48x48/apps/filelight.png
%{_iconsdir}/hicolor/64x64/apps/filelight.png
%{_iconsdir}/hicolor/128x128/apps/filelight.png
%dir %{_datadir}/kxmlgui5/filelight
%{_datadir}/kxmlgui5/filelight/filelightui.rc
%{_datadir}/metainfo/org.kde.filelight.appdata.xml
%{_datadir}/qlogging-categories5/filelight.categories
