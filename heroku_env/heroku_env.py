# -*- coding: utf-8 -*-

"""Main module."""
from __future__ import unicode_literals  # unicode support for py2

import os

import click


def set_config_var(name, value, app_name):
    command = 'heroku config:set "{}={}" --app {}'.format(name, value, app_name)
    os.system(command)


def upload_env(app_name, env_file):
    with open(env_file) as e:
        for line in e:
            line = line.strip()
            # check, avoid comments
            if "=" in line and not line.startswith("#"):
                kv_pair = line.split("=", 1)
                if len(kv_pair) > 1:  # has to at least be of form: k=
                    key = kv_pair[0]
                    value = kv_pair[1]
                    # an empty value is fine
                    if key:
                        # set it
                        set_config_var(key, value, app_name)
            else:
                click.echo("Skipping line : either a comment or not of the form key=value")
