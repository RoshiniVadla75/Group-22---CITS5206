from flask import Flask
from models import db
from routes import main


def create_app():
    app = Flask(__name__)


    app.config["SECRET_KEY"] = "dev"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ai_museum.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)