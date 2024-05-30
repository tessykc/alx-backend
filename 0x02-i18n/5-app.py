#!/usr/bin/env python3

from flask import g, before_request

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves the login_as parameter from the URL query string
    """
    user_id = flask.request.arhs.get('login_as')
    if user_id and User_id.isdigit():
        try:
            return users[int(user_id)]
        except KeyError:
            pass
    return None


@before_request
def before_request():
    """Uses the decorator to ensure it runs before every 
    request to the flask app"""
    g.user = get_user()
