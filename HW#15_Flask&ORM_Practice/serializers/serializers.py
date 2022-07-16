from marshmallow import Schema, fields
from marshmallow.validate import Length


class BookSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    title = fields.String(required=True)
    author_id = fields.Integer(required=False)
    authors = fields.Nested(lambda: AuthorSchema(only=["flname"]))


class AuthorSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    flname = fields.String(required=True)
    books = fields.List(fields.Nested(BookSchema()))


class BookAuthorSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    book_id = fields.Integer(required=False)
    books = fields.Nested(BookSchema(only=["title"]))
    author_id = fields.Integer(required=False)
    authors = fields.Nested(AuthorSchema(only=["flname"]))
