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


def make_app(
    debug=False, version_data=None, reviewboard_url='', ac_allow_origin=None
):
    """Construct a fully configured Tornado Application object.

    Leaving out the version_data argument may lead to unexpected behaviour.

    Args:
        debug: Optional boolean, turns on the Tornado application server's
            debug mode.
        version_data: A dictionary with keys and data matching the Dockerflow
            spec versions.json. Optional, but excluding it may lead to
            unexpected behaviour.
            See https://github.com/mozilla-services/Dockerflow/blob/master/docs/version_object.md  # noqa
        reviewboard_url: Optional string, the URL of the reviewboard host and
            port to use for API requests. (e.g. 'http://foo.something:0000')
        ac_allow_origin: A string of the origin which may perform CORS requests
            to the server. This will be used as the value of the
            'Access-Control-Allow-Origin' header. Passing None will result in
            no header being set, which is restrictive.
    """
    return tornado.web.Application(
        ROUTES,
        debug=debug,
        log_function=tornado_log_function,
        version_data=version_data,
        reviewboard_url=reviewboard_url,
        ac_allow_origin=ac_allow_origin
    )


@click.command()
@click.option('--debug', envvar='AUTOLANDWEB_DEBUG', is_flag=True)
@click.option('--reviewboard-url', envvar='REVIEWBOARD_URL', default='')
@click.option('--port', envvar='AUTOLANDWEB_PORT', default=8888)
@click.option('--pretty-log', envvar='AUTOLANDWEB_PRETTY_LOG', default=False)
@click.option(
    '--version-path',
    envvar='AUTOLANDWEB_VERSION_PATH',
    default='/app/version.json'
)
@click.option('--ac-allow-origin', envvar='AC_ALLOW_ORIGIN', default=None)
def autolandweb(
    debug, reviewboard_url, port, pretty_log, version_path, ac_allow_origin
):
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

    app = make_app(debug, version_data, reviewboard_url, ac_allow_origin)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    autolandweb()
