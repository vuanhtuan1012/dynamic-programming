# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2022-04-05 07:46:24
# @Email:  anh-tuan.vu@outlook.com
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2022-04-05 07:51:03

import logging
from time import perf_counter


def getLogger(logger_name: str, **kwargs) -> logging.Logger:
    """Get a logger

    Args:
        logger_name (str): logger's name
        **kwargs: Description

    Returns:
        logging.Logger: logger
    """
    # get arguments
    level = kwargs.get('level', logging.INFO)
    streaming = kwargs.get('streaming', True)
    storing = kwargs.get('storing', False)
    log_file = kwargs.get('log_file', None)

    # common settings
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    formatter = logging.Formatter('%(message)s')

    if streaming:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(stream_handler)

    if storing and log_file is not None:
        file_handler = logging.FileHandler(log_file, mod='w',
                                           encoding='utf-8')
        file_handler.setFormatter(formatter)
        if (not streaming) and logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(file_handler)
    return logger


def timer(func: str):
    """Decorator for displaying time execution of a function

    Args:
        func (str): function name

    Returns:
        TYPE: Description
    """
    def wrapper(*args, **kwargs):
        logger = getLogger('timer')
        # logger.info(f'executing function {func.__name__}...')
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        logger.info(f'function {func.__name__}() took'
                    f' {round(end-start, 3)} seconds')
        return result
    return wrapper
