# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import tornado.web

from autolandweb.series import get_series_status


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, from Autoland')


class ReposHandler(tornado.web.RequestHandler):
    """Handler for repositories."""

    def get(self, repo=None):
        pass


class SeriesHandler(tornado.web.RequestHandler):
    """Handler for series'."""

    async def get(self, repo, series=None):
        if series is None:
            self.write({})
            return

        status = await get_series_status(repo, series)
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
]
