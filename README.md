# Portable Educational Python bundle for Windows

Our aim is to create a single-zip Python distribution that comes pre-configured with educational packages, IDEs etc, that can be installed to a USB stick and used both in classrooms and at home.

The plan is to re-pack pre-built Python and binary wheels, plus source for various pure-Python packages. Some links:

* [Official Python from Python.org](https://www.python.org/ftp/python/3.5.1/)
* [Pygame from Appveyor?](https://ci.appveyor.com/project/pygame/pygame-temp-m8dun)
* [PyQT5 from PyPI](https://pypi.python.org/pypi/PyQt5/5.6)

## Obstacles

The Python.org Python distribution is shipped as an installer. The installed distribution includes a python.exe/pythonw.exe that can be relocated in the filesystem, but the pip.exe and other tools from `Scripts/` cannot be.

This has two drawbacks:

1. We cannot use this to create the entry points for our bundle.
2. CLI commands created by pip will be unusable.

These scripts seem to be built [by pip using distlib](https://github.com/pypa/pip/blob/281eb61b09d87765d7c2b92f6982b3fe76ccb0af/pip/_vendor/distlib/scripts.py). Possibly this could be patched to be relocatable. The source for the launcher is [here](https://bitbucket.org/vinay.sajip/distlib/src/tip/PC/). The pip repo holds a copy of distlib including compiled artifacts. 

It might, however, be possible to modify these scripts to create our own entry point binaries, solving issue 1 but not 2.

## Build system

Tbc - but build on Appveyor?
