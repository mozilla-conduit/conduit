FROM alpine

ENV HG_RELEASE=4.1 \
    HG_WEB_CONF=/etc/hg/hgweb.conf

RUN mkdir -p /etc/hg

RUN apk --no-cache add python py-pip
RUN apk --no-cache add --virtual build-dependencies \
      build-base \
      python-dev \
    && pip install --no-cache mercurial==$HG_RELEASE \
    && apk del build-dependencies

ADD dev-requirements.txt /dev-requirements.txt
RUN pip install -r /dev-requirements.txt

VOLUME ["/repos"]

EXPOSE 8080

WORKDIR /repos
CMD exec hg serve --port 8080 --web-conf ${HG_WEB_CONF}
