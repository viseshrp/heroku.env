==========
heroku.env
==========


.. image:: https://img.shields.io/pypi/v/heroku_env.svg
        :target: https://pypi.python.org/pypi/heroku.env

.. image:: https://img.shields.io/travis/viseshrp/heroku_env.svg
        :target: https://travis-ci.org/viseshrp/heroku.env

.. image:: https://readthedocs.org/projects/heroku-env/badge/?version=latest
        :target: https://heroku-env.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Simple CLI tool to upload environment variables to Heroku from a .env file.

* GitHub: https://github.com/viseshrp/heroku.env
* PyPI: https://pypi.python.org/pypi/heroku.env
* Free software: MIT license
* Documentation: https://heroku-env.readthedocs.io.


Installation
------------

``pip install heroku.env``


Requirements
------------

#. Python 2.7+
#. `Heroku CLI`_ (Toolbelt) installed.
#. A valid Heroku app name is required to run against.
#. The absolute/relative path to the .env file is also needed, but if not provided, ".env" will be used as the default, which expects a file named .env to be present in the current working directory.
#. Your Heroku API key is also mandatory, which can be set as an environment variable (as `HEROKU_API_KEY` **before** running the tool) or passed with --api-key or -k.


Usage
-----

If your API key is not set, you will be given a password-type prompt to enter it.

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

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
This is also inspired by a script by `sdkcodes`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _sdkcodes: https://github.com/sdkcodes/heroku-config
.. _Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
