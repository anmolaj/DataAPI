import logging


def get_logger(name=__name__, level=logging.DEBUG):
    """
    Get logger object
    :param name: logger name
    :param level: logging level
    :return: logger object
    """
    
    logger = logging.getLogger(name)
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logger
