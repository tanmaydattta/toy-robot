# -*- coding: utf-8 -*-
"""
 Coordinate and movement class
"""
import logging
from math import cos, radians, sin

from table import Terrain

__author__ = "tanmay.datta86@gmail.com"
logger = logging.getLogger(__name__)

DIRECTIONS_DEGREES = {"NORTH": 90, "SOUTH": 270, "EAST": 0, "WEST": 180}
DEGREES_DIRECTION = {90: "NORTH", 270: "SOUTH", 0: "EAST", 180: "WEST"}


class NavigationSystem:
    """
    Generic navigation system class to handle robot navigation
    """
    def __init__(self, x: int = None,
                 y: int = None,
                 direction: str = None,
                 terrain: Terrain = None):
        self.x = x
        self.y = y
        self.direction = direction
        self.degree = DIRECTIONS_DEGREES.get(direction, None)
        self.terrain = terrain

    def set_terrain(self, terrain: Terrain):
        """
             Sets the terrain for navigation
            :param terrain:Terrain: Where you want to navigate
        """
        self.terrain = terrain

    def update(self, x: int, y: int,
               direction: str = None,
               terrain: Terrain = None):
        """
        updaets the general navigation required paramters
            :param self: 
            :param x:int: x coordinate
            :param y:int: y cooordinate
            :param direction:str=None: facing direction 
            :param terrain:Terrain=None: terrain on which navigation is happening
        """

        self.terrain = terrain if terrain is not None else self.terrain
        if direction in DIRECTIONS_DEGREES.keys():
            self.x = x
            self.y = y
            self.direction = direction if direction is not None \
                else self.direction
            self.degree = DIRECTIONS_DEGREES.get(direction, None)

    def move(self):
        """
        Move one step at a time
        """
        try:
            new_x = self.x + int(cos(radians(self.degree)))
            new_y = self.y + int(sin(radians(self.degree)))
            if self.terrain.coordinates_within_limits(new_x, new_y):
                self.update(new_x, new_y, self.direction)
            return (self.x, self.y)
        except TypeError as te:
            logger.debug("move threw type error {}".format(te))

    def left(self):
        """
        Face left
        """
        try:
            self.degree += 90
            self.degree = self.degree % 360
            self.direction = DEGREES_DIRECTION.get(self.degree)
        except TypeError as te:
            logger.debug("left threw type error {}".format(te))
            pass

    def right(self):
        """
        Face right
        """
        try:
            self.degree -= 90
            self.degree = self.degree % 360
            self.direction = DEGREES_DIRECTION.get(self.degree)
        except TypeError as te:
            logger.debug("right threw type error {}".format(te))

    def __str__(self) -> str:
        """
        for reporting
        """
        return "Coordinate(x,y): {x}, {y}. Position {direction}".format(
            x=self.x,
            y=self.y, direction=self.direction)
