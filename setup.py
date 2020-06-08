import re
from os.path import join, dirname

from setuptools import setup, find_packages


dependencies = [
    'rarfile',
]


setup(
    name='archive',
    description='A tool for archive types',
    author='Mehdi Nazari',
    author_email='mehdi.nazari.3727@gmail.com',
    install_requires=dependencies,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT',
)

