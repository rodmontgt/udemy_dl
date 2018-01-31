#!/usr/bin/env python

import os
import subprocess
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [pkg.split('=')[0] for pkg in open('requirements.txt').readlines()]

description = 'Download videos from Udemy for personal offline use'
try:
    subprocess.call(["pandoc", "README.md", "-f", "markdown", "-t", "rst", "-o", "README.rst"])
    long_description = open("README.rst").read()
except OSError:
    print("Pandoc not installed")
    long_description = description

classifiers = ['Environment :: Console',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 3',
               'Topic :: Multimedia :: Video',
               ]

version = open('CHANGES.txt').readlines()[0][1:].strip()

# if installed as root or with sudo, set permission mask to allow read/exec for all users
try:
    if os.getuid() == 0:
        os.umask(int('022', 8))
except AttributeError as e:
    print("Error: Setting permission mask to allow read/exec for all users failed!\nDetails: {0}".format(e))

setup(name='udemy-dl',
      version=version,
      description=description,
      author='Gaganpreet Singh Arora',
      author_email='gaganpreet.arora@gmail.com',
      url='https://github.com/nishad/udemy-dl',
      scripts=['src/udemy-dl',],
      install_requires=requirements,
      long_description=long_description,
      packages=['udemy_dl'],
      package_dir = {'udemy_dl': 'src/udemy_dl'},
      classifiers=classifiers
    )
