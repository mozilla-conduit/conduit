FROM alpine:3.5

ENV HG_RELEASE=4.1 \
    VCT_VERSION=tip

WORKDIR /root

RUN apk --no-cache add python ca-certificates curl
RUN apk --no-cache add --virtual build-dependencies \
      build-base \
      python-dev \
      py-pip \
    && pip install --no-cache simplejson \
    && pip install --no-cache mercurial==$HG_RELEASE \
    && apk del build-dependencies

RUN hg clone https://hg.mozilla.org/hgcustom/version-control-tools -r $VCT_VERSION /root/version-control-tools

COPY hgrc /root/.hgrc

CMD /bin/sh
