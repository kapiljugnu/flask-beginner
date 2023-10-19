from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///project.db',
        SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from .db import app_db
    app_db.init_app(app)

    import flaskr.models  # importing it here for migration otherwise it will not detect
    from flask_migrate import Migrate
    Migrate(app, app_db)

    from .routes import register_blueprint
    register_blueprint(app)

    return app
