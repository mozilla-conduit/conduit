# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

CANNED_RESPONSES = {}

CANNED_RESPONSES['bz://123456/cannotland'] = {
    'id':
    'bz://123456/cannotland',
    'bug':
    123456,
    'repository':
    'https://hg.mozilla.org/mozilla-central/',
    'pushes': [
        {
            'commits': [
                {
                    'id':
                    'Bmc6S5XudOp',
                    'landing_blocker':
                    'This commit has not received '
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
                    'revision':
                    '8eb8319674344fde118b0987b30e22cded00f71b',
                    'status':
                    'active',
                }, {
                    'id':
                    '1qxr8YNzP4h',
                    'landing_blocker':
                    None,
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
                    'revision':
                    '11fb4626f5c357217e3f3a6c8edc22ee5c837224',
                    'status':
                    'active',
                }
            ],
            'landing_blocker':
            'Some commits are not ready to land.',
            'pusher': {
                'name': "Wavid Dalsh [:waviddalsh]",
                'email': "waviddalsh@mozilla.com",
            },
            'status':
            'active',
        },
        {
            'commits': [
                {
                    'id': '1qxr8YNzP4h',
                    'landing_blocker': 'This commit is obsolete',
                    'revision': '0acfc2c6fd8e92f33acd90c99c035bd3656286ca',
                    'previous_revisions': [],
                    'status': 'obsolete',
                },
            ],
            'landing_blocker':
            'This push is obsolete.',
            'pusher': {
                'name': "Wavid Dalsh [:waviddalsh]",
                'email': "waviddalsh@mozilla.com",
            },
            'status':
            'obsolete',
        },
    ],
    'revisions': {
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
                'landed_revision': '59117a9f626cf2e954b9bb592efdc69d8169647f',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'status': 'backout',
                'error': None,
            },
        },
    ],
}

CANNED_RESPONSES['bz://123456/canland'] = {
    'id':
    'bz://123456/canland',
    'bug':
    123456,
    'repository':
    'https://hg.mozilla.org/mozilla-central/',
    'pushes': [
        {
            'landing_blocker':
            None,
            'commits': [
                {
                    'id':
                    'Bmc6S5XudOp',
                    'landing_blocker':
                    None,
                    'previous_revisions': [],
                    'revision':
                    '8eb8319674344fde118b0987b30e22cded00f71b',
                    'reviews': [
                        {
                            'created_date': '2013-09-07T02:29:18Z',
                            'reviewer': {
                                'name': 'Jyron Bones [:blog]',
                                'nick': 'blog',
                                'email': 'jyronbones@mozilla.com',
                            },
                            'last_updated_date': '2013-09-07T02:32:18Z',
                            'status': 'r+',
                        }
                    ],
                    'status':
                    'active',
                }, {
                    'id':
                    '1qxr8YNzP4h',
                    'landing_blocker':
                    None,
                    'previous_revisions': [
                        '0acfc2c6fd8e92f33acd90c99c035bd3656286ca',
                    ],
                    'revision':
                    '11fb4626f5c357217e3f3a6c8edc22ee5c837224',
                    'reviews': [
                        {
                            'created_date': '2013-09-07T02:29:18Z',
                            'reviewer': {
                                'name': 'Jyron Bones [:blog]',
                                'nick': 'blog',
                                'email': 'jyronbones@mozilla.com',
                            },
                            'last_updated_date': '2013-09-07T02:30:18Z',
                            'status': 'r+',
                        }
                    ],
                    'status':
                    'active',
                }
            ],
            'pusher': {
                'name': 'Wavid Dalsh [:waviddalsh]',
                'email': 'waviddalsh@mozilla.com',
            },
            'status':
            'active',
        }, {
            'landing_blocker':
            'This push is obsolete.',
            'commits': [
                {
                    'id': '1qxr8YNzP4h',
                    'landing_blocker': 'This commit is obsolete',
                    'previous_revisions': [],
                    'revision': '0acfc2c6fd8e92f33acd90c99c035bd3656286ca',
                    'status': 'obsolete',
                }
            ],
            'pusher': {
                'name': 'Wavid Dalsh [:waviddalsh]',
                'email': 'waviddalsh@mozilla.com',
            },
            'status':
            'obsolete',
        }
    ],
    'revisions': {
        '8eb8319674344fde118b0987b30e22cded00f71b': {
            'commit_id': 'Bmc6S5XudOp',
            'status': 'active',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>',
        },
        '11fb4626f5c357217e3f3a6c8edc22ee5c837224': {
            'commit_id': '1qxr8YNzP4h',
            'status': 'active',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>',
        },
        '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
            'commit_id': '1qxr8YNzP4h',
            'status': 'obsolete',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>',
        },
    },
    'landings': [
        {
            '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
                'status': 'backout',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': '2013-09-07T02:26:18Z',
                'commit_id': '1qxr8YNzP4h',
                'backout_date': '2013-09-07T02:27:18Z',
                'landed_revision': '59117a9f626cf2e954b9bb592efdc69d8169647f',
            }
        },
    ],
}

