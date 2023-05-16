%global debug_package %{nil}

Name: lua-language-server
Version: 3.6.19
Release: %autorelease
Summary: A language server that offers Lua language support - programmed in Lua.

License: MIT
URL: https://github.com/LuaLS/lua-language-server
Source0: https://github.com/luals/lua-language-server/archive/refs/tags/3.6.19.tar.gz
Source1: ./lua-language-server

BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-static

%description
A language server that offers Lua language support - programmed in Lua.

%prep
%setup -q -c

git clone https://github.com/LuaLS/lua-language-server

%build
cd lua-language-server
./make.sh

%global optdir /opt/%{name}

%install
ls -la lua-language-server/
install -m 0755 -d %{buildroot}%{optdir}/bin
install -m 0755 lua-language-server/bin/lua-language-server %{buildroot}%{optdir}/bin
install -m 0644 lua-language-server/bin/main.lua %{buildroot}%{optdir}/bin
install -m 0644 lua-language-server/main.lua %{buildroot}%{optdir}
install -m 0664 lua-language-server/debugger.lua %{buildroot}%{optdir}
cp -r lua-language-server/locale lua-language-server/meta lua-language-server/script %{buildroot}%{optdir}

# Include lua-language-server wrapper script
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 %{SOURCE1} %{buildroot}%{_bindir}

%files
%license lua-language-server/LICENSE
%doc lua-language-server/README.md

# Install lua-language-server files
%{optdir}

# Install wrapper script to start lua-language-server
%{_bindir}/lua-language-server

%changelog
%autochangelog
