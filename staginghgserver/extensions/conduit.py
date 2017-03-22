# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.
"""Conduit server extension.

This extension adds a set of API endpoints to the mercurial server to
support the conduit workflow.
See the swagger.yml for the API specification.
"""
import os
import json

from mercurial.hgweb import webcommands
from mercurial.hgweb.common import (
    HTTP_OK,
    HTTP_SERVER_ERROR,
)
import requests

COMMIT_INDEX_URL = os.environ['COMMIT_INDEX_URL']


def extsetup(ui):
    """Standard extension setup routine."""
    setattr(webcommands, 'stage', stage)
    webcommands.__all__.append('stage')


def stage(web, req, tmpl):
    """Proxy to the commit index to stage commits."""
    post_iteration_url = '%s/iterations/' % COMMIT_INDEX_URL
    try:
        iteration_res = requests.post(post_iteration_url,
                                      json={'commits': req.form['commit_ids']})
        data = iteration_res.json()['data']
        commits_list = ', '.join(c['id'] for c in data['commits'])
        message = ('Successfully made Iteration id=%d on Topic id=%d with '
                   'commits: [%s]') % (data['id'], data['topic'], commits_list)
        response = json.dumps({'message': message})
        req.respond(HTTP_OK, 'application/json')
    except:
        # TODO Handle different types of errors appropriately.
        response = format_error('Internal Server Error', HTTP_SERVER_ERROR,
                                'Something went wrong.')
        req.respond(HTTP_SERVER_ERROR, 'application/json')
    return response


def format_error(title, status, detail,
                 type='about:blank', instance='about:blank'):
    """Formats an error according to the RFC7807 spec.

    Returns a json string of the formatted error.
    """
    return json.dumps({
        'type': type, 'title': title, 'status': status,
        'detail': detail, 'instance': instance
    })
