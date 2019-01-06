# -*- coding: utf-8 -*-

"""Console script for heroku.env"""

# enable absolute imports of this module for Python2.x
from __future__ import absolute_import
from __future__ import unicode_literals  # unicode support for py2

import os

import click
import requests

from heroku_env import __version__
from .constants import (
    HEROKU_TROUBLESHOOT_URL,
    HEROKU_API_KEY_HELP_URL
)
from .exceptions import (
    HerokuRunError,
    InvalidHerokuAppError,
    InvalidAPIKeyError
)
from .heroku_env import upload_env
from .param_types import APIKeyParamType


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(__version__, '-v', '--version')
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
@click.option(
    '-t',
    '--set-alt',
    is_flag=True,
    required=False,
    help="Flag to enable reading of alternate values of env vars from"
         " comments in the env file."
         " Specify the alternate value to use with 'alt_value=VALUE'"
         " in the line right before the actual env var you want to change."
)
def main(app, env_file, api_key, set_alt):
    """
    Simple CLI tool to upload environment variables to
    Heroku from a .env file, through the Heroku API.

    It is recommended for security purposes that you set API
    key as an environment variable like this:

    export HEROKU_API_KEY=a1b12c24-ab1d-123f-5678-1234b12a0a1b

    Example usages:

    heroku.env --app swimming-briskly-123 --env-file dot.env

    heroku.env --app swimming-briskly-123 --env-file dot.env
    --api-key a1b12c24-ab1d-123f-5678-1234b12a0a1b
    """
    # if not defined, then set it.
    if not os.getenv('HEROKU_API_KEY'):
        os.environ['HEROKU_API_KEY'] = api_key
    try:
        upload_env(app, env_file, set_alt)
    except IndexError:
        raise click.ClickException("The entries in your .env file are not of the form KEY=VALUE")
    except HerokuRunError as e:
        # launch Heroku troubleshooting page for a failed run.
        click.launch(HEROKU_TROUBLESHOOT_URL)
        raise click.ClickException(e)
    except InvalidAPIKeyError as e:
        # launch API key doc
        click.launch(HEROKU_API_KEY_HELP_URL)
        raise click.ClickException(e)
    except (
        HerokuRunError,
        InvalidHerokuAppError
    ) as e:
        raise click.ClickException(e)
    except requests.exceptions.ConnectionError:
        raise click.ClickException("Please check your internet connection and try again.")
    except Exception as e:
        # all other exceptions
        click.echo(e)
        raise click.ClickException("An unknown error occurred. Please open an issue with the log.")


if __name__ == "__main__":
    main()  # pragma: no cover
