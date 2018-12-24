from __future__ import unicode_literals  # unicode support for py2

import re

import click


class APIKeyParamType(click.ParamType):
    """
    Custom ParamType for API key input cleaning and validation
    """
    name = 'API Key Param Type'

    def convert(self, value, param, ctx):
        is_valid = re.match(r'[0-9a-f]{36}', value)

        if not is_valid:
            self.fail('Your API Key has to be a 36-character hexadecimal string', param, ctx)
