FROM node:7-alpine

MAINTAINER Mozilla <dev-version-control@lists.mozilla.org>

ENV DOCKERIZE_VERSION v0.3.0
ENV MOUNTEBANK_MAJOR_VERSION 1.6
ENV MOUNTEBANK_VERSION 1.6.0
ENV MOUNTEBANK_SHA256 0149ee5c1a7f1f02e0a46e748d16a7a8c7145c459139357e6f73e39f0e716308

# So wget works over SSL
RUN apk --no-cache add openssl

# Install the mountebank nodejs service. See http://www.mbtest.org/docs/install
RUN wget -c -O mountebank.tar.gz https://s3.amazonaws.com/mountebank/v${MOUNTEBANK_MAJOR_VERSION}/mountebank-v${MOUNTEBANK_VERSION}-npm.tar.gz \
    && echo "${MOUNTEBANK_SHA256}  mountebank.tar.gz" | sha256sum -c \
    && tar xf mountebank.tar.gz \
    && rm mountebank.tar.gz

# Install dockerize so that the mountebank logs get sent to docker.
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

EXPOSE 2525 4000

ENTRYPOINT ["/usr/local/bin/dockerize", "-stdout", "/mb.log", "-poll", "/mountebank/bin/mb"]
