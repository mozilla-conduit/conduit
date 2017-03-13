FROM alpine

ENV HG_RELEASE=4.1 \
    HG_WEB_CONF=/etc/hg/hgweb.conf

RUN mkdir -p /etc/hg

RUN apk --no-cache add python
RUN apk --no-cache add --virtual build-dependencies \
      build-base \
      python-dev \
      py-pip \
    && pip install --no-cache mercurial==$HG_RELEASE \
    && apk del build-dependencies

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME ["/repos"]

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]
