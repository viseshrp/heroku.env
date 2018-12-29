# -*- coding: utf-8 -*-

"""Main module."""
from __future__ import unicode_literals  # unicode support for py2

import os

import click


def set_config_var(name, value, app_name):
    command = 'heroku config:set "{}={}" --app {}'.format(name, value, app_name)
    os.system(command)


def upload_env(app_name, env_file, set_alt):
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
                        use_alt = False
                    else:
                        value = kv_pair[1]

                    # an empty value is fine
                    if key:
                        set_config_var(key, value, app_name)
            else:
                click.echo("Skipping line : Not of the form key=value")
