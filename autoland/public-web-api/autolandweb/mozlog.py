# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# mozlog specification used can be found at
# https://github.com/mozilla-services/Dockerflow/blob/master/docs/mozlog.md
import json
import logging
import time


def tornado_log_function(handler):
    """Log tornado access' in mozlog format.

    This logging function can be used to override the default tornado
    logging function for logging in the mozlog format.
    """
    data = {
        'Timestamp': int(time.time() * 1000000000),
        'Type': 'request.summary',
        'Logger': 'autolandweb.tornado.access',
        # TODO: Add the Hostname.
        # 'Hostname': 'server-a123.mozilla.org',
        'EnvVersion': '2.0',
        # TODO: Properly set the severity based on the type
        # of response that was generated.
        'Severity': 6,
        'Fields': {
            # TODO: Use a proper error code for error
            # responses.
            'errno': 0,
            'status': handler.get_status(),
            'method': handler.request.method,
            'path': handler.request.path,
            't': int(handler.request.request_time() * 1000),
            # TODO: This should include the entire chain of
            # addresses between the client and server.
            'remoteAddressChain': [handler.request.remote_ip]
            # TODO: Add the user id when we actually
            # have access to it.
            # 'uid': '12345'
        }
    }

    agent = handler.request.headers.get('User-Agent')
    if agent is not None:
        data['Fields']['agent'] = agent

    logging.getLogger('tornado.access').info(json.dumps(data))


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'json': {
            'format': '%(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        },
    },
    'loggers': {
        'tornado.access': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}
