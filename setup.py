#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for danatacppwrapper

You can install danatacppwrapper with

python setup.py install
"""
from glob import glob
import os
import sys
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

if sys.version_info[:2] < (2, 7):
    print("danata-cpp-wrapper requires Python 2.7 or later (%d.%d detected)." %
          sys.version_info[:2])
    sys.exit(-1)

# Write the version information.
sys.path.insert(0, 'danatacppwrapper')
import release
version = release.write_versionfile()
sys.path.pop(0)

packages=["danatacppwrapper",
          "danatacppwrapper.classes",
          "danatacppwrapper.transform",
          "danatacppwrapper.external",
          "danatacppwrapper.readwrite",
          "danatacppwrapper.utils"]

docdirbase  = 'share/doc/danatacppwrapper-%s' % version
# add basic documentation
data = [(docdirbase, glob("*.txt"))]
# add examples
for d in ['draw_ast']:
    dd = os.path.join(docdirbase,'examples', d)
    pp = os.path.join('examples', d)
    data.append((dd, glob(os.path.join(pp ,"*.py"))))
    data.append((dd, glob(os.path.join(pp ,"*.bz2"))))
    data.append((dd, glob(os.path.join(pp ,"*.gz"))))
    data.append((dd, glob(os.path.join(pp ,"*.mbox"))))
    data.append((dd, glob(os.path.join(pp ,"*.edgelist"))))

# add the tests
#package_data     = { 'danatacppwrapper': ['tests/*.py'] }

install_requires = ['decorator>=3.4.0']

if __name__ == "__main__":

    setup(
        name             = release.NAME.lower(),
        version          = version,
        maintainer       = release.MAINTAINER,
        maintainer_email = release.MAINTAINER_EMAIL,
        author           = release.AUTHORS['Youngsung'][0],
        author_email     = release.AUTHORS['Youngsung'][1],
        description      = release.DESCRIPTION,
        keywords         = release.KEYWORDS,
        long_description = release.LONG_DESCRIPTION,
        license          = release.LICENSE,
        platforms        = release.PLATFORMS,
        url              = release.URL,
        download_url     = release.DOWNLOAD_URL,
        classifiers      = release.CLASSIFIERS,
        packages         = packages,
        data_files       = data,
#        package_data     = package_data,
        install_requires = install_requires,
        setup_requires   = ['pytest-runner'],
#        test_suite       = 'testing',
        tests_require    = ['pytest'],
        zip_safe         = False
    )
