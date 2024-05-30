#!/usr/bin/env python3
"""Prioritize user locale and integrate it 
with existing mock login functionality"""

from flask import current_app, request


def get_locale(supported_locales=("en", "fr")):
    """Gets the current locale based on user preference, URL parameter, or default.

    Args:
        supported_locales (tuple, optional): A tuple of supported locale codes.
            Defaults to ("en", "fr").

    Returns:
        str: The chosen locale or the default locale.
    """

    user = getattr(g, 'user', None)  # Check for logged-in user

    # 1. User locale (if logged in and has a locale)
    if user and user.get('locale') in supported_locales:
        return user['locale']

    # 2. Locale from URL parameter
    locale_from_url = request.args.get('locale')
    if locale_from_url and locale_from_url.lower() in supported_locales:
        return locale_from_url.lower()

    # 3. Locale from request header (optional)
    # Implement logic to extract locale from headers (e.g., 'Accept-Language')
    # if request.headers.get('Accept-Language'):
    #     # ... (extract and validate locale from header)
    #     return extracted_locale

    # 4. Default locale
    return supported_locales[0]
