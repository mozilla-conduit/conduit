# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Test helpers.
"""

from collections import namedtuple

import requests


class MountebankClient:
    def __init__(self, host, port=2525, imposter_port=4000):
        self.host = host
        self.port = port
        self.imposter_port = imposter_port

    @property
    def imposters_admin_url(self):
        return self.get_endpoint_with_port(self.port, '/imposters')

    @property
    def stub_baseurl(self):
        return self.get_endpoint_with_port(self.imposter_port)

    def get_endpoint(self, path=''):
        """Construct a URL for the imposter service with optional path."""
        return self.get_endpoint_with_port(self.imposter_port, path)

    def get_endpoint_with_port(self, port, path=''):
        """Construct a service endpoint URL with port and optional path."""
        return 'http://{0}:{1}{2}'.format(self.host, port, path)

    def create_imposter(self, imposter_json):
        """Take a dict and turn it into a service stub."""
        response = requests.post(self.imposters_admin_url, json=imposter_json)
        if response.status_code != 201:
            raise RuntimeError(
                "mountebank imposter creation failed: {0} {1}".
                format(response.status_code, response.content)
            )

    def create_stub(self, stub_json):
        """Create a http stub using the default imposter port."""
        self.create_imposter(
            {
                'port': self.imposter_port,
                'protocol': 'http',
                'stubs': stub_json
            }
        )

    def reset_imposters(self):
        """Delete all imposters."""
        requests.delete(self.imposters_admin_url)

    def get_requests(self):
        """Return a list of requests made to the imposter."""
        url = self.imposters_admin_url + '/' + str(self.imposter_port)
        return requests.get(url).json().get('requests')


MBHostInfo = namedtuple('MBHostInfo', 'ip adminport imposterport')
