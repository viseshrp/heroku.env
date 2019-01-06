#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import io

from setuptools import setup, find_packages

# Package meta-data.
VERSION = '0.5.0'
NAME = 'heroku.env'
DESCRIPTION = "CLI tool to upload environment variables from local .env files to Heroku"
URL = 'https://github.com/viseshrp/heroku.env'
EMAIL = 'viseshrprasad@gmail.com'
AUTHOR = 'Visesh Prasad'
REQUIRES_PYTHON = ">=2.7"
REQUIREMENTS = ['future>=0.15.2', 'Click>=6.0', 'requests>=1.2.3',
                'heroku3>=3.4.0', 'colorama>=0.4.1']
SETUP_REQUIREMENTS = ['pytest-runner', ]
TEST_REQUIREMENTS = ['pytest', ]

with io.open('README.rst', 'r', encoding='utf-8') as readme_file:
    README = readme_file.read()

with io.open('HISTORY.rst', 'r', encoding='utf-8') as history_file:
    HISTORY = history_file.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README + '\n\n' + HISTORY,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(include=['heroku_env']),
    include_package_data=True,
    license="MIT license",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
