import asyncio
import logging
import sys

from .service import Service

PROXY_IP = ""
PROXY_PORT = 8080
WEBSOCKET_IP = ""
WEBSOCKET_PORT = 8787
WEBSOCKET_URL = "/api/websocket"

_LOGGER = logging.getLogger(__name__)

def setup_logging(log_level: str) -> None:
    level = logging.getLevelName(log_level.upper())
    if not isinstance(level, int):
        # If the level name is not found, getLevelName() return a string of the
        # form "Level <level>". If that's the case, default to 'warning' level
        level = logging.WARNING

    logging.basicConfig(level=level, format="%(name)s: %(message)s")
    _LOGGER.setLevel(level)

    # create console handler and set level appropriately
    ch = logging.StreamHandler()
    ch.setLevel(level)

    _LOGGER.addHandler(ch)


if __name__ == "__main__":
    log_level = sys.argv[1]
    setup_logging(log_level)
    service = Service(PROXY_IP, PROXY_PORT, WEBSOCKET_IP, WEBSOCKET_PORT, WEBSOCKET_URL)
    try:
        asyncio.run(service.run())
    except KeyboardInterrupt:
        print("Exiting.")
