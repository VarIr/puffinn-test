#!/usr/bin/env bash
# Build external dependencies that cannot successfully install via pip or conda
# If you use this file as template, don't forget to `chmod a+x newfile`

set -e

# Check for the operating system and install puffinn
if [[ $(uname) == "Darwin" ]]; then
  echo "Running under Mac OS X and CPU..."
  echo "xcode-select --install"
  xcode-select --install || true
  echo "Install MacOS SDK header for 10.14..."
  open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg || true

  echo "git clone puffinn, build, install"
  git clone https://github.com/puffinn/puffinn.git
  cd puffinn
  which gcc
  unset CC
  unset CXX
  python3 setup.py build
  pip install .
  cd ..

elif [[ $(uname -s) == Linux* ]]; then
  echo "Running under Linux on CPU..."
  git clone https://github.com/puffinn/puffinn.git
  cd puffinn
  python3 setup.py build
  pip install .
  cd ..

elif [[ $(uname -s) == MINGW32_NT* ]]; then
  echo "Running under Win x86-32"
  echo "Nothing to build."

elif [[ $(uname -s) == MINGW64_NT* ]]; then
  echo "Running under Win x86-64"
  echo "Nothing to build."

elif [[ $(uname -s) == CYGWIN* ]]; then
  echo "Running under Cygwin"
  echo "Nothing to build."

fi
