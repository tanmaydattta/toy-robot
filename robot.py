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
    valid_directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, table: Table = None):
        logger.debug("robot created table is {}".format(Table))
        self.table = table
        self.ready = False
        self.direction = None
        self.position = (None, None)

    def place(self, x_coord: int, y_coord: int, direction: str):
        if(self.table.is_valid_position(x_coord, y_coord) and
           direction in self.valid_directions):
            logger.debug("Valid position, placing robot")
            self.position = (x_coord, y_coord)
            self.direction = direction
            self.ready = True
        else:
            logger.error("Not a valid position or direction on table.")
            pass

    def move(self):
        pass

    def left(self):
        pass

    def right(self):
        pass
    
    def report(self):
        return str(self)

    def __str__(self) -> str:
        return "Coordinate(x,y): {x}, {y}. Position {direction}".format(
            x=self.position[0],
            y=self.position[1], direction=self.direction)
