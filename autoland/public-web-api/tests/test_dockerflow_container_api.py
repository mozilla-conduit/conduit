# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Tests to ensure we honour the Dockerflow container API specification.

See https://github.com/mozilla-services/Dockerflow for details.
"""

import pytest

# FIXME: need to get pycharm test runner to add /app to the container PYTHONPATH
import sys
sys.path.insert(0, '/app')

from autolandweb.server import make_app


@pytest.fixture
def app():
    return make_app(False)


@pytest.mark.gen_test
async def test_loadbalancer_heartbeat_returns_200(http_client, base_url):
    lb_heartbeat_url = base_url + '/__lbheartbeat__'
    response = await http_client.fetch(lb_heartbeat_url)
    assert response.code == 200


@pytest.mark.gen_test
async def test_heartbeat_returns_200(http_client, base_url):
    heartbeat_url = base_url + '/__heartbeat__'
    response = await http_client.fetch(heartbeat_url)
    assert response.code == 200
