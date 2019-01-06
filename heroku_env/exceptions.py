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
