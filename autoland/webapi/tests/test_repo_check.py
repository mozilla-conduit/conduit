# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Test repository handling logic.
"""

from autolandweb.server import make_app
from autolandweb.testing import MountebankClient

import pytest

# FIXME: need to get pycharm test runner to add /app to the container PYTHONPATH # noqa
import sys
sys.path.insert(0, '/app')


class FakeReviewBoard:
    def __init__(self, mountebank_client):
        self.mountebank = mountebank_client

    @property
    def url(self):
        # Copied from the project docker-compose.yml file.
        return 'http://mountebank:' + str(self.mountebank.imposter_port)

    def create_repo(self, name, repo_info):
        """Create a repo in the fake reviewboard server."""
        repo_path = '/repos/' + name
        self.mountebank.create_stub(
            [
                # 200 for our repo path
                {
                    "predicates":
                    [{
                        "equals": {
                            "method": "GET",
                            "path": repo_path
                        }
                    }],
                    "responses": [
                        {
                            "is": {
                                "statusCode": 200,
                                "headers": {
                                    "Content-Type": "application/json"
                                },
                                "body": repo_info
                            }
                        }
                    ]
                },
                # 404 everything else
                {
                    "predicates": [{
                        "not": {
                            "equals": {
                                "path": repo_path
                            }
                        }
                    }],
                    "responses": [{
                        "is": {
                            "statusCode": 404
                        }
                    }]
                }
            ]
        )


@pytest.fixture
def app(reviewboard):
    """Returns the tornado.Application instance we'll be testing against.

    Required for pytest-tornado to function.
    """
    return make_app(
        reviewboard_url=reviewboard.url,
        version_data={
            'commit': None,
            'version': 'test',
            'source': 'https://hg.mozilla.org/automation/conduit',
            'build': 'test',
        }
    )


@pytest.fixture
def api_root(base_url):
    return base_url + "/api/v1"


@pytest.fixture(scope='session')
def mountebank():
    # The docker-compose internal DNS entry for the mountebank container
    mountebank_host = "mountebank"
    # Lifted from the docker-compose file
    mountebank_admin_port = 2525
    mountebank_imposter_port = 4000

    return MountebankClient(
        mountebank_host, mountebank_admin_port, mountebank_imposter_port
    )


@pytest.fixture
def reviewboard(request, mountebank):
    # NOTE: comment out the line below if you want mountebank to save your
    # requests and responses for inspection after the test suite completes.
    # You can manually clean up the imposters afterwards by sending HTTP
    # DELETE to the exposed mountebank admin port, documented in
    # docker-compose.yml, or by restarting the mountebank container. See
    # http://www.mbtest.org/docs/api/stubs for details.
    request.addfinalizer(mountebank.reset_imposters)
    return FakeReviewBoard(mountebank)


@pytest.mark.gen_test
async def test_return_info_for_valid_repo(http_client, api_root, reviewboard):
    # Arrange
    repo_name = 'mycoolrepo'
    repo_info = {'repo': {'name': repo_name}}
    reviewboard.create_repo(repo_name, repo_info)

    # Act
    repo_url = api_root + '/repos/' + repo_name
    response = await http_client.fetch(repo_url)

    # Assert
    assert response.code == 200


@pytest.mark.gen_test
async def test_return_404_if_repo_not_in_reviewboard(
    http_client, api_root, reviewboard
):
    repo_url = api_root + "/repos/zabumafu"
    reviewboard.create_repo("movealong", {})
    response = await http_client.fetch(repo_url, raise_error=False)
    assert response.code == 404
