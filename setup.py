#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: BSD-3-Clause

""" Test puffinn LSH library.

(c) 2019, Roman Feldbauer
University of Vienna, Division of Computational Systems Biology (CUBE)
Contact: <roman.feldbauer@univie.ac.at>
"""

import codecs
from os import path
import re
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Single-sourcing the package version: Read from __init__
def read(*parts):
    with codecs.open(path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="puffinn-test",  # https://pypi.org/project/puffinn-test/
    version=find_version("puffinn_test_package", "__init__.py"),  # version number should comply with PEP 440
    description="Test puffinn",  # "summary" metadata field
    long_description=long_description,  # "Description" metadata field; what people will see on PyPI
    long_description_content_type='text/markdown',  # "Description-Content-Type" metadata field
    url="https://github.com/VarIr/puffinn-test",  # "Home-Page" metadata field
    author="Roman Feldbauer",
    author_email="roman.feldbauer@univie.ac.at",
    maintainer="Roman Feldbauer",
    maintainer_email="roman.feldbauer@univie.ac.at",
    classifiers=[  # https://pypi.org/classifiers/
        'Development Status :: 4 - Beta',
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords="machine-learning high-dimensional-data nearest-neighbor",  # string of words separated by whitespace
    packages=find_packages(exclude=['tests']),  # previously used : packages=['skhubness', 'tests'],
    python_requires='>=3.7',  # 'pip install' will check this
    install_requires=['pybind11',
                      'puffinn;platform_system!="Windows"',  # falconn is not available on Windows; see also PEP 508
                      ],
    extras_require={  # Install using the 'extras' syntax: $ pip install sampleproject[dev]
        # 'dev': ['check-manifest'],
        'test': ['coverage', 'pytest', 'nose'],
    },
)
