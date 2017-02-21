# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Tests to ensure we honour the Dockerflow container API specification.

See https://github.com/mozilla-services/Dockerflow for details.
"""
import json

import pytest

from autolandweb.server import make_app


@pytest.fixture
def app():
    """Returns the tornado.Application instance we'll be testing against.

    Required for pytest-tornado to function.
    """
    return make_app(
        version_data={
            'commit': None,
            'version': 'test',
            'source': 'https://hg.mozilla.org/automation/conduit',
            'build': 'test',
        }
    )


@pytest.mark.gen_test
async def test_loadbalancer_heartbeat_returns_200(http_client, base_url):
    lb_heartbeat_url = base_url + '/__lbheartbeat__'
    response = await http_client.fetch(lb_heartbeat_url)
    assert response.code == 200
    assert response.headers['Cache-Control'] == 'no-cache'
    assert not response.headers.get_list('Etag')


@pytest.mark.gen_test
async def test_heartbeat_returns_200(http_client, base_url):
    heartbeat_url = base_url + '/__heartbeat__'
    response = await http_client.fetch(heartbeat_url)
    assert response.code == 200
    assert response.headers['Cache-Control'] == 'no-cache'
    assert not response.headers.get_list('Etag')


@pytest.mark.gen_test
async def test_version_returns_200(http_client, base_url):
    version_url = base_url + '/__version__'
    response = await http_client.fetch(version_url)
    assert response.code == 200
    assert response.headers['Cache-Control'] == 'no-cache'
    assert not response.headers.get_list('Etag')
    assert 'application/json' in response.headers['Content-Type']

    data = json.loads(response.body.decode('utf-8'))
    assert data['version'] == 'test'
