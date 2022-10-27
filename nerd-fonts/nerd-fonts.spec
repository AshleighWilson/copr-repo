Name:    nerd-fonts
Version: 2.2.2
Release: 2%{?dist}
Summary: Nerd Fonts are patched fonts with a high number of glyphs

License: Apache-2.0 and OFL-1.1
URL: https://www.nerdfonts.com/ 
Source0: https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/RobotoMono.zip       
Source1: https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/FiraCode.zip
Source2: https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/JetBrainsMono.zip

BuildArch: noarch

%description
Nerd Fonts is a project that patches developer targeted fonts with a high
number of glyphs (icons). Specifically to add a high number of extra glyphs
from popular 'iconic fonts' such as Font Awesome, Devicons, Octicons, and 
others.

%prep
unzip %{_topdir}/SOURCES/RobotoMono.zip -d RobotoMono
mv RobotoMono/readme.md readme.md
mv RobotoMono/LICENSE.txt LICENSE-RobotoMono
unzip %{_topdir}/SOURCES/FiraCode.zip -d FiraCode
mv FiraCode/LICENSE LICENSE-FiraCode
rm FiraCode/readme.md
unzip %{_topdir}/SOURCES/JetBrainsMono.zip -d JetBrainsMono
rm JetBrainsMono/readme.md

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/fonts/
cp -r RobotoMono FiraCode JetBrainsMono $RPM_BUILD_ROOT/usr/share/fonts/

%files
%defattr(-,root,root,0755)
/usr/share/fonts/
%doc readme.md
%license LICENSE-RobotoMono LICENSE-FiraCode

%post
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache -fv

%changelog
* Thu Oct 27 2022 Ashleigh Wilson - 2.2.2-2
- Includes JetBrainsMono font.

* Fri Oct 14 2022 Ashleigh Wilson - 2.2.2-1
- Initial version of the package.
- Includes RobotoMono and FiraCode fonts.
