# -*- coding: utf-8 -*-

"""Module containing the core functionality."""

from __future__ import unicode_literals  # unicode support for py2

import sys
import subprocess

import click

from .constants import (
    EXIT_CODE_COMMAND_NOT_FOUND,
    EXIT_CODE_SUCCESS,
    HEROKU_INSTALL_URL,
    HEROKU_TROUBLESHOOT_URL,
    SUBPROCESS_WAIT_TIMEOUT
)
from .exceptions import HerokuNotFoundException, FailedHerokuRunException


def set_config_var(key, value, app_name):
    """
    Run Heroku Toolbelt to set vars.

    :param key: Env Key
    :param value: Env value
    :param app_name: The Heroku app
    :return: exit code of execution
    """
    command = ['heroku', 'config:set', '"{}={}"'.format(key, value), '--app', app_name]

    # run subprocess, returns exit code
    return subprocess.Popen(
        command,
        shell=False,
    ).wait(timeout=SUBPROCESS_WAIT_TIMEOUT)


def upload_env(app_name, env_file, set_alt):
    """
    Get and upload env vars to Heroku

    :param app_name: The Heroku app.
    :param env_file: Path to the env file.
    :param set_alt: Flag to check if alternate values must be used.
    :return: None
    """
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
                else:
                    click.echo("Skipping comment...")
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
                        exit_code = set_config_var(key, value, app_name)
                        # check command exit code
                        if exit_code != EXIT_CODE_SUCCESS:
                            if exit_code == EXIT_CODE_COMMAND_NOT_FOUND:
                                # launch install url in web browser
                                click.launch(HEROKU_INSTALL_URL)
                                # raise
                                raise HerokuNotFoundException("Heroku CLI is missing on your system."
                                                              " Please install it before proceeding.")
                            # default failed run
                            click.launch(HEROKU_TROUBLESHOOT_URL)
                            raise FailedHerokuRunException("Running of the Heroku CLI failed."
                                                           " Please check your arguments and try again.")

            else:
                click.echo("Skipping line : Not of the form key=value")
