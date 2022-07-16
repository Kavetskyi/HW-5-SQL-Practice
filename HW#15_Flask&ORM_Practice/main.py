from flask import Flask
from config import Config
from database import db
from book_api import book_router
from author_api import author_router
from book_author_api import ba_router


def create_app():
    app_ = Flask(__name__)
    app_.config.from_object(Config)

    db.init_app(app_)
    app_.register_blueprint(book_router)
    app_.register_blueprint(author_router)
    app_.register_blueprint(ba_router)
    return app_


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
