Name: ccls
Version: 0.20220729
Release: %autorelease
Summary: A C/C++/Objective-C language server

License: Apache-2.0
URL: https://github.com/MaskRay/ccls

Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.8
BuildRequires:  gcc-c++ >= 7.2
BuildRequires:  llvm-devel >= 7.0
BuildRequires:  clang-devel >= 7.0
BuildRequires:  rapidjson-devel
BuildRequires:  zlib-devel

%description
ccls, which originates from cquery, is a C/C++/Objective-C language server.

- code completion (with both signature help and snippets)
- definition/references, and other cross references
- cross reference extensions: $ccls/call $ccls/inheritance $ccls/member
  $ccls/vars ...
- formatting
- hierarchies: call (caller/callee) hierarchy, inheritance (base/derived)
  hierarchy, member hierarchy
- symbol rename
- document symbols and approximate search of workspace symbol
- hover information
- diagnostics and code actions (clang FixIts)
- semantic highlighting and preprocessor skipped regions
- semantic navigation: $ccls/navigate

# Prepare sources for building (unpack and patch).
%prep
%autosetup -p1
rm -rf third_party/rapidjson

# Compile sources into binaries.
%build
export CLANG_MAJOR_VERSION=$(clang --version|head -1|awk '{print $3}'|awk -F'.' '{print $1}')
%cmake -DCLANG_LINK_CLANG_DYLIB=ON -DCLANG_RESOURCE_DIR=%{_libdir}/clang/$CLANG_MAJOR_VERSION
%cmake_build
chmod 644 LICENSE README.md

# Prepare installation layout by creating directory structure.
%install 
%cmake_install

# Installation of files
%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
%autochangelog
