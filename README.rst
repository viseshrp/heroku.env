==========
heroku.env
==========


.. image:: https://img.shields.io/pypi/v/heroku_env.svg
        :target: https://pypi.python.org/pypi/heroku.env

.. image:: https://img.shields.io/travis/viseshrp/heroku_env.svg
        :target: https://travis-ci.org/viseshrp/heroku.env

.. image:: https://readthedocs.org/projects/herokuenv/badge/?version=latest
        :target: https://herokuenv.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Simple CLI tool to upload environment variables to Heroku from a .env file, through the Heroku CLI Toolbelt.

* GitHub: https://github.com/viseshrp/heroku.env
* PyPI: https://pypi.python.org/pypi/heroku.env
* Free software: MIT license
* Documentation: https://herokuenv.readthedocs.io.

Disclaimer
----------

This library was a quick personal project because we use Heroku a lot at work and I find it really annoying
when you have to add env vars manually from your local environment every time.
This is also my first venture into open source Python and my very first library on PyPI.
If you're a rockstar dev reading this, I cannot be happier
and I cannot tell you how much your feedback would mean to me :) Thanks.

Installation
------------

``pip install heroku.env``


Requirements
------------

#. Tested on Python 3.6+ but may work in Python 2.7+.
#. `Heroku CLI`_ (Toolbelt) installed.
#. A valid Heroku app name is required to run against.
#. The absolute/relative path to the .env file is also needed, but if not provided, ".env" will be used as the default, which expects a file named .env to be present in the current working directory.
#. Your Heroku API key (found `here`_ or by running `this`_), for use with Heroku CLI.


Features
--------

* Auto-setting of all env vars from a .env file.

Examples:

``$ heroku.env --app swimming-briskly-123 --env-file dot.env``

* Lines starting with # are considered comments in the env file and ignored.

Examples:

``# Django settings module``
``DJANGO_SETTINGS_MODULE=portfolio.settings``

* Allow setting of alternate values by specifying **alt_value=VALUE** in comments of the env file.

For example, if using the .env file in production and you want to set a different value.

NOTE: The **alt_value** needs to be on the line right before the actual env var you want to change.

Examples of allowed usages:

``# Django settings module alt_value=portfolio.prod_settings``
``DJANGO_SETTINGS_MODULE=portfolio.settings``

OR

``# Django settings module``
``# alt_value=portfolio.prod_settings``
``DJANGO_SETTINGS_MODULE=portfolio.settings``

OR

``# alt_value=portfolio.prod_settings``
``# Django settings module``
``DJANGO_SETTINGS_MODULE=portfolio.settings``

Note that anything specified after **alt_value=** is used as the alternate value.

AND then,

``$ heroku.env --app swimming-briskly-123 --env-file dot.env --set-alt``

* Secure, does not store your API key anywhere.

The API key can be set as an environment variable (as `HEROKU_API_KEY` **before** running the tool) or passed with --api-key or -k.

If the API key is set as an environment variable, it will be automatically read.

If it is not set in any way, you will be given a password-type prompt to enter it.

It is recommended for security purposes that you set it as an environment variable before running the tool, like this:

``$ export HEROKU_API_KEY=a1b12c24-ab1d-123f-5678-1234b12a0a1b``

OR you can wait for the prompt.

This is **not** recommended, but still available as an option.

``$ heroku.env --app swimming-briskly-123 --env-file dot.env --api-key a1b12c24-ab1d-123f-5678-1234b12a0a1b``


See all options with:

``$ heroku.env --help``


Credits
-------

* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
* This is inspired by a script by `sdkcodes`_.
* `Click`_, for making writing CLI tools a complete pleasure.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _sdkcodes: https://github.com/sdkcodes/heroku-config
.. _Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
.. _here: https://dashboard.heroku.com/account
.. _this: https://devcenter.heroku.com/articles/authentication#retrieving-the-api-token
.. _Click: https://click.palletsprojects.com
