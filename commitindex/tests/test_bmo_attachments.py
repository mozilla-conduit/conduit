# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Mountebank test cases for commit-index
"""

from commitindex.reviews.bugzilla import Bugzilla
from testing import MountebankClient

import pytest


class FakeBugzilla:
    """Setups up the imposter test double emulating Bugzilla"""

    def __init__(self, mountebank_client):

        self.mountebank = mountebank_client

    @property
    def url(self):
        """Return fully qualified url for server"""

        # Copied from the project docker-compose.yml file.
        return 'http://mountebank:' + str(self.mountebank.imposter_port)

    def create_attachment(self, bug_id):
        """Create a attachment in the fake bugzilla server."""

        path = '/bug/' + str(bug_id) + '/attachment'
        self.mountebank.create_stub(
            [
                {
                    "predicates": [
                        {
                            "equals": {
                                "method": "POST",
                                "headers": {
                                    "Content-Type": "application/json"
                                },
                                "path": path
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
                                    "attachments": {
                                        12345: {}
                                    }
                                }
                            }
                        }
                    ]
                },
                # 404 everything else
                {
                    "predicates": [{
                        "not": {
                            "equals": {
                                "path": path
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
def bugzilla(request, mountebank):
    """Returns emulated Bugzilla service methods"""

    # NOTE: comment out the line below if you want mountebank to save your
    # requests and responses for inspection after the test suite completes.
    # You can manually clean up the imposters afterwards by sending HTTP
    # DELETE to the exposed mountebank admin port, documented in
    # docker-compose.yml, or by restarting the mountebank container. See
    # http://www.mbtest.org/docs/api/stubs for details.
    request.addfinalizer(mountebank.reset_imposters)
    return FakeBugzilla(mountebank)


@pytest.mark.bugzilla
def test_create_valid_attachment(bugzilla):
    """Tests adding an attachment to the Bugzilla service"""

    attach_data = {
        "is_patch":
        False,
        "comment":
        "This is a new attachment comment",
        "summary":
        "Test Attachment",
        "content_type":
        "text/plain",
        "data":
        "data to be encoded",
        "file_name":
        "test_attachment.patch",
        "is_private":
        False,
        "flags": [
            {
                "name": "review",
                "status": "?",
                "requestee": "dkl@mozilla.com",
                "new": True
            }
        ]
    }

    bugzilla.create_attachment(1234)
    bug_test = Bugzilla(rest_url=bugzilla.url)
    result = bug_test.create_attachment(1234, attach_data, '12345')
    assert result == 12345
