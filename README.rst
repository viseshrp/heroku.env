==========
heroku.env
==========


.. image:: https://img.shields.io/pypi/v/heroku_env.svg
        :target: https://pypi.python.org/pypi/heroku.env

.. image:: https://img.shields.io/travis/viseshrp/heroku_env.svg
        :target: https://travis-ci.org/viseshrp/heroku_env


Simple CLI tool to upload environment variables to Heroku from a .env file, through the Heroku CLI Toolbelt.

* GitHub: https://github.com/viseshrp/heroku.env
* PyPI: https://pypi.python.org/pypi/heroku.env
* Free software: MIT license

Disclaimer
----------

I'm a beginner when it comes to Python libraries. I've been working on Django for over a year
and that encompasses all my experience with Python. This library was a quick personal project
because we use Heroku a lot at work and I find it really annoying when you have to add env vars
manually from your local environment every time. This is also my first venture into open source
Python and my very first library on PyPI. If you're a rockstar dev reading this, I cannot be happier
and I cannot tell you how much your feedback would mean to me :) Thanks.

Installation
------------

``pip install heroku.env``


Requirements
------------

#. Python 2.7+
#. `Heroku CLI`_ (Toolbelt) installed.
#. A valid Heroku app name is required to run against.
#. The absolute/relative path to the .env file is also needed, but if not provided, ".env" will be used as the default, which expects a file named .env to be present in the current working directory.
#. Your Heroku API key (found `here`_ or by running `this`_) is also mandatory, which must be set as an environment variable (as `HEROKU_API_KEY` **before** running the tool) or passed with --api-key or -k.


Usage
-----

If the API key is set as an environment variable, it will be automatically read.

If it is not set, you will be given a password-type prompt to enter it.

It is recommended for security purposes that you set it as an environment variable before running the tool, like this:

``$ export HEROKU_API_KEY=a1b12c24-ab1d-123f-5678-1234b12a0a1b``

Example usages:

This is perfect.

``$ heroku.env --app swimming-briskly-123 --env-file dot.env``

This is **not** recommended, but still available as an option.

``$ heroku.env --app swimming-briskly-123 --env-file dot.env --api-key a1b12c24-ab1d-123f-5678-1234b12a0a1b``


See all options by:

``$ heroku.env --help``

Features
--------

* Auto-setting of all env vars from a .env file
* Lines starting with # are considered comments and ignored
* Secure, does not store your API key anywhere.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
This is also inspired by a script by `sdkcodes`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _sdkcodes: https://github.com/sdkcodes/heroku-config
.. _Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
.. _here: https://dashboard.heroku.com/account
.. _this: https://devcenter.heroku.com/articles/authentication#retrieving-the-api-token
