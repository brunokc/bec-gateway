docker build --build-arg BUILD_FROM=ghcr.io/home-assistant/amd64-base-python:3.10-alpine3.16 -t bec src

docker rm -f bectest
docker run -d -p 8080:8080 -p 8787:8787 -e LOG_LEVEL_OVERRIDE=debug --name bectest bec
