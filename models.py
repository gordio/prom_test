from flask.ext.sqlalchemy import SQLAlchemy
from app import app


db = SQLAlchemy(app)

books_authors = db.Table(
    'books_authors',
    db.Model.metadata,
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'))
)


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=True)
    authors = db.relationship(
        'Author',
        secondary=books_authors,
        backref=db.backref('books', lazy='dynamic')
    )

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
