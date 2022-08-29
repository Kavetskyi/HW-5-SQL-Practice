import http
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from database import db
from models.models import Book, Author, BookAuthor
from serializers.serializers import BookSchema, AuthorSchema, BookAuthorSchema

ba_router = Blueprint('book_author', __name__, url_prefix='/book/author')


@ba_router.route('')
def ba_get():
    ba_schema = BookAuthorSchema()
    books_authors = BookAuthor.query.order_by(BookAuthor.id)
    ba_json = ba_schema.dump(books_authors, many=True)
    return jsonify(ba_json)


@ba_router.route('/<int:id_>')
def ba_retrieve(id_):
    ba_schema = BookAuthorSchema()
    books_authors = BookAuthor.query.filter_by(id=id_).first()
    ba_json = ba_schema.dump(books_authors)
    return jsonify(ba_json)


@ba_router.route('', methods=['POST'])
def ba_create():
    data = request.get_json(force=True)
    ba_schema = BookAuthorSchema()
    try:
        ba_data = ba_schema.load(data)
        new_ba = BookAuthor(book_id=ba_data['book_id'], author_id=ba_data['author_id'])
        db.session.add(new_ba)
        db.session.commit()
        new_ba_json = ba_schema.dump(new_ba)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_ba_json


@ba_router.route('/<int:id_>', methods=['PUT'])
def ba_update(id_):
    data = request.get_json(force=True)
    ba_schema = BookAuthorSchema()
    try:
        ba_data = ba_schema.load(data)
        upd_ba = BookAuthor.query.filter_by(id=id_).first()
        upd_ba.book_id = ba_data['book_id']
        upd_ba.author_id = ba_data['author_id']
        db.session.commit()
        ba_json = ba_schema.dump(upd_ba)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return ba_json


@ba_router.route('/<int:id_>', methods=['DELETE'])
def ba_delete(id_):
    try:
        del_ba = BookAuthor.query.filter_by(id=id_).first()
        db.session.delete(del_ba)
        db.session.commit()
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return {}, http.HTTPStatus.NO_CONTENT
