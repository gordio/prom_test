from flask import Flask, g, render_template, flash, redirect, session, request, url_for, abort


app = Flask(__name__, static_url_path='')
app.config.from_pyfile('config.py')


from models import db, Book, Author
from forms import AuthorForm, BookForm


# ERRORS
if not app.config['DEBUG']:
    @app.errorhandler(404)
    def page_not_found(error):
        return 'This page does not exist', 404

    @app.errorhandler(500)
    def page_not_found(error):
        return 'Server error', 500


# VIEWS
@app.route('/')
def index():
    form = BookForm()
    return render_template('index.html', **locals())


# Books
@app.route('/books/view/all', methods=['GET'])
@app.route('/books/', methods=['GET'])
def books_view_all():
    books = Book.query.all()
    return render_template('books/view_all.html', **locals())


@app.route('/books/add/', methods=['GET', 'POST'])
def books_add():
    form = BookForm(request.form)

    if request.method == "POST" and form.validate():
        new_book = Book(title=form.data.get('title'))
        new_book.authors = form.data.get('authors')
        db.session.add(new_book)
        db.session.commit()
        flash("Book added")
        return redirect(url_for('books_view_all'))

    return render_template('books/add.html', **locals())


@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def books_edit(book_id):
    book = Book.query.get_or_404(book_id)
    form = BookForm(request.form, obj=book)

    if request.method == "POST" and form.validate():
        book.title = form.data.get('title')
        db.session.commit()
        flash("Book changed")
        return redirect(url_for('books_view_all'))

    return render_template('books/edit.html', **locals())


@app.route('/books/delete/<int:book_id>', methods=['GET', 'POST'])
def books_delete(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == "POST":
        db.session.delete(book)
        db.session.commit()
        flash("Book deleted")
        return redirect(url_for('books_view_all'))

    return render_template('books/delete.html', **locals())


# Authors
@app.route('/authors/view/all', methods=['GET'])
@app.route('/authors/', methods=['GET'])
def authors_view_all():
    authors = Author.query.all()
    return render_template('authors/view_all.html', **locals())


@app.route('/authors/add/', methods=['GET', 'POST'])
def authors_add():
    form = AuthorForm(request.form)

    if request.method == "POST" and form.validate():
        new_author = Author(name=form.data.get('name'))
        db.session.add(new_author)
        db.session.commit()
        flash("Author added")
        return redirect(url_for('authors_view_all'))

    return render_template('authors/add.html', **locals())


@app.route('/authors/edit/<int:author_id>', methods=['GET', 'POST'])
def authors_edit(author_id):
    author = Author.query.get_or_404(author_id)

    form = AuthorForm(request.form, obj=author)

    if request.method == "POST" and form.validate():
        author.name = form.data.get('name')
        db.session.commit()
        flash("Author changed")
        return redirect(url_for('authors_view_all'))

    return render_template('authors/edit.html', **locals())


@app.route('/authors/delete/<int:author_id>', methods=['GET', 'POST'])
def authors_delete(author_id):
    author = Author.query.get_or_404(author_id)

    if request.method == "POST":
        db.session.delete(author)
        db.session.commit()
        flash("Author deleted")
        return redirect(url_for('authors_view_all'))

    return render_template('authors/delete.html', **locals())
