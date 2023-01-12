"""
heroku_env.exceptions
-----------------------
All exceptions used in the heroku.env code base are defined here.
"""


class HerokuEnvException(Exception):
    """
    Base exception. All other exceptions
    inherit from here.
    """


class HerokuRunError(HerokuEnvException):
    """
    Exception raised when the Heroku command fails.
    """


class InvalidHerokuAppError(HerokuEnvException):
    """
    Exception raised when the given Heroku app is invalid
    """


class InvalidAPIKeyError(HerokuEnvException):
    """
    Raised when the provided Heroku API key is wrong
    """


class RateLimitExceededError(HerokuEnvException):
    """
    Raised when the Heroku API rate limit has exceeded
    """


class EnvFileNotFoundError(HerokuEnvException):
    """
    Raised when the specified env file path does not exist.
    We check manually instead of using click.Path because
    this is used for both upload and dump.
    """


class EnvFileNotWritableError(HerokuEnvException):
    """
    Raised when the specified env file does not have write perms.
    We check manually instead of using click.Path because
    this is used for both upload and dump.
    """
