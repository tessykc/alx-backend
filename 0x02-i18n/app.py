#!/usr/bin/env python3
"""
Display the current time
"""

from datetime import datetime
from pytz import timezone, utc


def get_current_time():
    """Gets the current time in UTC."""
    return datetime.utcnow()


def format_current_time(timezone_str):
    """Formats the current UTC time in the specified time zone.

    Args:
        timezone_str (str): The time zone string (e.g., 'UTC', 'America/Los_Angeles').

    Returns:
        str: The formatted current time string.
    """

    try:
        # Convert current UTC time to the specified time zone
        current_time = utc.localize(get_current_time())
        localized_time = current_time.astimezone(timezone(timezone_str))
        # Use strftime for format customization (adjust format as needed)
        return localized_time.strftime("%b %d, %Y, %I:%M:%S %p")
    except UnknownTimeZoneError:
        return "Invalid Time Zone"  # Handle invalid time zones
