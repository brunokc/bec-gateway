# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Execute during the build of the image
#ARG TEMPIO_VERSION BUILD_ARCH
#RUN \
#    curl -sSLf -o /usr/bin/tempio \
#    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

RUN \
    set -x \
    && apk update \
    && apk upgrade \
    && apk add --no-cache --virtual .build-dependencies \
        git \
        build-base \
    && pip install --upgrade pip \
    && pip install --no-cache-dir setuptools wheel

# Copy root filesystem
COPY rootfs /
RUN \
    set -x \
    && chmod 755 /etc/services.d/bec/*

COPY . /bec

# Fix up a few things in the destination directory
RUN \
    set -x \
    && rm -r /bec/rootfs \
    && find /bec -type f | xargs chmod a-x

WORKDIR /bec
RUN \
    pip install --no-cache-dir -r requirements.txt \
    # && pip install --no-cache-dir . \
    && apk del --purge .build-dependencies \
