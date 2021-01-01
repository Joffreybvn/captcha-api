
from flask import Flask
from src.api import v1


class Api:
    """Initialize a Flask application."""

    def __init__(self):

        # Initialize the Flask server
        self.app = Flask(__name__)

        # Load the blueprints
        self.app.register_blueprint(v1.blueprint, url_prefix='/v1')

    def run(self, ip, port=3000, debug=False, threaded=False):
        """Run the Flask app."""

        self.app.run(ip, port=port, debug=debug, threaded=threaded)
