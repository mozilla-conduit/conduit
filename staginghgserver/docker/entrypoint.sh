#!/bin/sh
cd /repos
exec hg serve --port 8080 --web-conf ${HG_WEB_CONF}