CANNED_RESPONSES['bz://123456/inprogress'] = {
    'id':
    'bz://123456/inprogress',
    'bug':
    123456,
    'repository':
    'https://hg.mozilla.org/mozilla-central/',
    'pushes': [
        {
            'landing_blocker':
            'Landing is already in progress',
            'commits': [
                {
                    'id':
                    'Bmc6S5XudOp',
                    'landing_blocker':
                    None,
                    'previous_revisions': [],
                    'revision':
                    '8eb8319674344fde118b0987b30e22cded00f71b',
                    'reviews': [
                        {
                            'created_date': '2013-09-07T02:29:18Z',
                            'reviewer': {
                                'name': 'Jyron Bones [:blog]',
                                'nick': 'blog',
                                'email': 'jyronbones@mozilla.com'
                            },
                            'last_updated_date': '2013-09-07T02:32:18Z',
                            'status': 'r+'
                        }
                    ],
                    'status':
                    'landing'
                }, {
                    'id':
                    '1qxr8YNzP4h',
                    'landing_blocker':
                    None,
                    'previous_revisions':
                    ['0acfc2c6fd8e92f33acd90c99c035bd3656286ca'],
                    'revision':
                    '11fb4626f5c357217e3f3a6c8edc22ee5c837224',
                    'reviews': [
                        {
                            'created_date': '2013-09-07T02:29:18Z',
                            'reviewer': {
                                'name': 'Jyron Bones [:blog]',
                                'nick': 'blog',
                                'email': 'jyronbones@mozilla.com'
                            },
                            'last_updated_date': '2013-09-07T02:30:18Z',
                            'status': 'r+'
                        }
                    ],
                    'status':
                    'landing'
                }
            ],
            'pusher': {
                'name': 'Wavid Dalsh [:waviddalsh]',
                'email': 'waviddalsh@mozilla.com'
            },
            'status':
            'landing'
        }, {
            'landing_blocker':
            'This push is obsolete.',
            'commits': [
                {
                    'id': '1qxr8YNzP4h',
                    'landing_blocker': 'This commit is obsolete',
                    'previous_revisions': [],
                    'revision': '0acfc2c6fd8e92f33acd90c99c035bd3656286ca',
                    'status': 'obsolete'
                }
            ],
            'pusher': {
                'name': 'Wavid Dalsh [:waviddalsh]',
                'email': 'waviddalsh@mozilla.com'
            },
            'status':
            'obsolete'
        }
    ],
    'revisions': {
        '8eb8319674344fde118b0987b30e22cded00f71b': {
            'commit_id': 'Bmc6S5XudOp',
            'status': 'active',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>'
        },
        '11fb4626f5c357217e3f3a6c8edc22ee5c837224': {
            'commit_id': '1qxr8YNzP4h',
            'status': 'active',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>'
        },
        '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
            'commit_id': '1qxr8YNzP4h',
            'status': 'obsolete',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>'
        }
    },
    'landings': [
        {
            '8eb8319674344fde118b0987b30e22cded00f71b': {
                'status': 'landing',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': None,
                'commit_id': 'Bmc6S5XudOp',
                'backout_date': None,
                'landed_revision': None
            },
            '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
                'status': 'landing',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': None,
                'commit_id': '1qxr8YNzP4h',
                'backout_date': None,
                'landed_revision': None
            }
        }, {
            '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
                'status': 'backout',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': '2013-09-07T02:26:18Z',
                'commit_id': '1qxr8YNzP4h',
                'backout_date': '2013-09-07T02:27:18Z',
                'landed_revision': '59117a9f626cf2e954b9bb592efdc69d8169647f'
            }
        }
    ]
}

CANNED_RESPONSES['bz://123456/landed'] = {
    'id':
    'bz://123456/landed',
    'bug':
    123456,
    'repository':
    'https://hg.mozilla.org/mozilla-central/',
    'pushes': [
        {
            'landing_blocker':
            'Already landed',
            'commits': [
                {
                    'id':
                    'Bmc6S5XudOp',
                    'landing_blocker':
                    'Already landed',
                    'previous_revisions': [],
                    'revision':
                    '8eb8319674344fde118b0987b30e22cded00f71b',
                    'reviews': [
                        {
                            'created_date': '2013-09-07T02:29:18Z',
                            'reviewer': {
                                'name': 'Jyron Bones [:blog]',
                                'nick': 'blog',
                                'email': 'jyronbones@mozilla.com'
                            },
                            'last_updated_date': '2013-09-07T02:32:18Z',
                            'status': 'r+'
                        }
                    ],
                    'status':
                    'landed'
                }, {
                    'id':
                    '1qxr8YNzP4h',
                    'landing_blocker':
                    'Already landed',
                    'previous_revisions':
                    ['0acfc2c6fd8e92f33acd90c99c035bd3656286ca'],
                    'revision':
                    '11fb4626f5c357217e3f3a6c8edc22ee5c837224',
                    'reviews': [
                        {
                            'created_date': '2013-09-07T02:29:18Z',
                            'reviewer': {
                                'name': 'Jyron Bones [:blog]',
                                'nick': 'blog',
                                'email': 'jyronbones@mozilla.com'
                            },
                            'last_updated_date': '2013-09-07T02:30:18Z',
                            'status': 'r+'
                        }
                    ],
                    'status':
                    'landed'
                }
            ],
            'pusher': {
                'name': 'Wavid Dalsh [:waviddalsh]',
                'email': 'waviddalsh@mozilla.com'
            },
            'status':
            'landed'
        }, {
            'landing_blocker':
            'This push is obsolete.',
            'commits': [
                {
                    'id': '1qxr8YNzP4h',
                    'landing_blocker': 'This commit is obsolete',
                    'previous_revisions': [],
                    'revision': '0acfc2c6fd8e92f33acd90c99c035bd3656286ca',
                    'status': 'obsolete'
                }
            ],
            'pusher': {
                'name': 'Wavid Dalsh [:waviddalsh]',
                'email': 'waviddalsh@mozilla.com'
            },
            'status':
            'obsolete'
        }
    ],
    'revisions': {
        '8eb8319674344fde118b0987b30e22cded00f71b': {
            'commit_id': 'Bmc6S5XudOp',
            'status': 'active',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>'
        },
        '11fb4626f5c357217e3f3a6c8edc22ee5c837224': {
            'commit_id': '1qxr8YNzP4h',
            'status': 'active',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>'
        },
        '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
            'commit_id': '1qxr8YNzP4h',
            'status': 'obsolete',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>'
        }
    },
    'landings': [
        {
            '8eb8319674344fde118b0987b30e22cded00f71b': {
                'status': 'landed',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': '2013-09-07T02:34:18Z',
                'commit_id': 'Bmc6S5XudOp',
                'backout_date': None,
                'landed_revision': '8851a6fd328fe222531e8552103a5eca2dc4d3a5',
                'error': None
            },
            '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
                'status': 'landed',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': '2013-09-07T02:34:18Z',
                'commit_id': '1qxr8YNzP4h',
                'backout_date': None,
                'landed_revision': 'be2d6a3f29c06ecff9f55e882ff37bd601901cd6',
                'error': None
            }
        }, {
            '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
                'status': 'backout',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': '2013-09-07T02:26:18Z',
                'commit_id': '1qxr8YNzP4h',
                'backout_date': '2013-09-07T02:27:18Z',
                'landed_revision': '59117a9f626cf2e954b9bb592efdc69d8169647f',
                'error': None
            }
        }
    ]
}

