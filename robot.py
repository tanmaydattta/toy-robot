# -*- coding: utf-8 -*-
"""
Main module for defining toy robot

"""
import logging

from table import Table
from coordinate import Coordiates


__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


class Robot:
    """
    The main robot class which does most of the action here
    """
    valid_directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, table: Table = None):
        logger.debug("robot created table is {}".format(Table))
        self.table = table
        self.ready = False
        self.coordinates = Coordiates()

    def place(self, x_coord: int, y_coord: int, direction: str):
        if(self.table.is_valid_position(x_coord, y_coord) and
           direction in self.valid_directions):
            logger.debug("Valid position, placing robot")
            self.ready = True
            self.coordinates.update(x_coord, y_coord, direction)
        else:
            logger.error("Not a valid position or direction on table.")
            pass

    def position(self):
        return (self.coordinates.x,
                self.coordinates.y, self.coordinates.direction)

    def move(self):
        self.coordinates.move()

    def left(self):
        pass

    def right(self):
        pass
    
    def report(self):
        return str(self)

    def __str__(self) -> str:
        status = str(self.coordinates)
        return status
