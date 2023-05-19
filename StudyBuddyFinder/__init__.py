from flask import Flask
import secrets

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_urlsafe(32)

    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    from .views.home_view import home_bp
    app.register_blueprint(home_bp)

    from .views.auth_views import auth_bp
    app.register_blueprint(auth_bp)