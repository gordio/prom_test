from flask import Flask, g, render_template, flash, redirect, session, request,\
    url_for, abort


app = Flask(__name__, static_url_path='')
app.config.from_pyfile('config.py')


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
    return render_template('index.html', **locals())
