# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from connexion import problem, request
from flask import current_app

from commitindex.reviews.triggers import get_bugzilla_client, trigger_review
from commitindex.commits.mercurial import Mercurial


def search():
    pass


def get_mercurial_client():
    """Return Mercurial client instance."""
    return Mercurial(rest_url=current_app.config['HG_SERVER_URL'])


def get(id):
    # TODO: Attempt to find a persisted iteration matching the request.

    # We could not find a matching iteration.
    return problem(
        404,
        'Iteration not found',
        'The requested iteration does not exist',
        type='https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404'
    )


def post(data):
    """
    data:
        - commits: (array of strings): required
        - topic: (integer): optional
    """
    # TODO: Validate the passed commits form a single linear DAG line.
    # TODO: Create and persist a real iteration.

    bugzilla = get_bugzilla_client()
    if not bugzilla.valid_api_key(
        request.headers['X-Bugzilla-Login'],
        request.headers['X-Bugzilla-API-Key']
    ):
        return problem(
            401, 'Invalid Bugzilla header values',
            'The Bugzilla API headers in the request were not valid'
        )

    topic = data.get('topic', 1)

    # TODO: Topic lookup and validation

    # Validate the commits with the mercurial server
    data['commits'] = fetch_commit_data(data['commits'])

    # Trigger review creation for this iteration.
    trigger_review(data['commits'], request.headers['X-Bugzilla-API-Key'])

    return {
        'data': {
            'id': 1,
            'topic': topic,
            'commits': [{
                'id': commit
            } for commit in data['commits']],
        },
    }, 200


def fetch_commit_data(commits, repo):
    """
    Take a list of commits ids, and fetch data for each from the
    Mercurial server.

    TODO:
    1. host variable should go away and be pulled in from some
    configuration file or environment variable. It is added here
    to facilitate mountebank testing.
    """

    mercurial = get_mercurial_client()

    commit_data = []

    for commit in commits:
        data = mercurial.get_commit_data(repo, commit)
        commit_data.append(data)

    return commit_data


def fetch_commit_diff(commit, repo):
    """
    Fetch the full diff for a specified commit.

    TODO:
    1. host variable should go away and be pulled in from some
    configuration file or environment variable. It is added here
    to facilitate mountebank testing.
    """

    mercurial = get_mercurial_client()

    return mercurial.get_commit_diff(repo, commit)
