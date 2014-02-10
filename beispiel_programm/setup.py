#!/usr/bin/env python

from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup

setup(name='HiperCRM Vortrags prog',
      version='0.1',
      description='Ein kleines Django-Projekt um BDD zu demonstrieren',
      author='Gabriel Jacobsohn',
      author_email='gaja@ara.de',
      url='https://github.com/GJacobsohn/bdd_vortrag',
      install_requires=["Django<1.5.5",
                        "django-nose==1.2",
                        "lettuce==0.2.19",
                        "nose==1.3.0",
                        "selenium==2.39.0"],
     )
