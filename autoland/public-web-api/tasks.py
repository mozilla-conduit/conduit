# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from invoke import task


@task
def create_virtualenv(c):
    """Create a suitable python virtualenv."""
    c.run('virtualenv -p python3 venv')


@task(create_virtualenv)
def install_python_requirements(c):
    """Install the python requirements for development."""
    c.run('./venv/bin/pip install -r requirements.txt')
    c.run('./venv/bin/pip install -r test-requirements.txt')


@task(install_python_requirements)
def develop(c):
    """Download/refresh dev environment."""
    c.run('./venv/bin/python setup.py develop')


@task
def run(c, port=8080):
    """Run the development server."""
    c.run('./venv/bin/autolandweb --debug --port %s' % port, pty=True)


@task
def flake8(c):
    """Check the code against flake8."""
    c.run('./venv/bin/flake8 setup.py tasks.py autolandweb tests')


@task
def checkstyle(c):
    """Check the code style of the project."""
    c.run(
        './venv/bin/yapf --diff --recursive '
        'setup.py tasks.py autolandweb tests'
    )


@task
def formatstyle(c):
    """Reformat the code style in place."""
    c.run(
        './venv/bin/yapf --in-place --recursive '
        'setup.py tasks.py autolandweb tests'
    )


@task
def test(c):
    """Run the tests."""
    c.run('./venv/bin/pytest tests', pty=True)
