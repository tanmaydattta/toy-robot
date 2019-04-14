# -*- coding: utf-8 -*-
"""
Main module for Table class

"""
import logging

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


class Table:
    """
    Table on which robot will be placed
    """

    def __init__(self, length, width):
        if (length < 1 or width < 1):
            raise ValueError("Table length and width should be more than 0")
        logger.debug("Table init with length: {} width {}".format(length,
                                                                  width))
        self.length = length
        self.width = width

    def is_valid_position(self, x_pos: int, y_pos: int) -> bool:
        """
        Given x and y coordinates return if the location is on table
            :param self: insance
            :param x_pos: x co-ordinate
            :param y_pos: y co-ordinate
        """
        logger.debug("Table with length: {} width {}".format(self.length,
                                                             self.width))
        logger.debug(
            "Position with co-ordinates: x {} y {}".format(x_pos, y_pos))
        return (0 <= x_pos <= self.width) and (0 <= y_pos <= self.length)

    def __str__(self):
        return "Width: {width}, Length: {length}".format(width=self.width,
                                                         length=self.length)
