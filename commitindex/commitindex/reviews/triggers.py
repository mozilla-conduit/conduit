# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from commitindex.reviews.bugzilla import Bugzilla
from flask import current_app


def get_bugzilla_client():
    return Bugzilla(rest_url=current_app.config['BUGZILLA_URL'])


def trigger_review(commits):
    """Trigger review creation for an Iteration."""

    for commit in commits:
        # TODO: Create real diff
        commit['data'] = """diff --git a/dirs/source.py b/dirs/source.py
--- a/dirs/source.py
+++ b/dirs/source.py
@@ -1,8 +1,17 @@

+from commitindex.reviews.bugzilla import Bugzilla"""

        diff_id = get_bugzilla_client().create_attachment(1, commit)
