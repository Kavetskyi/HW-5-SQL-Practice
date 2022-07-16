import http
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from database import db
from models.models import Book, Author, BookAuthor
from serializers.serializers import BookSchema, AuthorSchema, BookAuthorSchema

book_router = Blueprint('book', __name__, url_prefix='/book')


@book_router.route('')
def book_get():
    book_schema = BookSchema()
    books = Book.query.order_by(Book.title)
    book_json = book_schema.dump(books, many=True)
    return jsonify(book_json)


@book_router.route('/<int:id_>')
def book_retrieve(id_):
    book_schema = BookSchema()
    book = Book.query.filter_by(id=id_).first()
    book_json = book_schema.dump(book)
    return jsonify(book_json)


@book_router.route('', methods=['POST'])
def book_create():
    data = request.get_json(force=True)
    book_schema = BookSchema()
    try:
        book_data = book_schema.load(data)
        new_book = Book(title=book_data['title'], author_id=book_data['author_id'])
        db.session.add(new_book)
        db.session.commit()
        new_book_json = book_schema.dump(new_book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_book_json


@book_router.route('/<int:id_>', methods=['PUT'])
def book_update(id_):
    data = request.get_json(force=True)
    book_schema = BookSchema()
    try:
        book_data = book_schema.load(data)
        upd_book = Book.query.filter_by(id=id_).first()
        upd_book.title = book_data['title']
        upd_book.author_id = book_data['author_id']
        db.session.commit()
        book_json = book_schema.dump(upd_book)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return book_json


@book_router.route('/<int:id_>', methods=['DELETE'])
def book_delete(id_):
    try:
        del_book = Book.query.filter_by(id=id_).first()
        db.session.delete(del_book)
        db.session.commit()
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return {}, http.HTTPStatus.NO_CONTENT


@book_router.route('/<int:id_>/change_author/<int:a_id_>', methods=['POST'])
def book_author(id_, a_id_):
    try:
        upd_book = Book.query.filter_by(id=id_).first()
        if author_book := Author.query.filter_by(id=a_id_).first():
            upd_book.author_id = author_book.id
            db.session.commit()
            book_schema = BookSchema()
            book_json = book_schema.dump(upd_book)
            return book_json, http.HTTPStatus.OK
        else:
            return {'Author not found'}, http.HTTPStatus.NOT_FOUND
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY
