#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import io
import os
import sys
from shutil import rmtree

from setuptools import setup, find_packages

# Package meta-data.
version='0.2.0'  # lower case for bumpversion
NAME = 'heroku.env'
DESCRIPTION = "CLI tool to load heroku env vars from local .env files"
URL = 'https://github.com/viseshrp/heroku.env'
EMAIL = 'viseshrprasad@gmail.com'
AUTHOR = 'Visesh Prasad'
REQUIRES_PYTHON = ">=2.7"
REQUIREMENTS = ['future>=0.15.2', 'Click>=6.0', ]
SETUP_REQUIREMENTS = ['pytest-runner', ]
TEST_REQUIREMENTS = ['pytest', ]

with io.open('README.rst', 'r', encoding='utf-8') as readme_file:
    README = readme_file.read()

with io.open('HISTORY.rst', 'r', encoding='utf-8') as history_file:
    HISTORY = history_file.read()

working_dir = os.path.abspath(os.path.dirname(__file__))

# more setup.py subcommands
if sys.argv[-1] == 'build':
    print('Removing previous builds...')
    # remove build dir
    os.system('{} setup.py clean --all'.format(sys.executable))

    try:
        rmtree(os.path.join(working_dir, 'dist'))
        rmtree(os.path.join(working_dir, 'heroku.env.egg-info'))
    except OSError:
        pass

    print("Bumping version...")
    os.system('bumpversion minor')

    print("Reinstalling new version...")
    os.system('pip install -e .')

    print("Running build...")
    os.system('{} setup.py sdist bdist_wheel'.format(sys.executable))
    os.system('tar tzf dist/*.tar.gz')

    sys.exit()

if sys.argv[-1] == 'publish':
    os.system('twine upload dist/*')
    sys.exit()

if sys.argv[-1] == 'tags':
    os.system("git tag -a {} -m 'version {}'".format(version, version))
    os.system("git push --tags")
    sys.exit()

if sys.argv[-1] == 'readme':
    print(README)
    sys.exit()

setup(
    name=NAME,
    version=version,
    description=DESCRIPTION,
    long_description=README + '\n\n' + HISTORY,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(include=['heroku_env']),
    include_package_data=True,
    license="MIT license",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        'console_scripts': [
            'heroku.env=heroku_env.__main__:main',
        ],
    },
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIREMENTS,
    keywords='heroku.env heroku env herokuenv heroku_env environment variables load',
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    zip_safe=False,
)
