from flask import Flask, render_template
from flask_babel import Babel
"""
Instantiate the Babel object in your app. 
Store it in a module-level variable named babel
"""

app = Flask(__name__)
babel = Babel(app)


class Config:
  """
  Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
  Use Config to set Babel’s default locale ("en") and timezone ("UTC")
  """
  LANGUAGES = ["en", "fr"]  # Available languages
  BABEL_DEFAULT_LOCALE = "en"  # Default locale
  BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone


if __name__ == '__main__':
  """__name__ must be equal to main to run app"""
  app.config.from_object(Config)
  app.run(debug=True)
