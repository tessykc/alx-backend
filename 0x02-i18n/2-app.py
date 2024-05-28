from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
  """Selects the best locale based on user preferences and supported languages."""
  supported_languages = app.config['LANGUAGES']
  return request.accept_languages.best_match(supported_languages)

# ... rest of your application code
