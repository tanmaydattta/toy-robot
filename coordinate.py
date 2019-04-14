# -*- coding: utf-8 -*-
"""
 Coordinate and movement class
"""


class Coordiates:

    def __init__(self, x: int = None, y: int = None, direction: str = None):
        self.x = x
        self.y = y
        self.direction = direction

    def update(self, x: int = None, y: int = None, direction: str = None):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == "NORTH":
            self.y += 1
        if self.direction == "EAST":
            self.x += 1
        if self.direction == "SOUTH":
            self.y -= 1
        if self.direction == "WEST":
            self.x -= 1
        return (self.x, self.y)
    
    def __str__(self) -> str:
        return "Coordinate(x,y): {x}, {y}. Position {direction}".format(
            x=self.x,
            y=self.y, direction=self.direction)
