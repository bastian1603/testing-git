import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def debug(e):
    logging.debug(e)


def info(e):
    logging.info(e)


def warning(e):
    logging.warning(e)


def error(e):
    logging.error(e)


def critical(e):
    logging.critical(e)
