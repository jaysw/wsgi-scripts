#!/usr/bin/env python
from setuptools import setup

setup(
    name='WsgiScripts',
    version='0.0.3',
    description="helpers for wrapping and running wsgi apps",
    author='Jay Sweeney',
    author_email='jay.sweeney@wotifgroup.com',
    url='http://www.jaysweeney.com.au',
    include_package_data=True,
    zip_safe=False,
    scripts=['scripts/tornado-run', 'scripts/flask-run'],
    install_requires=['tornado', 'termcolor']
)
