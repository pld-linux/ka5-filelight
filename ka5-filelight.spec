%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		filelight
Summary:	Filelight
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	297295e9313df2afaeba6ec1fabb8128
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_iconsdir}/hicolor/32x32/actions/views_filelight.png
%{_iconsdir}/hicolor/32x32/apps/filelight.png
%{_iconsdir}/hicolor/48x48/apps/filelight.png
%{_iconsdir}/hicolor/64x64/apps/filelight.png
%dir %{_datadir}/kxmlgui5/filelight
%{_datadir}/kxmlgui5/filelight/filelightui.rc