CANNED_RESPONSES['bz://123456/failedland'] = {
    'id':
    'bz://123456/failedland',
    'bug':
    123456,
    'repository':
    'https://hg.mozilla.org/mozilla-central/',
    'pushes': [
        {
            'landing_blocker':
            None,
            'commits': [
                {
                    'id':
                    'Bmc6S5XudOp',
                    'landing_blocker':
                    None,
                    'previous_revisions': [],
                    'revision':
                    '8eb8319674344fde118b0987b30e22cded00f71b',
                    'reviews': [
                        {
                            'created_date': '2013-09-07T02:29:18Z',
                            'reviewer': {
                                'name': 'Jyron Bones [:blog]',
                                'nick': 'blog',
                                'email': 'jyronbones@mozilla.com'
                            },
                            'last_updated_date': '2013-09-07T02:32:18Z',
                            'status': 'r+'
                        }
                    ],
                    'status':
                    'active'
                }, {
                    'id':
                    '1qxr8YNzP4h',
                    'landing_blocker':
                    None,
                    'previous_revisions':
                    ['0acfc2c6fd8e92f33acd90c99c035bd3656286ca'],
                    'revision':
                    '11fb4626f5c357217e3f3a6c8edc22ee5c837224',
                    'reviews': [
                        {
                            'created_date': '2013-09-07T02:29:18Z',
                            'reviewer': {
                                'name': 'Jyron Bones [:blog]',
                                'nick': 'blog',
                                'email': 'jyronbones@mozilla.com'
                            },
                            'last_updated_date': '2013-09-07T02:30:18Z',
                            'status': 'r+'
                        }
                    ],
                    'status':
                    'active'
                }
            ],
            'pusher': {
                'name': 'Wavid Dalsh [:waviddalsh]',
                'email': 'waviddalsh@mozilla.com'
            },
            'status':
            'active'
        }, {
            'landing_blocker':
            'This push is obsolete.',
            'commits': [
                {
                    'id': '1qxr8YNzP4h',
                    'landing_blocker': 'This commit is obsolete',
                    'previous_revisions': [],
                    'revision': '0acfc2c6fd8e92f33acd90c99c035bd3656286ca',
                    'status': 'obsolete'
                }
            ],
            'pusher': {
                'name': 'Wavid Dalsh [:waviddalsh]',
                'email': 'waviddalsh@mozilla.com'
            },
            'status':
            'obsolete'
        }
    ],
    'revisions': {
        '8eb8319674344fde118b0987b30e22cded00f71b': {
            'commit_id': 'Bmc6S5XudOp',
            'status': 'active',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>'
        },
        '11fb4626f5c357217e3f3a6c8edc22ee5c837224': {
            'commit_id': '1qxr8YNzP4h',
            'status': 'active',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>'
        },
        '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
            'commit_id': '1qxr8YNzP4h',
            'status': 'obsolete',
            'author': 'Wavid Dalsh <waviddalsh@mozilla.com>'
        }
    },
    'landings': [
        {
            '8eb8319674344fde118b0987b30e22cded00f71b': {
                'status': 'failed',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': '2013-09-07T02:34:18Z',
                'commit_id': 'Bmc6S5XudOp',
                'backout_date': None,
                'landed_revision': None,
                'error': 'Rebase failed, requires manual rebase'
            },
            '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
                'status': 'failed',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': '2013-09-07T02:34:18Z',
                'commit_id': '1qxr8YNzP4h',
                'backout_date': None,
                'landed_revision': None,
                'error': 'Rebase failed, requires manual rebase'
            }
        }, {
            '0acfc2c6fd8e92f33acd90c99c035bd3656286ca': {
                'status': 'backout',
                'repository': 'https://hg.mozilla.org/integration/autoland/',
                'landed_date': '2013-09-07T02:26:18Z',
                'commit_id': '1qxr8YNzP4h',
                'backout_date': '2013-09-07T02:27:18Z',
                'landed_revision': '59117a9f626cf2e954b9bb592efdc69d8169647f',
                'error': None
            }
        }
    ]
}
