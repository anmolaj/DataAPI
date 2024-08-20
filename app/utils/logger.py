import logging


def get_logger(name=__name__):
    """
    Get logger object
    :param name: logger name
    :return: logger object
    """
    
    logger = logging.getLogger(name)
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        level=logging.DEBUG,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logger
