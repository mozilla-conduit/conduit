# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import json
import os

from invoke import Collection, task, run

project_root = os.path.dirname(__file__)


@task(name='web',
      help={'image': 'The image to use to execute the test suite container '
                     '(default: autoland_autolandweb)',
            'testargs': 'Arguments to pass to the test suite (default: \'\')',
            'color': 'Include ANSI colour sequences in test output '
                     '(default: True)'})
def autoland_test_web(ctx, image='autoland_autolandweb', testargs='',
                      color=True):
    """Run the project test suite in a docker container."""
    if color:
        # pytest will produce colour output if it detects a pty, so to get
        # colour output we'll tell docker to allocate a pty to the container.
        pty_flag = '-t'
    else:
        pty_flag = ''

    # Taken from docker-compose.yml.  On the CI server we call docker
    # directly instead of using docker-compose. We'll build a command
    # similar to 'docker-compose run --rm autolandweb pytest'.
    run('docker run'
        ' -v {project_root}/autoland/public-web-api:/app'
        ' --rm'
        ' {pty}'
        ' {image} pytest {args}'.format(
            project_root=project_root,
            image=image,
            args=testargs,
            pty=pty_flag),
        echo=True)


@task(default=True, name='all', post=[autoland_test_web])
def autoland_test_all(ctx):
    """Run all tests for autoland."""
    pass


@task(name='version')
def version_json(ctx):
    """Print version information in JSON format."""
    version = {
        'commit': os.getenv('CIRCLE_SHA1', None),
        'version': os.getenv('CIRCLE_SHA1', None),
        'github-source': 'https://github.com/%s/%s' % (
            os.getenv('CIRCLE_PROJECT_USERNAME', 'mozilla-conduit'),
            os.getenv('CIRCLE_PROJECT_REPONAME', 'conduit')),
        'source': 'https://hg.mozilla.org/automation/conduit',
        'build': os.getenv('CIRCLE_BUILD_URL', None)
    }
    print(json.dumps(version))


namespace = Collection(
    Collection(
        'autoland',
        Collection(
            'test',
            autoland_test_all,
            autoland_test_web,
        ),
    ),
    version_json,
)
