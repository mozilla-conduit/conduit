# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='autolandweb',
    version='0.1',
    description='A public web API for Mozilla\'s autoland',
    long_description=long_description,
    url='https://mozilla-version-control-tools.readthedocs.io/',
    author='Mozilla',
    author_email='dev-version-control@lists.mozilla.org',
    license='MPL 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='mozilla autoland development',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=['tornado>=4.4.2', 'click>=6.7'],
    extras_require={'test': [
        'pytest',
        'yapf',
        'flake8',
    ], },
    entry_points={
        'console_scripts': ['autolandweb=autolandweb.server:autolandweb', ],
    },
)
