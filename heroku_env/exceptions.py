# -*- coding: utf-8 -*-

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


class HerokuNotFoundException(HerokuEnvException):
    """
    Exception raised when Heroku is not installed.
    """


class FailedHerokuRunException(HerokuEnvException):
    """
    Exception raised when the Heroku command fails.
    """
