# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


async def get_series_status(repo, series):
    """Return the status of a given commit series."""
    # TODO: Validate the series_id before echoing it back or using
    # it in any queries. The current regex is completely permissive.
    return {
        'id': series,
        'bug': 123456,
        'repository': 'https://hg.mozilla.org/mozilla-central/',
        'pushes': [  # List where each entry is a push of commits.
            {
                'commits': [  # Each commit pushed has an entry
                    {
                        'id': 'Bmc6S5XudOp',
                        'landing_blocker': 'This commit has not received '
                                           'sufficient review.',
                        'previous_revisions': [],
                        'reviews': [
                            {
                                'reviewer': {
                                    'name': 'Jyron Bones [:blog]',
                                    'nick': 'blog',
                                    'email': 'jyronbones@mozilla.com',
                                },
                                'status': 'r?',
                                'created_date': '2013-09-07T02:29:18Z',
                                'last_updated_date': '2013-09-07T02:29:18Z',
                            },
                        ],
                        'revision': '8eb8319674344fde118b0987b30e22cded00f71b',
                        'status': 'active',
                    },
                    {
                        'id': '1qxr8YNzP4h',
                        'landing_blocker': None,
                        'previous_revisions': [
                            '0acfc2c6fd8e92f33acd90c99c035bd3656286ca',
                        ],
                        'reviews': [
                            {
                                'reviewer': {
                                    'name': 'Jyron Bones [:blog]',
                                    'nick': 'blog',
                                    'email': 'jyronbones@mozilla.com',
                                },
                                'status': 'r+',
                                'created_date': '2013-09-07T02:29:18Z',
                                'last_updated_date': '2013-09-07T02:30:18Z',
                            },
                        ],
                        'revision': '11fb4626f5c357217e3f3a6c8edc22ee5c837224',
                        'status': 'active',
                    }
                ],
                'landing_blocker': 'Some commits are not ready to land.',
                'pusher': {
                    'name': "Wavid Dalsh [:waviddalsh]",
                    'email': "waviddalsh@mozilla.com",
                },
                'status': 'active',
            },
            {
                'commits': [
                    {
                        'id': '1qxr8YNzP4h',
                        'landing_blocker': 'This commit is obsolete',
                        # Reviewers are not listed for any push but the
                        # current.
                        'revision': '0acfc2c6fd8e92f33acd90c99c035bd3656286ca',
                        'previous_revisions': [],
                        'status': 'obsolete',
                    },
                ],
                'landing_blocker': 'This push is obsolete.',
                'pusher': {
                    'name': "Wavid Dalsh [:waviddalsh]",
                    'email': "waviddalsh@mozilla.com",
                },
                'status': 'obsolete',
            },
        ],
        'revisions': {
            # Revision data is in it's own dict to avoid repeating when
            # a revision has been in multiple pushes.
            '8eb8319674344fde118b0987b30e22cded00f71b': {
                'author': 'Wavid Dalsh <waviddalsh@mozilla.com>',
                'status': 'active',
                'commit_id': 'Bmc6S5XudOp',
            },
            '11fb4626f5c357217e3f3a6c8edc22ee5c837224': {
                'author': 'Wavid Dalsh <waviddalsh@mozilla.com>',
                'status': 'active',
                'commit_id': '1qxr8YNzP4h',
            },
            '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
                'author': 'Wavid Dalsh <waviddalsh@mozilla.com>',
                'status': 'obsolete',
                'commit_id': '1qxr8YNzP4h',
            },
        },
        'landings': [
            {
                '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
                    'backout_date': '2013-09-07T02:27:18Z',
                    'commit_id': '1qxr8YNzP4h',
                    'landed_date': '2013-09-07T02:26:18Z',
                    'landed_revision':
                        '59117a9f626cf2e954b9bb592efdc69d8169647f',
                    'repository':
                        'https://hg.mozilla.org/integration/autoland/',
                    'status': 'backout',
                    'error': None,
                },
            },
        ],
    }
