# -*- coding: utf-8 -*-
"""
Main module for defining toy robot

"""
from table import Table
import logging

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


class Robot:
    """
    The main robot class which does most of the action here
    """

    def __init__(self):
        logger.debug("robot created table is None")
        self.table = None
