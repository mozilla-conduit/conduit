# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import logging
import logging.config
import sys

import click
import tornado.ioloop
import tornado.log
import tornado.web

from autolandweb.dockerflow import read_version
from autolandweb.mozlog import get_mozlog_config, tornado_log_function
from autolandweb.routes import ROUTES

logger = logging.getLogger(__name__)


def make_app(debug, version_data):
    """Construct a fully configured Tornado Application object."""
    return tornado.web.Application(
        ROUTES,
        debug=debug,
        log_function=tornado_log_function,
        version_data=version_data
    )


@click.command()
@click.option('--debug', envvar='AUTOLANDWEB_DEBUG', is_flag=True)
@click.option('--port', envvar='AUTOLANDWEB_PORT', default=8888)
@click.option('--pretty-log', envvar='AUTOLANDWEB_PRETTY_LOG', default=False)
@click.option(
    '--version-path',
    envvar='AUTOLANDWEB_VERSION_PATH',
    default='/app/version.json'
)
def autolandweb(debug, port, pretty_log, version_path):
    logging_config = get_mozlog_config(debug=debug, pretty=pretty_log)
    logging.config.dictConfig(logging_config)

    version_data = read_version(version_path)
    if not version_data:
        logger.critical(
            {
                'msg': 'Could not load version.json, shutting down',
                'path': version_path,
            }, 'app.fatal'
        )
        sys.exit(1)

    app = make_app(debug, version_data)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    autolandweb()
