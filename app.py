from flask import Flask
from models import db
from routes import main


def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ai_museum.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialise database
    db.init_app(app)

    # Register routes blueprint
    app.register_blueprint(main)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)