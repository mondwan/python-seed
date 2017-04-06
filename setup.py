"""
- `File`: setup.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: A script for installing this package
"""

from distutils.core import setup
from ConfigParser import ConfigParser
import os

SETUP_CFG_PATH = 'setup.cfg'

# Instantiate a parser for reading setup.cfg metadata
parser = ConfigParser()
parser.read(SETUP_CFG_PATH)
metadata = dict(parser.items('metadata'))


def getPackages(name):
    # Get paths of __init__.py
    paths = [
        os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk(name)
        for f in files if f == '__init__.py'
    ]
    # Module name = dirname of p and replace / with .
    return [os.path.dirname(p).replace('/', '.') for p in paths]


setup(
    name=metadata['name'],
    version=metadata['version'],
    url=metadata['url'],
    description=metadata['short_description'],
    author=metadata['author'],
    author_email=metadata['author_email'],
    license=metadata['license'],
    packages=getPackages(
        metadata['name']
    ),
)
