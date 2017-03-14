# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json

from mercurial.hgweb import webcommands
from mercurial.hgweb.common import HTTP_OK


def extsetup(ui):
    """Standard extension setup routine"""
    print('Hello from the conduit mercurial extension!')

    setattr(webcommands, 'commitindex', extensioncommand)
    webcommands.__all__.append('commitindex')


def extensioncommand(web, req, tmpl):
    """Simply dumps a sample JSON to prove the endpoint works"""
    req.respond(HTTP_OK, 'application/json')
    return json.dumps({'message': 'Hello from the Conduit extension!'})
