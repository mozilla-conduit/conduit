# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import tornado.httpclient
import tornado.web

from autolandweb.dockerflow import DOCKERFLOW_ROUTES
from autolandweb.series import get_series_status


class PublicApiHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        if self.settings['cors_allowed_origins']:
            self.set_header(
                'Access-Control-Allow-Origin',
                self.settings['cors_allowed_origins']
            )


class MainHandler(PublicApiHandler):
    def get(self):
        self.write('Hello, from Autoland')


class ReposHandler(PublicApiHandler):
    """Handler for repositories."""

    async def get(self, repo=None):
        if repo is None:
            return

        http = tornado.httpclient.AsyncHTTPClient()
        # FIXME: We don't validate the user input here!  Security problem?
        repo_url = self.settings['reviewboard_url'] + '/repos/' + repo
        # FIXME: Should the user agent be configurable or a constant?
        response = await http.fetch(
            repo_url,
            headers={'Accept': 'application/json'},
            user_agent='autoland tornado AsyncHTTPClient',
            raise_error=False
        )

        # Handle HTTP response codes.  3XX codes have already been handled
        # and followed by the tornado HTTP client.
        if response.code == 200:
            self.set_status(200)
        elif response.code == 404:
            self.set_status(404)
            self.write({'error': 'Repo not found'})
        else:
            # Everything not 2XX or 404 is an exception.
            response.rethrow()


class SeriesHandler(PublicApiHandler):
    """Handler for series'."""

    async def get(self, repo, series=None):
        if series is None:
            self.write({})
            return

        status = await get_series_status(repo, series)
        if status is None:
            self.set_status(404)
            self.write({'error': 'Series not found'})
        else:
            self.write(status)


REPO_REGEX = r'[a-zA-z-]+'

SERIES_REGEX = (  # "bz://<bug_number>/<irc_nick>"
    r'bz://[1-9][0-9]*/[a-zA-Z_<^\{\}\[\]\\][0-9a-zA-Z_<^\{\}\[\]\\]*')

ROUTES = [
    (r'/$', MainHandler),
    (r'/api/v1/repos/?$', ReposHandler),
    (r'/api/v1/repos/(?P<repo>' + REPO_REGEX + r')/?$', ReposHandler),
    (r'/api/v1/repos/(?P<repo>' + REPO_REGEX + r')/series/?$', SeriesHandler),
    (
        r'/api/v1/repos/(?P<repo>' + REPO_REGEX + r')/series/(?P<series>' +
        SERIES_REGEX + r')/?$', SeriesHandler
    ),
] + DOCKERFLOW_ROUTES
