# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import tornado.web


class LoadBalancerHeartbeatHandler(tornado.web.RequestHandler):
    """Handler for Dockerflow __lbheartbeat__."""

    def compute_etag(self):
        return None

    async def get(self):
        """Perform health check for load balancer.

        Since this is for load balancer checks it should not check
        backing services.
        """
        self.write({})
        self.set_status(200)
        self.set_header('Cache-Control', 'no-cache')


class HeartbeatHandler(tornado.web.RequestHandler):
    """Handler for Dockerflow __heartbeat__."""

    def compute_etag(self):
        return None

    async def get(self):
        """Perform health check of autoland backend."""
        self.write({})
        self.set_status(200)
        self.set_header('Cache-Control', 'no-cache')


DOCKERFLOW_ROUTES = [
    (r'/__lbheartbeat__/?$', LoadBalancerHeartbeatHandler),
    (r'/__heartbeat__/?$', HeartbeatHandler),
]
