#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='graphene_sqlalchemy_autocrud',
    version='0.0.1',
    author='Brent Tubbs',
    author_email='brent.tubbs@gmail.com',
    packages=find_packages(),
    url='https://github.com/harvestport/graphene_sqlalchemy_autocrud',
    description='Tools for automatically building GraphQL query resolvers and mutations from SQLAlchemy models',
    long_description=open('README.md').read(),
    install_requires=[
        'graphene>=2.0.1,<3',
        'graphene_sqlalchemy>=2.0.0,<3',
    ],
)
