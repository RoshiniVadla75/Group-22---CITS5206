from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from models import db, User
from routes import main

login_manager = LoginManager()
migrate = Migrate()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(
        __name__,
        template_folder="app/templates",
        static_folder="app/static",
    )

    # -------------------------
    # CONFIG
    # -------------------------
    app.config["SECRET_KEY"] = "dev"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ai_museum.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # -------------------------
    # INIT EXTENSIONS
    # -------------------------
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = "main.login"
    login_manager.login_message_category = "warning"

    # -------------------------
    # REGISTER ROUTES
    # -------------------------
    app.register_blueprint(main)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)