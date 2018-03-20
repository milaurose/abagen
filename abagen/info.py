# -*- coding: utf-8 -*-

__version__ = '0.0.1'

NAME = 'abagen'
MAINTAINER = 'Ross Markello'
VERSION = __version__
LICENSE = 'MIT'
DOWNLOAD_URL = 'http://github.com/rmarkello/abagen'
DESCRIPTION = """
A toolbox for working with the Allen Brain Atlas genetic expression data.
"""

INSTALL_REQUIRES = [
    'nibabel',
    'numpy',
    'pandas',
    'scikit-learn'
    'scipy',
]

TESTS_REQUIRE = [
    'pytest',
]

PACKAGE_DATA = {
}