from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

from passlib.context import CryptContext

# Password encryption context created
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)

db = SQLAlchemy()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[env or 'test'])
    api = Api(app, title='SportBud API', version='0.1.0')

    register_routes(api, app)
    db.init_app(app)

    migrate = Migrate(app, db, compare_type=True)

    @app.route('/health')
    def health():
        return jsonify('healthy')

    return app
