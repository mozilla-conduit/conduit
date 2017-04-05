# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.
#
# To run the tests:
# `docker-compose up hgserver pytest /test`

import os
import sys
import json
import requests_mock

from mercurial.hgweb.common import (
    HTTP_OK,
    HTTP_SERVER_ERROR
)

# Manually add the hg extension folder to the path
sys.path.insert(0, '/hgext')
import conduit


class StubRequest(object):
    """A stub of mercurial.hgweb.request.

    This stubs out the request object that gets passed into the extension
    web endpoint and provides mock methods for it to call.
    """
    def __init__(self, headers, form_data):
        self.env = headers
        self.form = form_data
        self.response_status = None
        self.response_content_type = None

    def respond(self, status, content_type):
        """A mock of mercurial.hgweb.request.respond."""
        self.response_status = status
        self.response_content_type = content_type

    def has_valid_response_head(self, status_code):
        """A helper method to validate the response header.

        Use this method after respond has been called to ensure that the caller
        set the correct status code and and content type on this stub.
        """
        return self.response_status == status_code and \
            self.response_content_type == 'application/json'


def test_posting_valid_commits_returns_200():
    # WSGI parses all requests headers and puts them in the environment.
    # Thus, they look different than how they were specified in the request.
    wsgi_headers = {
        'HTTP_X_BUGZILLA_LOGIN': 'mozillian@example.com',
        'HTTP_X_BUGZILLA_API_KEY': '1234567890abcdefgABC',
    }
    form_data = {
        'topic': 1,
        'commit_ids': [
            '25c8974ba0d1e382c8f23da6e1a827cd22c4d015',
            '48982f7f928b8c8a77433bf7b1fa986fda4b239d'
        ],
    }
    request = StubRequest(wsgi_headers, form_data)

    expected_message = 'Successfully made Iteration id=1 on Topic id=1 with ' \
                       'commits: [25c8974ba0d1e382c8f23da6e1a827cd22c4d015, ' \
                       '48982f7f928b8c8a77433bf7b1fa986fda4b239d]\n'
    expected_response = json.dumps({'message': expected_message})

    with requests_mock.mock() as m:
        post_url = '%s/iterations/' % os.environ['COMMIT_INDEX_URL']
        result = {
            'data': {
                'id': 1,
                'topic': 1,
                'commits': [{
                    'id': commit
                } for commit in form_data['commit_ids']],
            },
        }
        m.post(post_url, text=json.dumps(result))
        response = conduit.stage(None, request, None)

    assert request.has_valid_response_head(HTTP_OK)
    assert response == expected_response


def test_posting_invalid_data_returns_500():
    request = StubRequest({}, {})
    expected_response = json.dumps({
        'type': 'about:blank', 'title': 'Internal Server Error',
        'status': HTTP_SERVER_ERROR, 'detail': 'Something went wrong.',
        'instance': 'about:blank'
    })

    with requests_mock.mock() as m:
        post_url = '%s/iterations/' % os.environ['COMMIT_INDEX_URL']
        result = {}
        m.post(post_url, text=json.dumps(result))
        response = conduit.stage(None, request, None)

    assert request.has_valid_response_head(HTTP_SERVER_ERROR)
    assert response == expected_response
