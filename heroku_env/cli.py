# -*- coding: utf-8 -*-

"""Console script for heroku.env"""

from __future__ import unicode_literals  # unicode support for py2

import os
import sys

import click

from .heroku_env import upload_env
from .param_types import APIKeyParamType


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
    type=click.Path(exists=True, file_okay=True, dir_okay=False,
                    readable=True, resolve_path=True, allow_dash=False),
    default=".env",
    show_default=True,
    help="Path to the .env file"
)
@click.option(
    '-k',
    '--api-key',
    prompt="Please enter the Heroku API key to continue",
    hide_input=True,
    confirmation_prompt=True,
    required=True,
    type=APIKeyParamType(),
    envvar="HEROKU_API_KEY",
    help="Your Heroku API key"
)
def main(app, env_file, api_key):
    """
    Simple CLI tool to upload environment variables to Heroku from a .env file,
    through the Heroku CLI Toolbelt.

    It is recommended for security purposes that you set API key as an environment variable like this:

    export HEROKU_API_KEY=a1b12c24-ab1d-123f-5678-1234b12a0a1b

    Example usages:

    heroku.env --app swimming-briskly-123 --env-file dot.env

    heroku.env --app swimming-briskly-123 --env-file dot.env --api-key a1b12c24-ab1d-123f-5678-1234b12a0a1b
    """
    # if not defined, then set it.
    if not os.getenv('HEROKU_API_KEY'):
        os.environ['HEROKU_API_KEY'] = api_key
    try:
        upload_env(app, env_file)
    except Exception as e:
        raise click.ClickException(e)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
