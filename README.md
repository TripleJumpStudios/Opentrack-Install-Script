# Opentrack Build Script

This repository contains a Bash script that automates the process of building and installing [opentrack](https://github.com/opentrack/opentrack) on Fedora-based systems including Nobara using `dnf`.

## Overview

The script performs the following tasks:

1. **Dependency Handling:**  
   - Checks for conflicting Wine packages and selects the appropriate development package (`wine-devel` or `wine-staging-devel`).
   - Installs necessary dependencies including `cmake`, `git`, `qt5` packages, `opencv-devel`, `onnxruntime-devel`, and others.

2. **Repository Management:**  
   - Clones the opentrack repository if it doesn't exist.
   - Updates the repository if it already exists.

3. **Build Process:**  
   - Configures the build environment using CMake (with support for ONNXRuntime and Wine SDK).
   - Compiles opentrack using `make` with parallel processing.
   - Installs opentrack locally within the build directory.

4. **Post-Installation Instructions:**  
   - Provides instructions on adding the opentrack executable to your PATH.
   - Offers an optional cleanup step for unused dependencies.

## Prerequisites

- **Operating System:**  
  A Fedora-based Linux distribution or any system that uses `dnf` as its package manager.

- **Permissions:**  
  The script must be run as a non-root user with sudo privileges.

## Usage

- Download the script, open a terminal in the directory where you put it and make it executable with `chmod +x v1.0_opentrack_build.sh`

- Run the script with `./v1.0_opentrack_build.sh`
  - note: Depending on dependencies it could take some time to complete.
 
- After install for easier access you can add the opentrack directory to PATH
  - `export PATH="$HOME/opentrack/build/install/bin:$PATH"`

## Tested Distros
- Fedora Workstation 41
- Nobara 41

## Disclaimer

This script is provided "as is" without any warranty. Use it at your own risk. The author is not responsible for any damage or data loss resulting from the use of this script.
