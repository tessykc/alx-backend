#!/usr/bin/env python3
"""
Infer appropriate time zone
"""

from flask import current_app, request
from pytz import timezone, UnknownTimeZoneError
from flask_babel import Babel


@babel.timezoneselector
def get_timezone():
    """Gets the user's preferred time zone or defaults to UTC.

    Returns:
        str: The chosen time zone or 'UTC'.
    """

    user = getattr(g, 'user', None)  # Check for logged-in user

    # 1. Time zone from user settings (if valid)
    if user and user.get('timezone') and validate_timezone(user['timezone']):
        return user['timezone']

    # 2. Time zone from URL parameter (if valid)
    timezone_from_url = request.args.get('timezone')
    if timezone_from_url and validate_timezone(timezone_from_url):
        return timezone_from_url

    # 3. Default time zone
    return 'UTC'


def validate_timezone(timezone_str):
    """Validates a time zone string using pytz.

    Args:
        timezone_str (str): The time zone string to validate.

    Returns:
        bool: True if the time zone is valid, False otherwise.
    """

    try:
        timezone(timezone_str)
        return True
    except UnknownTimeZoneError:
        return False

