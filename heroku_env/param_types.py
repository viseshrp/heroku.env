import re

import click


class APIKeyParamType(click.ParamType):
    """
    Custom ParamType for API key input cleaning and validation
    """

    name = "API Key Param Type"

    def convert(self, value, param, ctx):
        cleaned_value = value.strip()
        is_valid = re.match(r"[0-9-a-f]{36}", cleaned_value)

        if not is_valid:
            self.fail(
                "Your API Key has to be a 36-character hexadecimal string", param, ctx
            )

        return cleaned_value
