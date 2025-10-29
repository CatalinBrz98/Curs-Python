import logging
import sys

logger = logging.getLogger()

formatter = logging.Formatter(fmt="[%(levelname)s] - [%(asctime)s] - [%(message)s]")

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

logger.handlers = [stream_handler]
logger.setLevel(logging.DEBUG)
