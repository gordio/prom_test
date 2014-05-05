import os
from flask import Flask, g, render_template, flash, redirect, session, request, url_for, abort
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restless


app = Flask(__name__, static_url_path='')


# CONFIG
###############################################################################
_PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__)).replace('\\', '/')

app.config['SECRET_KEY'] = "random.get()"

# Auto switch to debug?
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + _PROJECT_ROOT + "/data.sqlite3"


db = SQLAlchemy(app)


# MODELS
###############################################################################
books_authors = db.Table(
    'books_authors',
    db.Model.metadata,
    db.Column('author_id', db.Integer, db.ForeignKey('author.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), unique=True)
    authors = db.relationship(
        'Author',
        secondary=books_authors,
        backref=db.backref('books', lazy='dynamic')
    )


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)


# REST
###############################################################################
# Create the Flask-Restless API manager.
restless_manager = restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
restless_manager.create_api(Author, methods=['GET', 'POST', 'DELETE'])
restless_manager.create_api(Book, methods=['GET', 'POST', 'DELETE'])


# VIEWS
###############################################################################
@app.route('/')
def index():
    return render_template('index.html', **locals())


if __name__ == "__main__":
    app.run()
