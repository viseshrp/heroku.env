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

.. image:: https://pepy.tech/badge/heroku-env
        :target: https://pepy.tech/project/heroku-env
        :alt: Downloads


Simple CLI tool to upload environment variables to Heroku from a .env file, through the Heroku API.

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
.. code-block:: bash

    pip install heroku.env


Requirements
------------

#. Python 2.7+
#. Your Heroku API key (found `here`_ or by running `this`_), for the Heroku API to run and authenticate you.
#. A valid Heroku app name is required to run against.
#. The absolute/relative path to the .env file is also needed, but if not provided, ``.env`` will be used as the default file name, which expects a file named ``.env`` to be present in the current working directory.


Features
--------

* Auto-setting of all env vars from a .env file.

    Examples:

    .. code-block:: bash

        $ heroku.env --app swimming-briskly-123 --env-file dot.env

* Lines starting with # are considered comments in the env file and ignored.

    Examples:

    .. code-block:: yaml

        # Django settings module
        DJANGO_SETTINGS_MODULE=portfolio.settings

* Allow setting of alternate values by specifying  ``alt_value=VALUE`` in comments of the env file.

    For example, if you want to load the env vars from the .env file into a Heroku app running in production,
    you might want to use different values for some variables, than the ones in the .env file.

    Examples of allowed usages:

    I use a portfolio.env for my portfolio app running in Docker for local development.
    If I want the Heroku app to use a different value for ``DJANGO_SETTINGS_MODULE``, I would do something like this:

    .. code-block:: yaml

        # Django settings module alt_value=portfolio.prod_settings
        DJANGO_SETTINGS_MODULE=portfolio.settings

    OR

    .. code-block:: yaml

        # Django settings module
        # alt_value=portfolio.prod_settings
        DJANGO_SETTINGS_MODULE=portfolio.settings

    OR

    .. code-block:: yaml

        # alt_value=portfolio.prod_settings
        # Django settings module
        DJANGO_SETTINGS_MODULE=portfolio.settings

    NOTE: The ``alt_value`` needs to be on the line right before the actual env var you want to change.
    Also note that **anything** (except for trailing whitespace) specified after ``alt_value=`` is used as the alternate value, so be careful.

    Any of these methods above will force the tool to replace the value for ``DJANGO_SETTINGS_MODULE`` with
    ``portfolio.prod_settings`` instead of the actual ``portfolio.settings``, but only if you run with the option
    ``--set-alt`` like this:

    .. code-block:: bash

        $ heroku.env --app swimming-briskly-123 --env-file portfolio.env --set-alt

* Secure, does not store your API key anywhere.

    There are 3 ways of passing your API key:
        * setting it as an environment variable (recommended: set as ``HEROKU_API_KEY`` **before** running the tool)
        * entering it in a password prompt.
        * passing with ``--api-key`` or ``-k``

    If the API key is set as an environment variable, it will be automatically read first.
    **All other ways of setting it will be ignored.**

    If it is not set in any way, you will be given a password-type prompt to enter it.

    It is recommended for security purposes that you set it as an environment variable before running the tool, like this:

    .. code-block:: bash

        $ export HEROKU_API_KEY=a1b12c24-ab1d-123f-5678-1234b12a0a1b

    OR you can wait for the prompt.

    This is **not** recommended, but is still available as an option.

    .. code-block:: bash

        $ heroku.env --app swimming-briskly-123 --env-file dot.env --api-key a1b12c24-ab1d-123f-5678-1234b12a0a1b


See all options with:

.. code-block:: bash

    $ heroku.env --help


Credits
-------

* This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
* This is inspired by a script by `sdkcodes`_.
* **martyzz1**, for the `heroku3`_ API wrapper.
* `Click`_, for making writing CLI tools a complete pleasure.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _sdkcodes: https://github.com/sdkcodes/heroku-config
.. _here: https://dashboard.heroku.com/account
.. _this: https://devcenter.heroku.com/articles/authentication#retrieving-the-api-token
.. _Click: https://click.palletsprojects.com
.. _heroku3: https://github.com/martyzz1/heroku3.py
