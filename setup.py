#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

setup(name="singer-python",
      version='5.0.8',
      description="Singer.io utility library",
      author="Stitch",
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      url="http://singer.io",
      install_requires=[
          'jsonschema==2.6.0',
          'pendulum==1.2.0',
          'simplejson==3.11.1',
          'python-dateutil>=2.6.0',
          'backoff==1.3.2',
      ],
      extras_require={
          'dev': [
              'pylint',
              'nose',
              'singer-tools'
          ]
      },
      packages=find_packages(),
      package_data = {
          'singer': [
              'logging.conf'
              ]
          },
)
