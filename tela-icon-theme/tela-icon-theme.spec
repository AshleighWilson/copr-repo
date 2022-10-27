%global debug_package %{nil}

Name:    tela-icon-theme 
Version: 2022_08_28
Release: 1%{?dist}
Summary: A flat, colorful icon theme

License: GPLv3
URL: https://github.com/vinceliuice/Tela-icon-theme
Source0: https://github.com/vinceliuice/Tela-icon-theme/archive/refs/tags/2022-08-28.tar.gz

BuildArch: noarch
BuildRequires: gtk-update-icon-cache
BuildRequires: fdupes

%description
A flat, colorful icon theme

%prep
%setup -q -n Tela-icon-theme-2022-08-28

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/
bash install.sh purple -d $RPM_BUILD_ROOT/usr/share/icons/
%fdupes -s $RPM_BUILD_ROOT/usr/share/icons

rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple-dark/16/actions/preferences-desktop-baloo.svg
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple-dark/22/devices/uav.svg
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple-dark/24/devices/uav.svg
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple-dark/symbolic/actions/outbox-symbolic.svg
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple-dark/symbolic/actions/scan-type-batch-symbolic.svg
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple/16/actions/preferences-desktop-baloo.svg
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple/22/devices/uav.svg
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple/24/devices/uav.svg
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple/scalable/apps/steam_icon_1486350.svg
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple/symbolic/actions/outbox-symbolic.svg 
rm $RPM_BUILD_ROOT/usr/share/icons/Tela-purple/symbolic/actions/scan-type-batch-symbolic.svg

%files
%defattr(-,root,root,0755)
/usr/share/icons/*
%doc README.md

%changelog
* Sun Oct 16 2022 Ashleigh Wilson - 2022_08_28-1
- Initial version of the package.
- Includes purple and purple-dark icons.
