from fabric.decorators import task
from fabric.context_managers import settings
from fabric.api import require, env, local, abort, run as frun
from fabric.contrib.console import confirm
from fabric.colors import green, red



@task
def run():
    """
    Run development server
    """
    do('venv/bin/python3 app.py')


@task
def build():
    """
    Build basic application
    """
    do('[ -d venv ] || virtualenv venv --no-site-packages --python=python3')
    do('venv/bin/pip install --upgrade -r requirements.txt')
    do('venv/bin/python3 -c "from models import db; db.create_all()"')


def do(*args):
    """
    Runs command locally or remotely depending on whether a remote host has
    been specified and ask about continue on fail.
    """
    with settings(warn_only=True):
        if env.host_string:
            with settings(cd(config.remote_path)):
                result = frun(*args, capture=False)
        else:
            result = local(*args, capture=False)

    if result.failed:
        if result.stderr:
            print(red(result.stderr))
        if not confirm("Continue anyway?"):
            abort('Stopped execution per user request.')
