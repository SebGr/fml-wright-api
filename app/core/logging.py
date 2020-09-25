import logging


def create_logger():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )
    logger = logging.getLogger("fml-wright-api")
    return logger
