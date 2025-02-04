Name:           opentrack-fedora
Version:        1.0.0
Release:        1%{?dist}
Summary:        Head tracking software for gaming and simulation

License:        GPLv3+
URL:            https://github.com/TripleJump1/Opentrack-Fedora
Source0:        https://github.com/opentrack/opentrack/archive/refs/tags/opentrack-2023.3.0.tar.gz

BuildArch:      x86_64

Requires:       qt5-qttools, qt5-qtbase, procps-ng, opencv

%description
OpenTrack is an application that lets you track head movements for gaming and simulation.
This package provides a prebuilt Fedora-compatible OpenTrack binary for easy installation.

%prep
# Extract the tarball
%setup -q

%build
# No compilation needed

%install
# Create installation directory and copy files
mkdir -p %{buildroot}/usr/bin
cp -r %{_sourcedir}/opentrack-2023.3.0/* %{buildroot}/usr/bin/

%files
/usr/bin/opentrack

%changelog
* Mon Feb 03 2025 TripleJump1 <your-email@example.com> - 1.0.0-1
- Initial release of OpenTrack for Fedora/Nobara
- Packaged prebuilt OpenTrack binaries
