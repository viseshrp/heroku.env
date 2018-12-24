# -*- coding: utf-8 -*-

"""Main module."""

import os


def split_line(line):
    return line.strip().split("=", 1)


def set_config_var(name, value, app_name):
    if name and value:
        command = 'heroku config:set "' + name + '=' + value + '"' + ' --app ' + app_name
        os.system(command)


def upload_env(app_name, env_file):
    with open(env_file) as e:
        for line in e:
            # avoid comments
            if not line.startswith("#"):
                cleaned_line = split_line(line)
                if len(cleaned_line) > 1:
                    name = cleaned_line[0]
                    try:
                        value = cleaned_line[1]
                    except IndexError:
                        # sometimes we upload empty values for vars which is totally fine.
                        value = ""
                    # log it
                    print("*** Setting " + name + " = " + value + " ***")
                    # set it
                    set_config_var(name, value, app_name)
