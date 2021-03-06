#!/bin/sh
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# This Source Code Form is "Incompatible With Secondary Licenses", as
# defined by the Mozilla Public License, v. 2.0.

# Configure Phabricator on startup from environment variables.

set -e

echo "Starting Phabricator"
echo "Version info:"
echo "phabricator git SHA:  $PHABRICATOR_GIT_SHA"
echo "arcanist git SHA:     $ARCANIST_GIT_SHA"
echo "libphutil Git SHA:    $LIBPHUTIL_GIT_SHA"
HG_VER=$(hg --version | grep -o "(version .*)")
echo "mercurial client: $HG_VER"

set -x

cd phabricator

# Set the local repository and make sure it is readable by the web user.
./bin/config set repository.default-local-path "${REPOSITORY_LOCAL_PATH}"
chown -R www-data:www-data $REPOSITORY_LOCAL_PATH

# Wait for MySQL to come up
wait-for-mysql.php

./bin/config set mysql.host ${MYSQL_HOST}
./bin/config set mysql.port ${MYSQL_PORT}
./bin/config set mysql.user ${MYSQL_USER}
set +x
./bin/config set mysql.pass ${MYSQL_PASS}
set -x

# You should set the base URI to the URI you will use to access Phabricator,
# like "http://phabricator.example.com/".
#
# Include the protocol (http or https), domain name, and port number if you are
# using a port other than 80 (http) or 443 (https).
./bin/config set phabricator.base-uri "${PHABRICATOR_URI}"
./bin/config set security.alternate-file-domain "${PHABRICATOR_URI}"

# FIXME: make this happen on first-run only!
# See 'bin/storage status' for possible first-run control points.
./bin/storage upgrade --force

# NOTE: This works for development, but workers should probably be run in a
# separate container in production.
# Start phd service so Phabricator daemons run.
./bin/phd start

exec php-fpm
