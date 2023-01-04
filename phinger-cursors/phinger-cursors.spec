Name: phinger-cursors
Version: 1.1
Release: 1%{?dist}
Summary: An over engineered cursor theme
License: CC-BY-SA-4.0
URL: https://github.com/phisch/phinger-cursors
Source0: https://github.com/phisch/phinger-cursors/releases/download/v1.1/phinger-cursors-variants.tar.bz2

BuildArch: noarch

%description
Say hello to your new cursor theme. Phinger cursors is most likely the most over
engineered cursor theme out there.


%prep
%setup -q -n  phinger-cursors
ls -la

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/phinger-cursors
cp -R * $RPM_BUILD_ROOT/usr/share/icons/phinger-cursors

%files
%defattr(-,root,root,0755)
/usr/share/icons/*


%changelog
* Wed Jan 04 2023 Ashleigh Wilson - 1.1-1
- Initial version of the package.

