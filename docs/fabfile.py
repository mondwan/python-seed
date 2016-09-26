"""
- `File`: fabfile.py

- `Author`: Me

- `Email`: 0

- `Github`: 0

- `Description`: Makefile for generating documentaiton
"""

import os
from fabric.api import local
from ConfigParser import ConfigParser

# Project root
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Document root
DOC_DIR = os.path.join(PROJECT_DIR, 'docs')

# Build root
BUILD_DIR = os.path.join(DOC_DIR, 'build')

# Root of .rst
RST_SRC_DIR = os.path.join(DOC_DIR, 'src')

# METADATA
SETUP_CFG_PATH = os.path.join(PROJECT_DIR, 'setup.cfg')

# CURRENT_PATH
CURRENT_PATH = os.getcwd()


def fix_directory(f):
    """
    A decorator function which setup directory for us
    """
    def wrapped(*args, **kwargs):
        # Make sure we works under documentation root
        os.chdir('%s' % DOC_DIR)

        ret = f(*args, **kwargs)

        # Going back to current path
        os.chdir('%s' % CURRENT_PATH)

        return ret

    return wrapped


def get_metadata():
    """
    Return metadata of this project

    Return:

    - `dict`
    """
    # Instantiate a parser for reading setup.cfg metadata
    parser = ConfigParser()
    parser.read(SETUP_CFG_PATH)
    metadata = dict(parser.items('metadata'))

    return metadata


@fix_directory
def initialize():
    """
    Generate conf.py and index.rst by the help of sphinx-quickstart
    """
    metadata = get_metadata()
    cmd = 'sphinx-quickstart %s %s'
    cmd_opts = [
        ('--quiet', ''),
        ('-p', '"%s"' % metadata['name']),
        ('-a', '"%s"' % metadata['author']),
        ('-v', '"%s"' % metadata['version']),
        ('--suffix=.rst', ''),
        ('--ext-autodoc', ''),
        ('--ext-coverage', ''),
        ('--ext-viewcode', ''),
        ('--no-makefile', ''),
        ('--no-batchfile', ''),
    ]

    # normalized cmd_opts
    normalized_opts = [
        opt for cmd_opt in cmd_opts for opt in cmd_opt if len(opt) > 0
    ]

    # join them by space
    option_string = ' '.join(normalized_opts)

    # construct the final cmd
    cmd = cmd % (option_string, BUILD_DIR)

    # run the command
    local(cmd)

    # Moving index from BUILD_DIR to RST_SRC_DIR if it does not exist at first
    local('mv -n %s %s' % (
        os.path.join(BUILD_DIR, 'index.rst'),
        RST_SRC_DIR
    ))

    # Remove index.rst in build dir if it still exists
    local('rm -f %s' % os.path.join(BUILD_DIR, 'index.rst'))


@fix_directory
def make(builder='html'):
    """
    `making` documentation in one command

    Parameters:

    - `builder`: type of builder defined by sphinx-build
    """
    isInit = os.path.isfile(os.path.join(BUILD_DIR, 'conf.py'))

    # If there is no conf.py, generate them
    if not isInit:
        initialize()

    # Get metadata
    metadata = get_metadata()

    # Render apidoc
    # Assume the module, which named as metadata['name'], had been placed under
    # PROJECT_DIR
    cmd = 'sphinx-apidoc -M -e -o %s %s' % (
        RST_SRC_DIR,
        os.path.join(PROJECT_DIR, metadata['name']),
    )
    local(cmd)

    # Based on the given builder, rendering documentaiton
    cmd = 'sphinx-build -b %s -d %s -c %s %s %s' % (
        builder,
        os.path.join(BUILD_DIR, 'doctrees'),
        BUILD_DIR,
        RST_SRC_DIR,
        os.path.join(BUILD_DIR, builder),
    )
    local(cmd)


@fix_directory
def clean():
    """
    Clean generated files
    """
    # Get metadata
    metadata = get_metadata()

    # Remove generated files
    cmd = 'rm -fr %s' % BUILD_DIR
    local(cmd)

    # Remove those generated api .rst
    cmd = 'rm -f %s' % os.path.join(RST_SRC_DIR, 'modules.rst')
    local(cmd)
    cmd = 'rm -f %s' % os.path.join(RST_SRC_DIR, '%s*.rst' % metadata['name'])
    local(cmd)
