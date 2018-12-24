# -*- coding: utf-8 -*-

"""Console script for heroku_env."""

from __future__ import unicode_literals  # unicode support for py2

import os
import sys
import click
from .heroku_env import upload_env


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option(
    '-a',
    '--app',
    required=True,
    type=str,
    help="The name of the heroku app."
)
@click.option(
    '-e',
    '--env-file',
    type=str,
    default=".env",
    show_default=True,
    help="Path to the .env file"
)
@click.option(
    '-k',
    '--api-key',
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    required=True,
    type=str,
    help="Your Heroku API key"
)
def main(app, env_file, api_key):
    """
    Simple CLI tool to upload environment variables to Heroku from a .env file.

    Requirements:

    1. Python 2.7+

    2. Heroku CLI installed.

    3. A valid Heroku app name is required to run against.

    4. The absolute path to the .env file is also needed, but if not provided,
    ".env" will be used as the default, which expects a file named .env to be present
    in the current working directory.

    5. Your Heroku API key is also mandatory, which can be set as an environment
    variable(as HEROKU_API_KEY) or passed with --api-key or -k.

    If not set, you will be given a password-type prompt to enter it.

    It is recommended for security purposes that you set it as an environment variable like this:

    export HEROKU_API_KEY=a1b12c24-ab1d-123f-5678-1234b12a0a1b

    Example usages:

    heroku.env --app swimming-briskly-123 --env-file dot.env

    heroku.env --app swimming-briskly-123 --env-file dot.env --api-key a1b12c24-ab1d-123f-5678-1234b12a0a1b
    """
    os.environ['HEROKU_API_KEY'] = api_key
    try:
        upload_env(app, env_file)
    except Exception as e:
        raise e
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
