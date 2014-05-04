from wtforms import Form, TextField, SelectMultipleField, validators

class BookForm(Form):
    title = TextField('Title', [
        validators.Required(),
        validators.Length(min=4, max=200)
    ])
    authors = SelectMultipleField(
        'Authors',
        [
            validators.Required(),
        ],
        choices=[('0', 'Empty')]
    )


class AuthorForm(Form):
    title = TextField('Title', [
        validators.Required(),
        validators.Length(min=4, max=200)
    ])
