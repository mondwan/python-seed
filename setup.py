"""
- `File`: setup.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: A script for installing this package
"""

from distutils.core import setup
from ConfigParser import ConfigParser

SETUP_CFG_PATH = 'setup.cfg'

# Instantiate a parser for reading setup.cfg metadata
parser = ConfigParser()
parser.read(SETUP_CFG_PATH)
metadata = dict(parser.items('metadata'))

setup(
    name=metadata['name'],
    version=metadata['version'],
    url=metadata['url'],
    description=metadata['short_description'],
    author=metadata['author'],
    author_email=metadata['author_email'],
    license=metadata['license'],
    packages=[
        metadata['name'],
    ],
)
