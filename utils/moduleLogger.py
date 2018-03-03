# Created by ioluwayo on 2018-02-11.
import logging
def init_logger(name, level = logging.DEBUG): # default level is DEBUG
    # define a Handler which writes level messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(level)
    # set a format
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger(name).addHandler(console)
    logger = logging.getLogger(name)
    logger.setLevel(level) # set the level
    return logger


