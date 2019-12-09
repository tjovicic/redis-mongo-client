import sys
from os import environ as env
import multiprocessing
import logging


def setup_custom_logger(name):
    formatter = logging.Formatter(
        '{"time":"%(asctime)s", "name": "%(name)s", \
        "level": "%(levelname)s", "message": "%(message)s"}'
    )
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    screen_handler.setLevel(logging.INFO)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(screen_handler)
    return logger


logger = setup_custom_logger(__name__)

PORT = int(env.get("PORT", 80))
DEBUG_MODE = int(env.get("DEBUG_MODE", 0))
MONGO_DSN = str(env.get('MONGO_DSN', 'mongodb://mongodb:27017'))
MONGO_DATABASE = str(env.get('MONGO_DATABASE', 'sandbox'))
REDIS_DSN = str(env.get('REDIS_MS_CACHE_DSN', 'redis://redis:6379'))

# Gunicorn config
bind = ":{}".format(str(PORT))
workers = multiprocessing.cpu_count() * 2 + 1
