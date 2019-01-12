%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		filelight
Summary:	Filelight
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	64d0b2a40221ae7925f9b9cc5ec2d507
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-ki18n-devel >= 5.23.0
BuildRequires:	kf5-kio-devel >= 5.23.0
BuildRequires:	kf5-kxmlgui-devel >= 5.23.0
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
