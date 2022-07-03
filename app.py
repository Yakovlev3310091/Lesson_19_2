from flask import Flask
from flask_restx import Api

from config import Config
from lesson19_project_hard_source.views.user import user_ns
from lesson19_project_hard_source.setup_db import db
from lesson19_project_hard_source.views.directors import director_ns
from lesson19_project_hard_source.views.genres import genre_ns
from lesson19_project_hard_source.views.movies import movie_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
