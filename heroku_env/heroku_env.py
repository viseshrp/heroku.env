# -*- coding: utf-8 -*-

"""Module containing the core functionality."""

from __future__ import unicode_literals  # unicode support for py2

import os

import click
import heroku3
import requests

from .exceptions import (
    HerokuRunError,
    InvalidHerokuAppError,
    InvalidAPIKeyError
)


def update_config_vars(config_dict, app):
    """
    Use the Heroku API to update config vars

    :param config_dict: dictionary of config vars
    :param app: name of the Heroku app
    :return: None
    """
    updated_config = app.update_config(config_dict)
    return updated_config.to_dict()


def upload_env(app_name, env_file, set_alt):
    """
    Get and upload env vars to Heroku

    :param app_name: The Heroku app.
    :param env_file: Path to the env file.
    :param set_alt: Flag to check if alternate values must be used.
    :return: None
    """
    try:
        # key error isn't expected here since the CLI tool
        # forces an API key before it reaches this point.
        heroku_conn = heroku3.from_key(os.environ['HEROKU_API_KEY'])
        app_instance = heroku_conn.apps()[app_name]
    except requests.exceptions.HTTPError:
        raise InvalidAPIKeyError("Please check your API key and try again.")
    except KeyError:
        raise InvalidHerokuAppError(
            "We could not find a Heroku app named {} registered with your API key".format(app_name))

    # init
    config_dict = {}
    use_alt = False
    alt_value = ''

    with open(env_file) as e:

        for line in e:
            line = line.strip()

            # check comments
            if line.startswith("#"):
                # enable --set-alt
                if set_alt and "alt_value=" in line:
                    alt_value = line.split("alt_value=", 1)[1]
                    if alt_value:
                        # use this value for the next env var
                        use_alt = True
                # any kind of comment warrants a skip
                continue

            # set env vars
            if "=" in line:
                kv_pair = line.split("=", 1)
                if len(kv_pair) > 1:  # has to at least be of form: k=
                    key = kv_pair[0]

                    if use_alt:
                        value = alt_value
                        # reset
                        use_alt = False
                    else:
                        value = kv_pair[1]

                    # an empty value is fine
                    if key:
                        config_dict[key] = value
                        # verify
                        click.secho(u'\u2713 ' + key, fg='green', bold=True)

            else:
                click.echo("Skipping line : Not of the form key=value")

    # update
    update_result = update_config_vars(config_dict, app_instance)

    if not update_result:
        raise HerokuRunError("Failed to update env vars. Possibly an error with Heroku."
                             " Please contact Heroku support.")

    click.echo("Config vars updated successfully.")
