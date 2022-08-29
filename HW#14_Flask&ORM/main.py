import http

from flask import Flask

from config import Config
from database import db
from user_api import user_router
from book_api import book_router


def create_app():
    app_ = Flask(__name__)
    app_.config.from_object(Config)
    db.init_app(app_)
    app_.register_blueprint(user_router)
    app_.register_blueprint(book_router)
    return app_


def setup_db(app_):
    with app_.app_context():
        db.create_all()
        db.session.commit()


if __name__ == '__main__':
    app = create_app()
    setup_db(app)
    app.run(host="0.0.0.0")
