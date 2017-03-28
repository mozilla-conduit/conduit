# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Mountebank test cases for commit-index
"""

from commitindex.commitindex import app
from commitindex.api.iterations import (
    get_mercurial_client, fetch_commit_data, fetch_commit_diff
)
from commitindex.commits.mercurial import MercurialError
from testing import MountebankClient
from flask import current_app
import pytest

COMMIT_DIFF = """diff --git a/dirs/source.py b/dirs/source.py
--- a/dirs/source.py
+++ b/dirs/source.py
@@ -1,8 +1,17 @@

+from commitindex.reviews.bugzilla import Bugzilla
"""


class FakeMercurial:
    """Setups up the imposter test double emulating Mercurial"""

    def __init__(self, mountebank_client):
        self.mountebank = mountebank_client

    @property
    def url(self):
        """Return fully qualified url for server"""

        # Copied from the project docker-compose.yml file.
        return 'http://mountebank:' + str(self.mountebank.imposter_port)

    def create_commit_stubs(self, commit_data):
        """Get detail information about specific revids from Mercurial."""

        data_path = '/automation/conduit/json-rev/'
        diff_path = '/automation/conduit/raw-rev/'

        create_stubs = []
        for commit_node in commit_data.keys():
            create_stubs.append(
                {
                    "predicates": [
                        {
                            "equals": {
                                "method": "GET",
                                "path": data_path + commit_node
                            }
                        }
                    ],
                    "responses": [
                        {
                            "is": {
                                "statusCode": 200,
                                "headers": {
                                    "Content-Type": "application/json"
                                },
                                "body": {
                                    "node": commit_node,
                                    "date": [1490110970.0, 14400],
                                    "desc": "commit description",
                                    "backedoutby": "",
                                    "branch": "default",
                                    "bookmarks": [],
                                    "tags": [],
                                    "user": "Joe Developer <joe@mexample.com>",
                                    "parents": [commit_data[commit_node]],
                                    "phase": "public",
                                    "pushid": 75,
                                    "pushdate": [1490146788, 0],
                                    "pushuser": "joe@example.com"
                                }
                            }
                        }
                    ]
                }
            )
            create_stubs.append(
                {
                    "predicates": [
                        {
                            "equals": {
                                "method": "GET",
                                "path": diff_path + commit_node
                            }
                        }
                    ],
                    "responses": [
                        {
                            "is": {
                                "statusCode": 200,
                                "headers": {
                                    "Content-Type": "text/plain"
                                },
                                "body": COMMIT_DIFF
                            }
                        }
                    ]
                }
            )

        predicates_not_found = []
        for commit_node in commit_data.keys():
            predicates_not_found.append(
                {
                    "not": {
                        "equals": {
                            "path": data_path + commit_node
                        }
                    }
                }
            )
            predicates_not_found.append(
                {
                    "not": {
                        "equals": {
                            "path": diff_path + commit_node
                        }
                    }
                }
            )

        create_stubs.append(
            {
                "predicates": predicates_not_found,
                "responses": [{
                    "is": {
                        "statusCode": 404
                    }
                }]
            }
        )
        self.mountebank.create_stub(create_stubs)


@pytest.fixture(scope='session')
def mountebank():
    """Returns configured Mounteback client instance"""

    # The docker-compose internal DNS entry for the mountebank container
    mountebank_host = "mountebank"
    # Lifted from the docker-compose file
    mountebank_admin_port = 2525
    mountebank_imposter_port = 4000

    return MountebankClient(
        mountebank_host, mountebank_admin_port, mountebank_imposter_port
    )


@pytest.fixture
def mercurial(request, mountebank):
    """Returns emulated Mercurial service methods"""

    # NOTE: comment out the line below if you want mountebank to save your
    # requests and responses for inspection after the test suite completes.
    # You can manually clean up the imposters afterwards by sending HTTP
    # DELETE to the exposed mountebank admin port, documented in
    # docker-compose.yml, or by restarting the mountebank container. See
    # http://www.mbtest.org/docs/api/stubs for details.
    request.addfinalizer(mountebank.reset_imposters)
    return FakeMercurial(mountebank)


@pytest.fixture
def fake_commit_data(mercurial):
    """Setup stubs for testing."""

    # commit_node : parent_node
    commit_data = {
        'f5279c5bcc6c74e9cf767fad36930e9ae7d09bdc':
        '797fef1ce31a759dcea06e8cd269405bcbd14f96',
        '48982f7f928b8c8a77433bf7b1fa986fda4b239d':
        'f5279c5bcc6c74e9cf767fad36930e9ae7d09bdc'
    }

    mercurial.create_commit_stubs(commit_data)

    return commit_data


def test_mercurial_client_properly_created():
    """Tests that a Mercurial client is properly created with URL"""

    hg_server_url = 'http://blah/'
    with app.app.app_context():
        current_app.config['HG_SERVER_URL'] = hg_server_url

        client = get_mercurial_client()
        assert client.rest_url == hg_server_url


def test_get_commit_data_success(fake_commit_data, mercurial):
    """
    Tests for successfully getting extended commit data from Mercurial.
    """

    with app.app.app_context():
        current_app.config['HG_SERVER_URL'] = mercurial.url

        results = fetch_commit_data(
            [x for x in fake_commit_data.keys()],
            'automation/conduit',
        )

        for result in results:
            assert result['node'] in fake_commit_data.keys()


def test_get_commit_data_bad_commit_raises_error(fake_commit_data, mercurial):
    """
    Tests for proper failure from Mercurial when using bad commit node.
    """

    with app.app.app_context():
        current_app.config['HG_SERVER_URL'] = mercurial.url

        with pytest.raises(MercurialError):
            fetch_commit_data(['12345'], 'automation/conduit')


def test_get_commit_data_bad_repo_raises_error(fake_commit_data, mercurial):
    """
    Tests for proper failure from Mercurial when using bad repo name.
    """

    with app.app.app_context():
        current_app.config['HG_SERVER_URL'] = mercurial.url

        with pytest.raises(MercurialError):
            fetch_commit_data(
                ['f5279c5bcc6c74e9cf767fad36930e9ae7d09bdc'],
                'automation/bugzilla'
            )


def test_get_commit_diff_success(fake_commit_data, mercurial):
    """
    Tests for successfully getting raw diff from Mercurial.
    """

    with app.app.app_context():
        current_app.config['HG_SERVER_URL'] = mercurial.url

        result = fetch_commit_diff(
            'f5279c5bcc6c74e9cf767fad36930e9ae7d09bdc', 'automation/conduit'
        )
        assert result == COMMIT_DIFF


def test_get_commit_diff_bad_commit_raises_error(fake_commit_data, mercurial):
    """
    Tests for proper failure Mercurial when using bad commit node.
    """

    with app.app.app_context():
        current_app.config['HG_SERVER_URL'] = mercurial.url

        with pytest.raises(MercurialError):
            fetch_commit_diff('12345', 'automation/conduit')


def test_get_commit_diff_bad_repo_raises_error(fake_commit_data, mercurial):
    """
    Tests for proper failure from Mercurial when using bad repo.
    """

    with app.app.app_context():
        current_app.config['HG_SERVER_URL'] = mercurial.url

        with pytest.raises(MercurialError):
            fetch_commit_diff(
                'f5279c5bcc6c74e9cf767fad36930e9ae7d09bdc',
                'automation/bugzilla'
            )
