# -*- coding: utf-8 -*-
"""
Main module for defining toy robot

"""
import logging

from table import Terrain
from navigation import NavigationSystem


__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)


class Robot:
    """
    The main robot class which does most of the action here
    """
    valid_directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, terrain: Terrain = None):
        logger.debug("robot created table is {}".format(terrain))
        self.terrain = terrain
        self.ready = False
        self.navigation_system = NavigationSystem()

    def set_terrain(self, terrain: Terrain):
        self.terrain = terrain

    def place(self, x_coord: int, y_coord: int, direction: str):
        if self.terrain is None:
            raise ValueError("""Unless robot knows the terrain,
            placement is not possible. Please specify terrain by running
            <robot>.set_terrain(<terrain>)""")

        if(self.terrain.coordinates_within_limits(x_coord, y_coord) and
           direction in self.valid_directions):
            logger.debug("Valid position, placing robot")
            self.ready = True
            self.navigation_system.update(x_coord,
                                          y_coord,
                                          direction,
                                          self.terrain)
        else:
            logger.error("Not a valid position or direction on table.")
            pass

    def position(self):
        return (self.navigation_system.x,
                self.navigation_system.y, self.navigation_system.direction)

    def report(self):
        return str(self)

    def __str__(self) -> str:
        status = str(self.navigation_system)
        return status
