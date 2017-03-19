# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import click
import connexion
from connexion.resolver import RestyResolver

app = connexion.App(__name__, specification_dir='spec/')
app.add_api('swagger.yml', resolver=RestyResolver('commitindex.api'))


@click.command()
@click.option('--debug', envvar='DEBUG', is_flag=True)
@click.option('--port', envvar='PORT', default=8888)
def development_server(debug, port):
    """Run the commitindex development server.

    This server should not be used for production deployments. Instead
    the commitindex should be served by an external webserver as a wsgi
    app.
    """
    app.run(debug=debug, port=port, host='0.0.0.0')
