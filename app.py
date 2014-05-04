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
@app.route('/book/view/<int:book_id>', methods=['GET','POST'])
def book_view(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('books/view.html', **locals())


@app.route('/book/add/', methods=['GET', 'POST'])
def book_add():
    form = BookForm(request.form)
    form.authors.choices = [(a.id, a.title) for a in Author.query.all()]

    if request.method == "POST" and form.validate():
        # Add book
        pass
        # return redirect(url_for('book_view', book_id=book.id))

    return render_template('books/add.html', **locals())


# Authors
@app.route('/author/view/<int:author_id>', methods=['GET'])
def author_view(author_id):
    author = Author.query.get_or_404(author_id)
    return render_template('authors/view.html', **locals())


@app.route('/author/add/', methods=['GET', 'POST'])
def author_add():
    form = AuthorForm(request.form)

    if request.method == "POST" and form.validate():
        new_author = Author(title=form.data.get('title'))
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('author_view', author_id=new_author.id))

    return render_template('authors/add.html', **locals())
