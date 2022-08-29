from flask import Flask
from config import Config
from core.database import db
from auth.view import auth_router
from event.view import event_router
from user.view import user_router


def create_app():
    app_ = Flask(__name__)
    app_.config.from_object(Config)

    db.init_app(app_)
    app_.register_blueprint(auth_router)
    app_.register_blueprint(user_router)
    app_.register_blueprint(event_router)
    return app_


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
