import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api

from db import db
from middleware.authentication import JWTManager
from middleware.blocklist import BLOCKLIST
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint


def create_app(db_uri=None):
    load_dotenv()
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Store API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    # SQLAlchemy setup
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Migrate setup
    migrate = Migrate(app, db)

    # JWT setup
    app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]
    jwt = JWTManager(app)

    # Registering blueprints
    api = Api(app)

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    return app
