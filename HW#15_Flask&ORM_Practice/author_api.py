import http
from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from database import db
from models.models import Author
from serializers.serializers import AuthorSchema

author_router = Blueprint('author', __name__, url_prefix='/author')


@author_router.route('')
def author_get():
    a_schema = AuthorSchema()
    authors = Author.query.order_by(Author.flname)
    a_json = a_schema.dump(authors, many=True)
    return jsonify(a_json)


@author_router.route('/<int:id_>')
def author_retrieve(id_):
    a_schema = AuthorSchema()
    author = Author.query.filter_by(id=id_).first()
    a_json = a_schema.dump(author)
    return jsonify(a_json)


@author_router.route('', methods=['POST'])
def author_create():
    data = request.get_json(force=True)
    a_schema = AuthorSchema()
    try:
        a_data = a_schema.load(data)
        new_author = Author(flname=a_data['flname'])
        db.session.add(new_author)
        db.session.commit()
        new_a_json = a_schema.dump(new_author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return new_a_json


@author_router.route('/<int:id_>', methods=['PUT'])
def author_update(id_):
    data = request.get_json(force=True)
    a_schema = AuthorSchema()
    try:
        a_data = a_schema.load(data)
        upd_author = Author.query.filter_by(id=id_).first()
        upd_author.flname = a_data['flname']
        db.session.commit()
        a_json = a_schema.dump(upd_author)
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return a_json


@author_router.route('/<int:id_>', methods=['DELETE'])
def author_delete(id_):
    try:
        del_author = Author.query.filter_by(id=id_).first()
        db.session.delete(del_author)
        db.session.commit()
    except ValidationError as e:
        return {'errors': e.messages}, http.HTTPStatus.UNPROCESSABLE_ENTITY

    return {}, http.HTTPStatus.NO_CONTENT
