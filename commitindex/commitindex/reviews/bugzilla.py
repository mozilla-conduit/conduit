# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Interface to a Bugzilla system."""

from urllib.parse import quote
import json
import logging
import requests

logger = logging.getLogger(__name__)


class Bugzilla(object):
    """
    Interface to a Bugzilla system.

    TODO:
    1. Load REST URL from system wide config
    2. New content_type for conduit attachments?
    3. Add comment_tags for conduit attachments?
    """

    def __init__(self, rest_url=None):
        self.rest_url = rest_url
        self.session = requests.Session()

    def call(self, method, path, api_key=None, data=None):
        """Perform REST API call and decode JSON.

        Generic call function that performs a REST API call to the
        Bugzilla system and turns the JSON data returned into a
        Python data object.

        Args:
            method: Request method such as GET/POST/PUT...
            path: The resource path of the REST call.
            data: Optional data for the POST method.

        Returns:
            A Python object, normally a dict, containing the converted
            JSON data.

        Raises:
            BugzillaError: General error such as invalid JSON or Bugzilla
            returned an error of its own. The code in the latter case will
            pertain to the specific error code generated by Bugzilla.
        """

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        if api_key:
            headers['X-Bugzilla-API-Key'] = str(api_key)

        if method == 'GET':
            response = self.session.get(
                self.rest_url + path, params=data, headers=headers
            )

        if method == 'POST':
            response = self.session.post(
                self.rest_url + path, json=data, headers=headers
            )

        try:
            data = json.loads(response.content.decode('utf-8'))
        except:
            raise BugzillaError(400, "Error decoding JSON data")

        if isinstance(data, dict) and 'error' in data:
            raise BugzillaError(data['message'], data['code'])

        return data

    def is_bug_confidential(self, bug_id):
        """Check if bug is confidential

        Simple REST call checking if a given bug id is private or not.

        Params:
            bug_id: Integer ID of the bug to check.

        Returns:
            True if bug is private, False if public.

        Raises:
            BugzillaError: General error where the fault code and string will
            pertain to the specific error code generated by Bugzilla.
        """

        try:
            self.call('GET', '/bug/' + quote(str(bug_id)))
        except BugzillaError as error:
            if error.fault_code == 102:
                return True
            raise

        return False

    def valid_api_key(self, username, api_key):
        """Check if API key is valid for specific username

        Simple REST call to check if a given API key for a specified user
        is a valid login.

        Params:
            username: The Bugzilla login for the user, normally their email
            address.
            api_key: The 40 character API key for the user.

        Returns:
            True if the api_key and username pair are a valid login,
            False if nota

        Raises:
            BugzillaError: General error where the fault code and string will
            pertain to the specific error code generated by Bugzilla.
        """

        params = {'login': quote(username)}

        try:
            self.call(
                'GET', '/valid_login', data=params, api_key=quote(api_key)
            )
        except BugzillaError as error:
            if error.fault_code == 306:
                return False
            raise

        return True

    def create_attachment(self, bug_id, attach_data, api_key=None):
        """Create the attachment using the provided flags.

        Create a single attachment in Bugzilla using the REST API.

        Params:
            http://bmo.readthedocs.io/en/latest/api/core/v1/attachment.html#create-attachment

        Returns:
            Integer ID for new Bugzilla attachment.

        Raises:
            BugzillaError: General error where the fault code and string will
            pertain to the specific error code generated by Bugzilla.
        """

        try:
            result = self.call(
                'POST',
                '/bug/' + quote(str(bug_id)) + '/attachment',
                api_key=api_key,
                data=attach_data
            )
        except BugzillaError as error:
            logger.warning(
                {
                    'msg': error.fault_string,
                    'code': error.fault_code
                }, 'app.warning'
            )
            raise

        return int(list(result['attachments'].keys())[0])


class BugzillaError(Exception):
    """Generic Bugzilla Exception"""

    def __init__(self, msg, code=None):
        super(BugzillaError, self).__init__(msg)
        self.fault_code = int(code)
        self.fault_string = str(msg)
