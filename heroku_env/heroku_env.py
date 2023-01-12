"""Module containing the core functionality."""
import os

import click
import heroku3

from .exceptions import (
    HerokuRunError,
    InvalidHerokuAppError,
    InvalidAPIKeyError,
    RateLimitExceededError,
    EnvFileNotFoundError,
    EnvFileNotWritableError,
    EnvFileEmptyError,
)


def raise_for_rate_limit(heroku_conn):
    """
    Check and raise if Heroku API rate limit has exceeded

    :param heroku_conn: Heroku connection object
    :return: None
    """
    if heroku_conn.ratelimit_remaining() < 1:
        raise RateLimitExceededError(
            "Your API key has reached the maximum number of calls to Heroku."
            " Please try later."
        )


def get_heroku_app(app_name):
    """
    Get Heroku configuration

    :param app_name: The Heroku app.
    :returns Heroku connection and app instance
    """
    try:
        # key error isn't expected here since the CLI tool
        # forces an API key before it reaches this point.
        heroku_conn = heroku3.from_key(os.environ["HEROKU_API_KEY"])

        # check and fail early
        if not heroku_conn.is_authenticated:
            raise InvalidAPIKeyError("Please check your API key and try again.")

        # get app
        app_instance = heroku_conn.apps()[app_name]
    except KeyError:
        raise InvalidHerokuAppError(
            f"We could not find a Heroku app named {app_name} registered with your API key."
        )

    # check rate limit before hitting API
    raise_for_rate_limit(heroku_conn)

    return app_instance


def write_env(env_dict, env_file):
    """
    Write config vars to file

    :param env_dict: dict of config vars
    :param env_file: output file
    :return: was the write successful?
    """
    content = [f"{k}={v}" for k, v in env_dict.items()]

    written = True
    try:
        with open(env_file, "w") as file:
            file.write("\n".join(content))
    except IOError:
        written = False

    return written


def dump_env(app_name, env_file):
    """
    Get and dump env vars from Heroku

    :param app_name: The Heroku app.
    :param env_file: Path to the env file.
    :return: None
    """
    # check for write perms only if file already exists,
    # otherwise we create one
    if os.path.exists(env_file) and not os.access(env_file, os.W_OK):
        raise EnvFileNotWritableError(
            f"File {env_file} does not have write permissions."
        )

    app_instance = get_heroku_app(app_name)

    if write_env(app_instance.config().to_dict(), env_file):
        click.echo(f"Config vars dumped successfully at {env_file}.")
    else:
        click.echo("Config vars dump failed. Please try again.")


def update_config_vars(config_dict, app):
    """
    Use the Heroku API to update config vars

    :param config_dict: dictionary of config vars
    :param app: name of the Heroku app
    :return: None
    """
    updated_config = app.update_config(config_dict)
    return updated_config.to_dict()


def read_env(env_file, set_alt):
    """
    Read config vars from file

    :param env_file: output file
    :param set_alt: Flag to check if alternate values must be used.
    :return: dict of read config vars
    """
    # init
    config_dict = {}
    use_alt = False
    alt_value = None

    with open(env_file) as e:

        for line in e:
            line = line.strip()
            if line:
                # check comments
                if line.startswith("#"):
                    # enable --set-alt
                    if set_alt and "alt_value=" in line:
                        alt_value = line.split("alt_value=", 1)[1]
                        if alt_value is not None:
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
                            if alt_value == "":
                                # skip the value if it's an empty string
                                continue
                            elif alt_value == "-":
                                # set to None if alt_value is '-'
                                # this allows removal of a config var.
                                value = None
                            else:
                                value = alt_value

                            # reset
                            use_alt = False
                        else:
                            value = kv_pair[1]

                        # finally, set to config dict
                        # an empty value is fine but obviously not an empty key.
                        if key:
                            config_dict[key] = value
                            # confirm
                            click.secho("\u2713 " + key, fg="green", bold=True)

                else:
                    click.echo("Skipping line : Not of the form key=value.")

    return config_dict


def upload_env(app_name, env_file, set_alt):
    """
    Get and upload env vars to Heroku

    :param app_name: The Heroku app.
    :param env_file: Path to the env file.
    :param set_alt: Flag to check if alternate values must be used.
    :return: None
    """
    if not os.path.exists(env_file):
        raise EnvFileNotFoundError(f"File {env_file} does not exist.")

    # read
    config_dict = read_env(env_file, set_alt)

    if config_dict:
        # update
        app_instance = get_heroku_app(app_name)
        update_result = update_config_vars(config_dict, app_instance)
    else:
        raise EnvFileEmptyError(f"No env/config vars were found in file {env_file}.")

    if not update_result:
        raise HerokuRunError(
            "Failed to update env vars. Possibly an error with Heroku."
            " Please try again or contact Heroku support."
        )

    click.echo("Config vars updated successfully.")
