# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements
RUN \
    apk add --no-cache \
        python3 \
        py3-pip
#    && pip3 install --no-cache-dir -r src/requirements.txt \

# Execute during the build of the image
#ARG TEMPIO_VERSION BUILD_ARCH
#RUN \
#    curl -sSLf -o /usr/bin/tempio \
#    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_${BUILD_ARCH}"

# Copy root filesystem
COPY rootfs /
COPY . /bec

WORKDIR /bec
RUN \
    set -x \
    rm -r /bec/rootfs \
    && apk add --no-cache --virtual .build-dependencies \
        git \
        python3-dev \
        build-base \
    && pip3 install --no-cache-dir setuptools wheel \
    && pip3 install --no-cache-dir -r requirements.txt \
    # && pip3 install --no-cache-dir -e . \
    && apk del .build-dependencies \
