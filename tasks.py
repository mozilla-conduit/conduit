# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import json
import os

from invoke import Collection, task, run

project_root = os.path.dirname(__file__)


@task(name='flake8')
def autoland_lint_web_flake8(ctx):
    """Run flake8 for autolandweb."""
    run(
        'docker-compose'
        ' -f {project_root}/autoland/docker-compose.yml'
        ' run'
        ' --rm'
        ' autolandweb'
        ' flake8 setup.py tasks.py autolandweb tests'
        ''.format(project_root=project_root),
        echo=True
    )


@task(name='yapf')
def autoland_lint_web_yapf(ctx):
    """Run yapf for autolandweb."""
    run(
        'docker-compose'
        ' -f {project_root}/autoland/docker-compose.yml'
        ' run'
        ' --rm'
        ' autolandweb'
        ' yapf --diff --recursive setup.py tasks.py autolandweb tests'
        ''.format(project_root=project_root),
        echo=True
    )


@task(
    default=True,
    name='all',
    post=[autoland_lint_web_yapf, autoland_lint_web_flake8]
)
def autoland_lint_web(ctx):
    """Lint autolandweb"""
    pass


@task(default=True, name='all', post=[autoland_lint_web])
def autoland_lint_all(ctx):
    """Lint autoland."""
    pass


@task(
    name='web',
    help={
        'testargs': 'Arguments to pass to the test suite (default: \'\')',
        'keep': 'Do not remove the test container after running',
    }
)
def autoland_test_web(ctx, testargs='', keep=False):
    """Test autolandweb."""
    run(
        'docker-compose'
        ' -f {project_root}/autoland/docker-compose.yml'
        ' run'
        '{rm}'
        ' autolandweb'
        ' pytest {args}'
        ''.format(
            project_root=project_root,
            args=testargs,
            rm=('' if keep else ' --rm')
        ),
        pty=True,
        echo=True
    )


@task(
    name='ui',
    help={
        'testargs': 'Arguments to pass to the test suite (default: \'\')',
        'keep': 'Do not remove the test container after running',
        'no_pty': 'Execute tests without a pty.',
    }
)
def autoland_test_ui(ctx, testargs='', keep=False, no_pty=False):
    """Test autoland/ui."""
    run(
        'docker-compose'
        ' -f {project_root}/autoland/docker-compose.yml'
        ' run'
        '{rm}'
        ' yarn'
        ' test {args}'
        ''.format(
            project_root=project_root,
            args=testargs,
            rm=('' if keep else ' --rm')
        ),
        pty=not no_pty,
        echo=True
    )


@task(default=True, name='all', post=[autoland_test_ui, autoland_test_web])
def autoland_test_all(ctx):
    """Test autoland."""
    pass


@task(post=[autoland_test_all])
def test(ctx):
    pass


@task(name='format')
def autoland_format(ctx):
    run(
        'docker-compose'
        ' -f {project_root}/autoland/docker-compose.yml'
        ' run'
        ' --rm'
        ' autolandweb'
        ' yapf --in-place --recursive setup.py tasks.py autolandweb tests'
        ''.format(project_root=project_root),
        echo=True
    )


@task(name='format', post=[autoland_format])
def code_format(ctx):
    """Auto format the code style (MODIFIES FILES!)."""
    pass


@task(post=[autoland_lint_all])
def lint(ctx):
    pass


@task(name='version')
def version_json(ctx):
    """Print version information in JSON format."""
    version = {
        'commit': os.getenv('CIRCLE_SHA1', None),
        'version': os.getenv('CIRCLE_SHA1', None),
        'github-source': 'https://github.com/%s/%s' % (
            os.getenv('CIRCLE_PROJECT_USERNAME', 'mozilla-conduit'),
            os.getenv('CIRCLE_PROJECT_REPONAME', 'conduit')
        ),
        'source': 'https://hg.mozilla.org/automation/conduit',
        'build': os.getenv('CIRCLE_BUILD_URL', None)
    }
    print(json.dumps(version))


namespace = Collection(
    Collection(
        'autoland',
        Collection(
            'lint',
            Collection(
                'web',
                autoland_lint_web,
                autoland_lint_web_flake8,
                autoland_lint_web_yapf,
            ),
            autoland_lint_all,
        ),
        Collection(
            'test',
            autoland_test_all,
            autoland_test_web,
            autoland_test_ui,
        ),
        autoland_format,
    ),
    code_format,
    lint,
    test,
    version_json,
)
