# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import logging.config

import click
import tornado.ioloop
import tornado.log
import tornado.web

from autolandweb.mozlog import get_mozlog_config, tornado_log_function
from autolandweb.routes import ROUTES


def make_app(debug):
    """Construct a fully configured Tornado Application object."""
    return tornado.web.Application(
        ROUTES, debug=debug, log_function=tornado_log_function
    )


@click.command()
@click.option('--debug', envvar='AUTOLANDWEB_DEBUG', is_flag=True)
@click.option('--port', envvar='AUTOLANDWEB_PORT', default=8888)
@click.option('--pretty-log', envvar='AUTOLANDWEB_PRETTY_LOG', default=False)
def autolandweb(debug, port, pretty_log):
    logging_config = get_mozlog_config(debug=debug, pretty=pretty_log)
    logging.config.dictConfig(logging_config)

    app = make_app(debug)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    autolandweb()
