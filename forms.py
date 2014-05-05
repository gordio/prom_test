from wtforms import Form, TextField, SelectMultipleField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from models import Author


class BookForm(Form):
    title = TextField('Title', [
        validators.Required(),
        validators.Length(min=4, max=200)
    ])
    authors = QuerySelectMultipleField('Authors', [
        validators.Required(),
    ], query_factory=lambda:Author.query.all())
    # authors = SelectMultipleField(
    #     'Authors',
    #     [
    #         validators.Required(),
    #     ],
    #     choices=[('0', 'Empty')]
    # )


class AuthorForm(Form):
    name = TextField('Name', [
        validators.Required(),
        validators.Length(min=4, max=200)
    ])
