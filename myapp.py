# myapp.py
import os
from flask import Flask, jsonify, render_template, url_for, abort
from dotenv import load_dotenv
import contentful


def create_contentful(SPACE_ID, DELIVERY_API_KEY):
    """Connect to contentful"""
    CLIENT = contentful.Client(
        SPACE_ID,
        DELIVERY_API_KEY)

    return CLIENT


def create_app(SPACE_ID, DELIVERY_API_KEY):
    """Create flask app"""
    client = create_contentful(SPACE_ID, DELIVERY_API_KEY)
    app = Flask(__name__)

    @app.route('/')
    @app.route('/home')
    def index():
        """index route. Gathers page from contentful and builds website."""
        heroes = client.entries({'content_type': 'post'})
        return render_template("index.html", heroes=heroes)

    @app.route('/ping')
    def ping():
        return jsonify(ping='pong')

    return app

if __name__ == '__main__':
    load_dotenv()

    SPACE_ID = os.getenv('SPACE_ID')
    DELIVERY_API_KEY = os.getenv('DELIVERY_API_KEY')

    app = create_app(SPACE_ID, DELIVERY_API_KEY)
    app.run(port=5000)
