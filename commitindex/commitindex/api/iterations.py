# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from connexion import problem

from commitindex.reviews.triggers import trigger_review


def search():
    pass


def get(id):
    # TODO: Attempt to find a persisted iteration matching the request.

    # We could not find a matching iteration.
    return problem(
        404,
        'Iteration not found',
        'The requested iteration does not exist',
        type='https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404'
    )


def post(commits):
    # TODO: Validate the passed commits form a single linear DAG line.
    # TODO: Create and persist a real iteration.

    # Trigger review creation for this iteration.
    trigger_review(commits)

    return {
        'data': {
            'id': 1,
            'topic': 1,
            'commits': [{
                'id': commit
            } for commit in commits],
        },
    }, 200
