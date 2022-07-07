from database import db
from models.book import Book

if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    db.session.add(Book(title="A very interesting book.", writer="John Smith"))
    db.session.commit()
    print("created tables")