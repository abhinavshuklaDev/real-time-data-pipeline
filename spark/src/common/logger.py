import logging
import sys


def get_logger(name):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

    )

    console = logging.StreamHandler(sys.stdout)

    console.setFormatter(formatter)

    logger.addHandler(console)

    return logger