# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from flask import current_app

from commitindex.reviews.bugzilla import Bugzilla


def get_bugzilla_client():
    return Bugzilla(rest_url=current_app.config['BUGZILLA_URL'])


def trigger_review(commits, api_key):
    """Trigger review creation for an Iteration."""

    bugzilla = get_bugzilla_client()
    results = []
    for commit in commits:
        # TODO: Create real diff
        commit_data = {}
        commit_data['file_name'] = 'conduit test patch'
        commit_data['is_patch'] = True
        commit_data['summary'] = 'This is a test attachment from conduit'
        commit_data['data'] = """diff --git a/dirs/source.py b/dirs/source.py
--- a/dirs/source.py
+++ b/dirs/source.py
@@ -1,8 +1,17 @@

+from commitindex.reviews.bugzilla import Bugzilla"""

        attachment_id = bugzilla.create_attachment(
            1, commit_data, api_key=api_key
        )
        results.append({'commit': commit, 'attachment_id': attachment_id})

    return results
