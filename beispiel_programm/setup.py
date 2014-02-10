#!/usr/bin/env python

from distutils.core import setup

setup(name='HiperCRM Vortrags prog',
      version='0.1',
      description='Dies ist ein kleines Djaqngo Projekt um BDD zu ',
      author='Gabriel Jacobsohn',
      author_email='gaja@ara.de',
      url='https://github.com/GJacobsohn/bdd_vortrag',
      install_requires=["Django<1.6",
                "django-nose==1.2",
                "lettuce==0.2.19",
                "nose==1.3.0",
                "selenium==2.39.0"],
     )
