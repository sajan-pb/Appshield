from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = "auth.login"

    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)
    @app.route("/")
    def home():
        return """
        <h1>AppShield</h1>
        <a href='/register'>Register</a><br>
        <a href='/login'>Login</a>
        """
    @app.route("/dashboard")
    @login_required
    def dashboard():
        return render_template("dashboard.html")

    with app.app_context():
        db.create_all()

    return app