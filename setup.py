#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="time_decode",
    version="2.2",
    author="Corey Forman",
    license="MIT",
    url="https://github.com/digitalsleuth/time_decode",
    description=("Python 3 timestamp decode/encode tool"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "python-dateutil",
        "colorama"
    ],
    scripts=['time_decode.py'],
    package_data={'': ['README.md, LICENSE.md']}
)