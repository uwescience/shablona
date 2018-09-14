from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "toymir: a toy package for learning about OSS in MIR"
# Long description will go up on the pypi page
long_description = """

toymir
========
toymir is a small Python package for use in the ISMIR 2018 tutorial on
open source software and reproducibility.

It is based on the Shablona_ package, developed by Ariel Rokem at the
University of Washington eScience Institute.

.. _Shablona: https://github.com/uwescience/shablona
"""

NAME = "toymir"
MAINTAINER = "Brian McFee"
MAINTAINER_EMAIL = "brian.mcfee@nyu.edu"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/bmcfee/ismir2018-oss-tutorial"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Brian McFee"
AUTHOR_EMAIL = "brian.mcfee@nyu.edu"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'toymir': [pjoin('data', '*')]}
REQUIRES = ["numpy"]
