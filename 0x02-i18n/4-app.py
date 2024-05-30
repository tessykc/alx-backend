#!/usr/bin/env python3

from flask import current_app, request


def get_locale(supported_locales=("en", "fr")):
    """Gets the current locale based on URL parameter or default.

    Args:
        supported_locales (tuple, optional): A tuple of supported locale codes.
            Defaults to ("en", "fr").

    Returns:
        str: The chosen locale or the default locale.

    Raises:
        ValueError: If an unsupported locale is provided.
    """

    # Get the current request object
    request = current_app.request

    # Check if the 'locale' parameter exists in the URL query string
    if request.args.get('locale'):
        # Get the value of the 'locale' parameter
        locale = request.args.get('locale')

        # Check if the provided locale is supported
        if locale.lower() not in supported_locales:
            raise ValueError(f"Unsupported locale: {locale}")

        return locale.lower()  # Ensure lowercase locale code

    # If parameter is missing or not supported, return the default locale
    return supported_locales[0]  # Return the first supported locale by default

