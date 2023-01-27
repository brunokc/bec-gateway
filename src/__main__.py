import asyncio
import logging

from .service import Service

PROXY_IP = ""
PROXY_PORT = 8080
WEBSOCKET_IP = ""
WEBSOCKET_PORT = 8787

_LOGGER = logging.getLogger(__name__)

def setup_logging():
    logging.basicConfig(level=logging.DEBUG, format="%(name)s: %(message)s")
    _LOGGER.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # formatter = logging.Formatter("%(name)s:%(levelname)s: %(message)s")
    # ch.setFormatter(formatter)

    _LOGGER.addHandler(ch)


if __name__ == "__main__":
    setup_logging()
    service = Service(PROXY_IP, PROXY_PORT, WEBSOCKET_IP, WEBSOCKET_PORT)
    try:
        asyncio.run(service.run())
    except KeyboardInterrupt:
        print("Exiting.")
