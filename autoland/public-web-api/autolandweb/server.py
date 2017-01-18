# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from autolandweb.routes import ROUTES

import click
import tornado.ioloop
import tornado.log
import tornado.web


@click.command()
@click.option('--debug', envvar='AUTOLANDWEB_DEBUG', is_flag=True)
@click.option('--port', envvar='AUTOLANDWEB_PORT', default=8888)
def autolandweb(debug, port):
    # Enable access logging.
    tornado.log.enable_pretty_logging()

    app = tornado.web.Application(ROUTES, debug=debug)
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    autolandweb()
