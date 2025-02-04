Name:           opentrack-fedora
Version:        1.0.0
Release:        1%{?dist}
Summary:        Head tracking software for gaming and simulation

License:        GPLv3+
URL:            https://github.com/TripleJump1/Opentrack-Fedora
Source0:        https://github.com/opentrack/opentrack.git

BuildArch:      x86_64

Requires:       qt5-qttools, qt5-qtbase, procps-ng, opencv

%description
OpenTrack is an application that lets you track head movements for gaming and simulation.
This package provides a prebuilt Fedora-compatible OpenTrack binary for easy installation.

%prep
# No source code to prepare, as we are using prebuilt binaries

%build
# No compilation needed

%install
mkdir -p %{buildroot}/usr/bin
cp -r %{_sourcedir}/opentrack %{buildroot}/usr/bin/opentrack

%files
/usr/bin/opentrack

%changelog
* Mon Feb 03 2025 TripleJump1 <your-email@example.com> - 1.0.0-1
- Initial release of OpenTrack for Fedora/Nobara
- Packaged prebuilt OpenTrack binaries
