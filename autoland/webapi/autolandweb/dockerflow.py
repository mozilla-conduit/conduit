# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import json

import tornado.web


def read_version(path):
    """Read dockerflow version json from path."""
    try:
        with open(path) as f:
            return json.load(f)
    except (IOError, ValueError) as e:
        return None


class DockerflowHandler(tornado.web.RequestHandler):
    """Handler which presets caching settings for Dockerflow endpoints."""

    def compute_etag(self):
        return None

    def set_default_headers(self):
        self.set_header('Cache-Control', 'no-cache')


class LoadBalancerHeartbeatHandler(DockerflowHandler):
    """Handler for Dockerflow __lbheartbeat__."""

    async def get(self):
        """Perform health check for load balancer.

        Since this is for load balancer checks it should not check
        backing services.
        """
        self.write({})
        self.set_status(200)


class HeartbeatHandler(DockerflowHandler):
    """Handler for Dockerflow __heartbeat__."""

    async def get(self):
        """Perform health check of autoland backend."""
        self.write({})
        self.set_status(200)


class VersionHandler(DockerflowHandler):
    """Handler for Dockerflow __version__."""

    async def get(self):
        """Respond with version information."""
        self.write(self.settings['version_data'])
        self.set_status(200)


DOCKERFLOW_ROUTES = [
    (r'/__heartbeat__/?$', HeartbeatHandler),
    (r'/__lbheartbeat__/?$', LoadBalancerHeartbeatHandler),
    (r'/__version__/?$', VersionHandler),
]
