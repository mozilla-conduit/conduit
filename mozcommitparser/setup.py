# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

from setuptools import setup, find_packages

PACKAGE = "mozcommitparser"
VERSION = "1.0rc1"

HERE = os.path.dirname(os.path.abspath(__file__))

setup(
    name=PACKAGE,
    description="Parse and manipulate commit messages from the Mozilla commit "
    "pipeline.",
    license="MPL 2.0",
    url="",  # FIXME
    version=VERSION,
    author="Mozilla Automation and Tools team",
    author_email="",  # FIXME
    keywords="mozilla",
    long_description=open(os.path.join(HERE, "README.rst")).read(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    zip_safe=False,  # FIXME
    classifiers=[
        "Development Status :: 5 - Production/Stable"
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[],
)
