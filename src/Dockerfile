# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Execute during the build of the image
#ARG TEMPIO_VERSION BUILD_ARCH
#RUN \
#    curl -sSLf -o /usr/bin/tempio \
#    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

# Copy root filesystem
COPY rootfs /
COPY . /bec

# Fix up a few things in the destination directory
RUN \
    set -x \
    && rm -r /bec/rootfs \
    && find /bec -type f | xargs chmod a-x

WORKDIR /bec
RUN \
    set -x \
    && apk add --no-cache --virtual .build-dependencies \
        git \
    && pip install --upgrade pip \
    && pip install --no-cache-dir setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir . \
    && apk del .build-dependencies \
