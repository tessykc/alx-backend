#!/usr/bin/env python3
"""
setting up a basic Flask app
"""

"""Importing flask from Flask"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  """The function that links to the template file"""
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
