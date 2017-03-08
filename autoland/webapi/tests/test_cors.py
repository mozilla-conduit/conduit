# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Tests to ensure that cors headers are properly set.
"""

import pytest

from autolandweb.server import make_app


@pytest.fixture
def app():
    """Returns the tornado.Application instance we'll be testing against.

    Required for pytest-tornado to function.
    """
    return make_app()


@pytest.mark.gen_test
async def test_cors_unset_without_config_option(http_client, base_url, app):
    root_url = base_url + '/'
    app.settings['ac_allow_origin'] = None
    response = await http_client.fetch(root_url)
    assert response.code == 200
    assert not response.headers.get_list('Access-Control-Allow-Origin')


@pytest.mark.gen_test
async def test_cors_header_set_from_config(http_client, base_url, app):
    root_url = base_url + '/'
    origin = 'https://autoland.mozilla.org'
    app.settings['ac_allow_origin'] = origin
    response = await http_client.fetch(root_url)
    assert response.code == 200
    assert response.headers['Access-Control-Allow-Origin'] == origin
