# -*- coding: utf-8 -*-
# Copyright (c) XiMing Xing. All rights reserved.
# Author: XiMing Xing

import os
import subprocess
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info


setup(
    name="vectorfusion",
    version="0.1.0",
    packages=[p for p in find_packages() if p.startswith('vectorfusion') ],
    package_data={'vectorfusion': ['py.typed']},
    install_requires=[
        # Base dependencies will be handled by custom install command
    ],
    python_requires=">=3.7",
    # Metadata
    author='XiMing Xing',
    author_email='ximingxing@gmail.com',
    description="VectorFusion Implementation",
    long_description="",
    long_description_content_type="text/markdown",
    keywords="svg, rendering, diffvg",
    url='https://github.com/ximinng/DiffSketcher',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
