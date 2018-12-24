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
    # default="swimming-briskly-123",
    # show_default=True,
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
    # default="a1b12c24-ab1d-123f-5678-1234b12a0a1b",
    # show_default=True,
    help="Your Heroku API key"
)
def main(app, env_file, api_key):
    """Simple CLI tool to load Heroku environment variables from a .env file"""
    os.environ['HEROKU_API_KEY'] = api_key
    try:
        upload_env(app, env_file)
    except Exception as e:
        raise e
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
