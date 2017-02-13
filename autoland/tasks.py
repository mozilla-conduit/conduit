# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import os

from invoke import task, run

project_root = os.path.dirname(__file__)


@task(help={'image': 'The image to use to execute the test suite container '
                     '(default: autoland_autolandweb)',
            'testargs': 'Arguments to pass to the test suite (default: \'\')',
            'color': 'Include ANSI colour sequences in test output '
                     '(default: True)'})
def test(image='autoland_autolandweb', testargs='', color=True):
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
        ' -v {project_root}/public-web-api:/app'
        ' --rm'
        ' {pty}'
        ' {image} pytest {args}'.format(
            project_root=project_root,
            image=image,
            args=testargs,
            pty=pty_flag),
        echo=True)
