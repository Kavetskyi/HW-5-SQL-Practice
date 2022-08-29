from database import db


class BookAuthor(db.Model):
    __tablename__ = 'book_author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    books = db.relationship('Book')
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    authors = db.relationship('Author')


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    authors = db.relationship('Author', secondary='book_author')


class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flname = db.Column(db.String(400), nullable=False)
    books = db.relationship('Book', secondary='book_author')


""" many to many relation Book -> BookAuthor -> Author """


# class BookAuthor(db.Model):
#     __tablename__ = 'book_author'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
#
#
# class Book2(db.Model):
#     __tablename__ = 'book'
#     __table_args__ = {'extend_existing': True}
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(500), nullable=False)
#     b_authors = db.relationship('Author2', secondary='book_author', back_populates='a_books')
#
#
# class Author2(db.Model):
#     __tablename__ = 'author'
#     __table_args__ = {'extend_existing': True}
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     flname = db.Column(db.String(400), nullable=False)
#     a_books = db.relationship('Book2', secondary='book_author', back_populates='b_authors')
